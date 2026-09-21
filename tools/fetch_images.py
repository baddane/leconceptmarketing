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
import argparse, hashlib, json, os, re, sys, threading, time
import urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

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


class Throttle:
    """L'archive limite le debit : on espace les departs de requete, quel que
    soit le nombre de fils, sinon elle repond 503 en rafale."""

    def __init__(self, interval):
        self.interval = interval
        self.lock = threading.Lock()
        self.last = 0.0

    def wait(self):
        with self.lock:
            pause = self.interval - (time.monotonic() - self.last)
            if pause > 0:
                time.sleep(pause)
            self.last = time.monotonic()


CDX_THROTTLE = Throttle(2.5)
REPLAY_THROTTLE = Throttle(0.35)


def cdx_query(prefix, attempts=4):
    """Une requete CDX par dossier : la requete globale est tronquee cote serveur."""
    target = "leconceptmarketing.com%s/*" % prefix
    url = ("https://web.archive.org/cdx/search/cdx?url=" + urllib.parse.quote(target, safe="")
           + "&output=json&fl=original,timestamp,statuscode&collapse=urlkey&limit=50000")
    delay = 15
    for attempt in range(attempts):
        try:
            CDX_THROTTLE.wait()
            body, _ = fetch(url, timeout=90)
            rows = json.loads(body.decode("utf-8", "replace"))
            return {key(o): ts for o, ts, code in rows[1:] if code == "200"}
        except Exception as exc:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 120)
    return {}


def build_cdx_index(urls, refresh=False, workers=2):
    """Index original -> timestamp, construit dossier par dossier et mis en cache.

    Les requetes partent par petits lots : l'Internet Archive repond lentement et
    renvoie souvent 503, mais tolere quelques requetes simultanees. Chaque dossier
    resolu est enregistre aussitot, donc une interruption ne coute que le lot en cours.
    """
    cache = load(INDEX, {}) if not refresh else {}
    index = cache.get("entries", {})
    done = set(cache.get("done", []))
    prefixes = [p for p in cdx_prefixes(urls) if p not in done]
    if not prefixes:
        return index

    print("Index CDX : %d dossiers a interroger (%d deja en cache)"
          % (len(prefixes), len(done)), flush=True)
    lock = threading.Lock()
    failures = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(cdx_query, p): p for p in prefixes}
        for n, future in enumerate(as_completed(futures), 1):
            prefix = futures[future]
            try:
                found = future.result()
            except Exception as exc:
                failures += 1
                print("  [%d/%d] %s : indisponible (%s)"
                      % (n, len(prefixes), prefix, str(exc)[:60]), flush=True)
                continue
            with lock:
                index.update(found)
                done.add(prefix)
                save(INDEX, {"entries": index, "done": sorted(done)})
            print("  [%d/%d] %s : %d captures (total %d)"
                  % (n, len(prefixes), prefix, len(found), len(index)), flush=True)
    if failures:
        print("  %d dossiers injoignables : relancez le script pour les reprendre."
              % failures, flush=True)
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
    ap.add_argument("--workers", type=int, default=4,
                    help="telechargements simultanes")
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

    counts = {"ok": 0, "miss": 0, "err": 0}
    lock = threading.Lock()

    def restore(item):
        k, url = item
        tries = candidates(url, index)
        if not tries:
            return k, None, "aucune capture"
        for ts, original in tries:
            replay = "https://web.archive.org/web/%sim_/%s" % (ts, original)
            try:
                REPLAY_THROTTLE.wait()
                data, ctype = fetch(replay)
            except Exception as exc:
                return k, None, str(exc)[:120]
            mime = ctype.split(";")[0]
            if len(data) < 128 or not mime.startswith("image/"):
                continue
            ext = EXTS.get(mime, os.path.splitext(k)[1] or ".jpg")
            name = hashlib.sha1(k.encode("utf-8")).hexdigest()[:16] + ext
            with open(os.path.join(IMAGES, name), "wb") as f:
                f.write(data)
            return k, name, None
        return k, None, "aucune capture exploitable"

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(restore, item) for item in todo]
        for n, future in enumerate(as_completed(futures), 1):
            k, name, problem = future.result()
            with lock:
                if name:
                    manifest[k] = name
                    failed.pop(k, None)
                    counts["ok"] += 1
                else:
                    failed[k] = problem
                    counts["miss" if problem.startswith("aucune") else "err"] += 1
                if n % 50 == 0:
                    save(MANIFEST, manifest)
                    save(FAILED, failed)
                    print("  %d/%d  ok=%d absentes=%d erreurs=%d"
                          % (n, len(todo), counts["ok"], counts["miss"], counts["err"]), flush=True)

    ok, miss, err = counts["ok"], counts["miss"], counts["err"]
    save(MANIFEST, manifest)
    save(FAILED, failed)
    print("TERMINE  rapatriees=%d absentes=%d erreurs=%d  total manifest=%d"
          % (ok, miss, err, len(manifest)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
