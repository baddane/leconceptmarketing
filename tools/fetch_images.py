#!/usr/bin/env python3
"""Rapatrie les illustrations perdues depuis les captures de l'Internet Archive.

La mediatheque de leconceptmarketing.com ne repond plus : toutes les URL
wp-content renvoient 404. Ce script retrouve chaque image dans Wayback, la
stocke sous public/images/ et ecrit public/images/manifest.json, que le site
consulte au build pour recabler les <img>.

Le script est reprenable : relance-le autant de fois que necessaire, il ne
retelecharge que ce qui manque.

Usage:
  python3 tools/fetch_images.py                 # tout ce qui manque
  python3 tools/fetch_images.py --limit 50      # echantillon
  python3 tools/fetch_images.py --dry-run       # liste sans telecharger
"""
import argparse, hashlib, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(HERE, "content")
IMAGES = os.path.join(HERE, "public", "images")
MANIFEST = os.path.join(IMAGES, "manifest.json")
INDEX = os.path.join(IMAGES, ".cdx-index.json")
FAILED = os.path.join(IMAGES, ".failed.json")

UA = "Mozilla/5.0 (X11; Linux x86_64) leconceptmarketing-archive-restore"
LOST = re.compile(r"^https?://(?:i[0-9]\.wp\.com/)?(?:www\.)?leconceptmarketing\.com/", re.I)
IMG_IN_BODY = re.compile(r"!\[[^\]]*\]\((https?://[^)\s]+)\)")
COVER = re.compile(r'^cover: "(https?://[^"]+)"$', re.M)
EXTS = {"image/jpeg": ".jpg", "image/png": ".png", "image/gif": ".gif",
        "image/webp": ".webp", "image/svg+xml": ".svg", "image/avif": ".avif"}
# Suffixe de taille ajoute par WordPress: image-1-1024x771.png -> image-1.png
SIZE_SUFFIX = re.compile(r"-\d{2,5}x\d{2,5}(?=\.[a-z0-9]+$)", re.I)


def key(url):
    """Meme cle que src/lib/images.mjs : sans protocole, sans prefixe CDN,
    sans query, et toujours decodee (les captures melangent les deux formes)."""
    url = re.sub(r"^https?://", "", str(url)).split("?")[0]
    url = re.sub(r"^i[0-9]\.wp\.com/", "", url)
    return urllib.parse.unquote(url)


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=0, sort_keys=True)
    os.replace(tmp, path)


def collect_urls():
    """Toutes les URL d'images perdues citees par l'archive, dedupliquees."""
    urls = {}
    for name in sorted(os.listdir(CONTENT)):
        if not name.endswith(".md"):
            continue
        text = open(os.path.join(CONTENT, name), encoding="utf-8").read()
        found = IMG_IN_BODY.findall(text) + COVER.findall(text)
        for url in found:
            url = url.strip().rstrip(".,;)")
            if LOST.match(url):
                urls.setdefault(key(url), url)
    return urls


def fetch(url, timeout=60):
    # Les noms de fichiers WordPress contiennent des accents et des apostrophes.
    url = urllib.parse.quote(url, safe=":/?&=%~+,*!$'()@;")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read(), resp.headers.get("Content-Type", "")


def cdx_prefixes(urls):
    """Dossiers mensuels WordPress cites par l'archive, du plus fourni au reste."""
    counts = {}
    for k in urls:
        m = re.search(r"(/wp-content/uploads/\d{4}/\d{2})/", k)
        prefix = m.group(1) if m else "/wp-content/uploads"
        counts[prefix] = counts.get(prefix, 0) + 1
    return [p for p, _ in sorted(counts.items(), key=lambda kv: -kv[1])]


def cdx_query(prefix, attempts=5):
    """Une requete CDX par dossier : la requete globale est tronquee cote serveur."""
    target = "leconceptmarketing.com%s/*" % prefix
    url = ("https://web.archive.org/cdx/search/cdx?url=" + urllib.parse.quote(target, safe="")
           + "&output=json&fl=original,timestamp,statuscode&collapse=urlkey&limit=50000")
    delay = 3
    for attempt in range(attempts):
        try:
            body, _ = fetch(url, timeout=180)
            rows = json.loads(body.decode("utf-8", "replace"))
            return {key(o): ts for o, ts, code in rows[1:] if code == "200"}
        except Exception as exc:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 60)
    return {}


