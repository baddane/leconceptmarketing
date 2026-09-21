#!/usr/bin/env python3
"""Reconstruit content/*.md a partir des captures brutes Wayback de dump/.

Source de verite: dump/ (HTML WordPress original, theme tagDiv Newspaper).
Sortie: un fichier Markdown par page, avec frontmatter YAML.

Usage: python3 tools/extract.py [--limit N] [--only SLUG]
"""
import argparse, csv, datetime, gzip, html, json, os, re, sys, unicodedata, urllib.parse
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DUMP = os.path.join(HERE, "dump")
OUT = os.path.join(HERE, "content")
MANIFEST = os.path.join(HERE, "manifest.csv")
DOMAIN = "leconceptmarketing.com"

# Archives et pages generees par le theme: on les reconstruit nous-memes.
SKIP_PREFIX = ("category__", "tag__", "author__")
SKIP_EXACT = {"__home__", "author"}
# Pages WooCommerce/transactionnelles sans contenu editorial recuperable.
SKIP_SLUGS = {"panier", "commander", "mon-compte", "boutique", "page-d-exemple",
              "affiliate-home", "affiliate-home__affiliate-login", "buy-adspace"}

# Le theme rend certaines categories en capitales ou avec une coquille:
# on retablit le libelle canonique sans fusionner de categories distinctes.
CATEGORY_ALIASES = {
    "INTELLIGENCE ARTIFICIELLE": "Intelligence artificielle",
    "Moteurs de Recherche": "Moteurs de recherche",
    "Wordpress": "WordPress",
    "Woocommerce": "WooCommerce",
    "Thémes": "Thèmes",
}

# Blocs injectes par les plugins WP: jamais du contenu d'article.
DROP_SELECTORS = [
    "script", "style", "noscript", "ins", "iframe[src*='doubleclick']",
    ".saboxplugin-wrap", "#ez-toc-container", ".ez-toc-title-container",
    ".code-block", ".td-a-rec", ".adsbygoogle", ".sharedaddy", ".jp-relatedposts",
    ".wp-block-latest-posts", ".yuzo_related_post", ".crp_related",
    ".td-post-sharing", ".td-post-source-tags", ".post-views",
    "form", ".wp-block-search", ".td-post-next-prev", "#comments", ".comment-respond",
]


class Conv(MarkdownConverter):
    """markdownify avec des reglages adaptes au contenu WordPress."""

    def convert_img(self, el, text, parent_tags=None):
        src = (el.get("data-src") or el.get("data-lazy-src") or el.get("src") or "").strip()
        if not src or src.startswith("data:"):
            return ""
        alt = (el.get("alt") or "").strip().replace("\n", " ")
        return "![%s](%s)" % (alt, src)

    def convert_a(self, el, text, parent_tags=None):
        href = (el.get("href") or "").strip()
        if not href or href.startswith(("javascript:", "#")):
            return text
        return "[%s](%s)" % (text, href) if text.strip() else ""


def md(node):
    return Conv(heading_style="ATX", bullets="-", strip=["span", "font"]).convert_soup(node)


def load_manifest():
    m = {}
    if os.path.exists(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as f:
            for row in csv.reader(f):
                if len(row) >= 3:
                    m[row[2]] = (row[0], row[1])
    return m


def jsonld(soup):
    """Renvoie les noeuds @graph du schema Yoast, indexes par @type."""
    out = {}
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or "")
        except Exception:
            continue
        for node in data.get("@graph", []) if isinstance(data, dict) else []:
            t = node.get("@type")
            for t in (t if isinstance(t, list) else [t]):
                out.setdefault(t, node)
    return out