def build_cdx_index(urls, refresh=False):
    """Index original -> timestamp, construit dossier par dossier et mis en cache.

    Chaque dossier resolu est enregistre immediatement : une interruption ou une
    indisponibilite de l'Internet Archive ne fait perdre que le dossier en cours.
    """
    cache = load(INDEX, {}) if not refresh else {}
    index = cache.get("entries", {})
    done = set(cache.get("done", []))
    prefixes = [p for p in cdx_prefixes(urls) if p not in done]
    if not prefixes:
        return index

    print("Index CDX : %d dossiers a interroger (%d deja en cache)"
          % (len(prefixes), len(done)), flush=True)
    for i, prefix in enumerate(prefixes, 1):
        try:
            found = cdx_query(prefix)
        except Exception as exc:
            print("  %s : indisponible (%s)" % (prefix, str(exc)[:60]), flush=True)
            continue
        index.update(found)
        done.add(prefix)
        save(INDEX, {"entries": index, "done": sorted(done)})
        print("  [%d/%d] %s : %d captures (total %d)"
              % (i, len(prefixes), prefix, len(found), len(index)), flush=True)
        time.sleep(1)
    return index


def candidates(url, index):
    """Timestamps a essayer, en retombant sur l'image non redimensionnee."""
    out = []
    k = key(url)
    if k in index:
        out.append((index[k], "https://" + k))
    base = SIZE_SUFFIX.sub("", k)
    if base != k and base in index:
        out.append((index[base], "https://" + base))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="nombre maximum d'images a traiter")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--refresh-index", action="store_true")
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()

    urls = collect_urls()
    manifest = load(MANIFEST, {})
    failed = load(FAILED, {})
    if args.retry_failed:
        failed = {}

    todo = [(k, u) for k, u in sorted(urls.items())
            if k not in manifest and (args.retry_failed or k not in failed)]
    print("images citees: %d | deja rapatriees: %d | en echec: %d | a traiter: %d"
          % (len(urls), len(manifest), len(failed), len(todo)), flush=True)
    if args.dry_run:
        for k, u in todo[:20]:
            print("   ", u)
        if len(todo) > 20:
            print("    ... (+%d)" % (len(todo) - 20))
        return 0
    if not todo:
        return 0

    os.makedirs(IMAGES, exist_ok=True)
    try:
        index = build_cdx_index(urls, args.refresh_index)
    except Exception as exc:
        print("ERREUR: index CDX indisponible (%s)." % exc)
        print("L'Internet Archive est peut-etre hors ligne: relancez plus tard.")
        return 1

    if args.limit:
        todo = todo[:args.limit]

    ok = miss = err = 0
    for i, (k, url) in enumerate(todo, 1):
        tries = candidates(url, index)
        if not tries:
            failed[k] = "aucune capture"
            miss += 1
            continue
        for ts, original in tries:
            replay = "https://web.archive.org/web/%sim_/%s" % (ts, original)
            try:
                data, ctype = fetch(replay)
            except Exception as exc:
                failed[k] = str(exc)[:120]
                err += 1
                break
            if len(data) < 128 or not ctype.split(";")[0].startswith("image/"):
                failed[k] = "reponse non-image"
                continue
            ext = EXTS.get(ctype.split(";")[0], os.path.splitext(k)[1] or ".jpg")
            name = hashlib.sha1(k.encode("utf-8")).hexdigest()[:16] + ext
            with open(os.path.join(IMAGES, name), "wb") as f:
                f.write(data)
            manifest[k] = name
            failed.pop(k, None)
            ok += 1
            break
        else:
            miss += 1
        if i % 25 == 0:
            save(MANIFEST, manifest)
            save(FAILED, failed)
            print("  %d/%d  ok=%d absentes=%d erreurs=%d" % (i, len(todo), ok, miss, err), flush=True)
        time.sleep(args.delay)

    save(MANIFEST, manifest)
    save(FAILED, failed)
    print("TERMINE  rapatriees=%d absentes=%d erreurs=%d  total manifest=%d"
          % (ok, miss, err, len(manifest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