def to_utc(value):
    if not value:
        return ""
    try:
        return datetime.datetime.fromisoformat(value).astimezone(
            datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    except ValueError:
        return ""


def meta(soup, **kw):
    tag = soup.find("meta", attrs=kw)
    return html.unescape((tag.get("content") or "").strip()) if tag else ""


def clean_text(value):
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def ascii_slug(value):
    """Slug ASCII: le site d'origine prefixait certains permaliens d'un caractere
    decoratif qui ne survit pas proprement a l'encodage d'URL."""
    value = unicodedata.normalize("NFD", value)
    value = "".join(c for c in value if unicodedata.category(c) != "Mn")
    value = value.lower().replace("\u2019", "").replace("'", "")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def normalize_permalink(permalink, fallback_slug):
    """Renvoie (permalien canonique ASCII, permalien d'origine decode)."""
    legacy = urllib.parse.unquote(permalink)
    slug = legacy.strip("/").split("/")[-1]
    if "?" in legacy or "=" in slug or not slug:
        slug = fallback_slug
    clean = ascii_slug(slug) or ascii_slug(fallback_slug) or "page"
    return "/%s/" % clean, legacy


def absolutize(url, base):
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return base.rstrip("/") + url
    return url


def body_markdown(soup):
    node = (soup.select_one(".td-post-content")
            or soup.select_one(".td-page-content")
            or soup.select_one(".amp-wp-article-content")
            or soup.select_one(".tdb_single_content"))
    if node is None:
        # Pages construites avec WPBakery: le corps est eclate en blocs .wpb_wrapper.
        blocks = soup.select(".td-main-content .wpb_wrapper, .td-ss-main-content .wpb_wrapper")
        if not blocks:
            return ""
        node = soup.new_tag("div")
        for b in blocks:
            node.append(b)
    for sel in DROP_SELECTORS:
        for tag in node.select(sel):
            tag.decompose()
    # CTA "Lire aussi" injectes en plein milieu des paragraphes.
    for tag in node.select("span.ctaText, span.postTitle"):
        parent = tag.find_parent("a") or tag
        parent.decompose()
    text = md(node)
    return tidy(text)


JUNK_LINE = re.compile(
    r"^\s*(?:\*\*)?(?:"
    r"partager|partagez|tweet(?:er)?|pin(?:terest)?|whatsapp|linkedin|telegram|"
    r"article pr[ée]c[ée]dent|article suivant|articles? (?:similaires?|connexes?)|"
    r"laisser un commentaire|votre adresse e-?mail.*|enregistrer mon nom.*|"
    r"rechercher|recherche|sommaire|table des mati[èe]res|tags?|partage[rz]?\s*:|"
    r"cet article vous a[- ]t[- ]il [ée]t[ée] utile.*"
    r")(?:\*\*)?\s*:?\s*$", re.I)


HEADING_BOLD = re.compile(r"^(#{1,6})\s*\*\*(.+?)\*\*\s*$")

# WordPress inserait des <br> a l'interieur des <script>: la balise se refermait
# trop tot et la suite du code se retrouvait en texte dans les <p> suivants.
SCRIPT_LEFTOVER = re.compile(
    r"googletagmanager|dataLayer|gtm\.start|fbq\(|connect\.facebook\.net|"
    r"CookiesEuBanner|adsbygoogle|googlesyndication|platform\.twitter\.com/widgets|"
    r"document\.createElement|getElementsByTagName|insertBefore\(|_stq|"
    r"\(function\(w,\s*d,\s*s|window\.addEventListener\(|new Date\(\)\.getTime\(\)",
    re.I)


# Balises restees en texte a cause du balisage casse de l'export WordPress.
# On ne retire que celles qui portent des attributs ou qui sont collees au
# texte: un article peut citer <div> ou <IFRAME> a dessein, entoure d'espaces.
TAG_WITH_ATTRS = re.compile(r"</?(?:div|span|a|br|p|section|figure|table|td|tr|ul|li|img|iframe)\b[^>]*=[^>]*>", re.I)
TAG_GLUED = re.compile(r"(?<=\w)</?(?:div|span|p|br)\s*/?>|</?(?:div|span|p|br)\s*/?>(?=\w)", re.I)


def drop_stray_markup(text):
    text = TAG_WITH_ATTRS.sub("", text)
    return TAG_GLUED.sub("", text)


def unescape_outside_code(text):
    """Decode les entites HTML restees litterales, sauf dans les extraits de
    code ou elles peuvent etre le sujet meme de l'article."""
    parts, fenced = [], False
    for block in text.split("\n\n"):
        fences = block.count("```")
        if fenced or fences:
            fenced ^= fences % 2 == 1
            parts.append(block)
            continue
        parts.append(html.unescape(block))
    return "\n\n".join(parts)


# Un appel de fonction suivi de ; ou {, ou une ligne de fermeture seule.
CODE_STATEMENT = re.compile(
    r"[\w$.\]]\s*\([^()]{0,160}\)\s*[;{]|^\s*[}\])]{1,4}\s*[;,)]?\s*$", re.M)
# Le francais met une espace avant le point-virgule, donc "(SEO) ;" ressemble a
# du code: on n'ecarte un bloc que s'il ne contient presque pas de mots francais.
FRENCH_WORDS = re.compile(
    r"\b(le|la|les|de|des|du|un|une|et|est|pour|dans|vous|nous|que|qui|sur|avec"
    r"|plus|par|ce|cette|au|aux|en|sont|ne|pas|son|ses|votre|vos|il|elle|on)\b", re.I)


def looks_injected(block):
    if not CODE_STATEMENT.search(block):
        return False
    return len(FRENCH_WORDS.findall(block)) < 3 and len(block.split()) < 40


def drop_script_leftovers(text):
    """Retire les blocs de code injecte, sans toucher aux extraits de code
    des tutoriels, qui eux sont balises comme tels."""
    kept, fenced = [], False
    for block in text.split("\n\n"):
        fences = block.count("```")
        if fenced or fences:
            fenced ^= fences % 2 == 1
            kept.append(block)
            continue
        if SCRIPT_LEFTOVER.search(block) or looks_injected(block):
            continue
        kept.append(block)
    return "\n\n".join(kept)


def tidy(text):
    lines = []
    for line in text.split("\n"):
        line = line.rstrip()
        if line and JUNK_LINE.match(line):
            continue
        # Les titres du theme sont souvent doublement emphases.
        line = HEADING_BOLD.sub(r"\1 \2", line)
        # Liens vides ou images fantomes laisses par les widgets.
        if re.fullmatch(r"\s*\[\]\([^)]*\)\s*", line):
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = drop_script_leftovers(text)
    text = drop_stray_markup(text)
    text = unescape_outside_code(text)
    text = text.replace(" ", " ").replace("​", "")
    text = "".join(ch for ch in text if ch >= " " or ch in "\n\t")
    return text.strip()


def yaml_str(value):
    return '"%s"' % str(value).replace("\\", "\\\\").replace('"', '\\"')


def yaml_list(values):
    return "[%s]" % ",".join(yaml_str(v) for v in values)


def read_dump(path):
    """Certaines captures Wayback sont servies en gzip brut, non decode."""
    raw = open(path, "rb").read()
    if raw[:2] == b"\x1f\x8b":
        try:
            raw = gzip.decompress(raw)
        except OSError:
            raw = gzip.GzipFile(fileobj=__import__("io").BytesIO(raw)).read()
    return raw.replace(b"\x00", b"")


def extract(path, manifest):
    fname = os.path.basename(path)
    slug = fname[:-5]
    if slug in SKIP_EXACT or slug.startswith(SKIP_PREFIX) or slug in SKIP_SLUGS:
        return None, "skip:archive"
    if slug.endswith("__amp"):
        return None, "skip:amp"

    raw = read_dump(path)
    soup = BeautifulSoup(raw.decode("utf-8", "replace"), "lxml")
    graph = jsonld(soup)
    article = graph.get("Article") or graph.get("BlogPosting") or graph.get("NewsArticle") or {}
    webpage = graph.get("WebPage") or graph.get("ItemPage") or {}

    body = body_markdown(soup)
    if len(body) < 200:
        return None, "skip:empty-body"

    origin, capture = manifest.get(fname, ("", ""))
    canonical = soup.find("link", rel="canonical")
    url = (canonical.get("href") if canonical else "") or webpage.get("url") or origin
    permalink = re.sub(r"^https?://[^/]+", "", url) or "/%s/" % slug
    if not permalink.endswith("/"):
        permalink += "/"
    permalink, legacy = normalize_permalink(permalink, slug)

    h1 = soup.select_one("h1.entry-title")
    title = clean_text(
        (h1.get_text() if h1 else "")
        or article.get("headline", "")
        or meta(soup, property="og:title")
        or (soup.title.get_text() if soup.title else ""))
    title = re.sub(r"\s*[-|]\s*Le Concept Marketing.*$", "", title)

    time_tag = soup.select_one("time.entry-date")
    date = to_utc(article.get("datePublished") or webpage.get("datePublished")
                  or (time_tag.get("datetime") if time_tag else ""))
    modified = to_utc(article.get("dateModified") or webpage.get("dateModified") or "")

    author_node = graph.get("Person") or article.get("author") or {}
    author = clean_text(author_node.get("name", "")) if isinstance(author_node, dict) else ""
    if not author:
        a = soup.select_one(".td-post-author-name a")
        author = clean_text(a.get_text()) if a else ""

    categories = [clean_text(a.get_text())
                  for a in soup.select("ul.td-category li.entry-category a")]
    categories = [CATEGORY_ALIASES.get(c, c) for c in categories]
    categories = [c for c in dict.fromkeys(categories) if c]

    tags = [clean_text(a.get_text())
            for a in soup.select(".td-post-source-tags .td-tags li a")]
    tags = [t for t in dict.fromkeys(tags) if t and t.lower() != "tags"]

    description = clean_text(meta(soup, name="description")
                             or meta(soup, property="og:description"))
    # Yoast tronque avec des points de suspension espaces: ". . ."
    description = re.sub(r"[\s.\u2026]+$", "", description)
    cover = meta(soup, property="og:image")
    if cover.endswith((".svg",)) or "gravatar" in cover:
        cover = ""

    kind = "post" if (date and (soup.select_one(".td-post-content")
                                or soup.select_one(".amp-wp-article-content"))) else "page"

    fm = [
        "---",
        "title: " + yaml_str(title),
        "permalink: " + yaml_str(permalink),
        "legacy_permalinks: __LEGACY__",
        "type: " + yaml_str(kind),
        "date: " + yaml_str(date),
        "modified: " + yaml_str(modified),
        "author: " + yaml_str(author),
        "categories: " + yaml_list(categories),
        "tags: " + yaml_list(tags),
        "description: " + yaml_str(description[:300]),
        "cover: " + yaml_str(absolutize(cover, "https://" + DOMAIN)),
        "source_url: " + yaml_str(origin or url),
        "source_capture: " + yaml_str(capture),
        "---",
        "",
    ]
    return slug, {
        "permalink": permalink,
        "legacy": legacy if legacy != permalink else "",
        "size": len(body),
        "text": "\n".join(fm) + body + "\n",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only")
    args = ap.parse_args()

    manifest = load_manifest()
    files = sorted(f for f in os.listdir(DUMP) if f.endswith(".html"))
    if args.only:
        files = [f for f in files if args.only in f]
    if args.limit:
        files = files[:args.limit]

    os.makedirs(OUT, exist_ok=True)
    stats = {}
    pages = {}
    for fname in files:
        slug, payload = extract(os.path.join(DUMP, fname), manifest)
        if slug is None:
            stats[payload] = stats.get(payload, 0) + 1
            continue
        pages[slug] = payload

    # Deux captures peuvent viser le meme permalien (variante decorative de
    # l'URL): on garde la version la plus complete et on redirige l'autre.
    by_permalink = {}
    for slug, page in pages.items():
        by_permalink.setdefault(page["permalink"], []).append(slug)

    dropped = 0
    for permalink, slugs in by_permalink.items():
        if len(slugs) < 2:
            continue
        slugs.sort(key=lambda s: pages[s]["size"], reverse=True)
        keeper = slugs[0]
        for other in slugs[1:]:
            legacy = pages[other]["legacy"] or pages[other]["permalink"]
            if legacy and legacy != permalink:
                pages[keeper].setdefault("extra", []).append(legacy)
            del pages[other]
            dropped += 1

    if not args.only and not args.limit:
        for stale in os.listdir(OUT):
            if stale.endswith(".md") and stale[:-3] not in pages:
                os.remove(os.path.join(OUT, stale))

    for slug, page in pages.items():
        legacy = [l for l in [page["legacy"], *page.get("extra", [])] if l]
        text = page["text"].replace("__LEGACY__", yaml_list(dict.fromkeys(legacy)))
        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as f:
            f.write(text)

    write_vercel_config(pages)
    print("ecrits: %d / %d  (doublons fusionnes: %d)" % (len(pages), len(files), dropped))
    for k, v in sorted(stats.items()):
        print("  %-22s %d" % (k, v))


def write_vercel_config(pages):
    """Redirections 301 des anciennes URL vers les permaliens canoniques."""
    redirects = []
    seen = set()
    for page in pages.values():
        for legacy in [page["legacy"], *page.get("extra", [])]:
            if not legacy or legacy == page["permalink"]:
                continue
            if "?" in legacy:
                # Ancien lien court WordPress: /?p=1234
                query = urllib.parse.parse_qs(urllib.parse.urlparse(legacy).query)
                post_id = (query.get("p") or [""])[0].strip("/")
                if not post_id or post_id in seen:
                    continue
                seen.add(post_id)
                redirects.append({
                    "source": "/",
                    "has": [{"type": "query", "key": "p", "value": post_id}],
                    "destination": page["permalink"],
                    "permanent": True,
                })
                continue
            for source in dict.fromkeys([legacy, urllib.parse.quote(legacy, safe="/")]):
                if source in seen or source == page["permalink"]:
                    continue
                seen.add(source)
                redirects.append({
                    "source": source.rstrip("/"),
                    "destination": page["permalink"],
                    "permanent": True,
                })
    redirects.sort(key=lambda r: (r["source"], r["destination"]))
    config = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        # Explicite plutot qu'auto-detecte: le projet Vercel peut avoir ete cree
        # avant l'ajout du site et rester sur un preset vide.
        "framework": "astro",
        "buildCommand": "astro build",
        "outputDirectory": "dist",
        "trailingSlash": True,
        "cleanUrls": False,
        "redirects": redirects,
        "headers": [
            {
                "source": "/images/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}],
            },
            {
                "source": "/_astro/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}],
            },
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                    {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                ],
            },
        ],
    }
    with open(os.path.join(HERE, "vercel.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
