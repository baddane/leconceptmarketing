#!/usr/bin/env python3
# Recupere le dernier snapshot Wayback (brut) de chaque URL canonique de leconceptmarketing.com
import urllib.request, urllib.parse, os, sys, time, re, csv

DOMAIN = "leconceptmarketing.com"
HERE = os.path.dirname(os.path.abspath(__file__))
DUMP = os.path.join(HERE, "dump")
os.makedirs(DUMP, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) recovery-script"

def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout).read()

def get_inventory():
    cdx = ("http://web.archive.org/cdx/search/cdx?url=" + DOMAIN +
           "*&output=text&fl=original,timestamp&filter=statuscode:200"
           "&filter=mimetype:text/html&collapse=urlkey&limit=20000")
    data = fetch(cdx, 120).decode("utf-8", "replace")
    rows = []
    for line in data.splitlines():
        parts = line.split(" ")
        if len(parts) < 2: continue
        orig, ts = parts[0], parts[1]
        rows.append((orig, ts))
    return rows

def keep(u):
    p = urllib.parse.urlparse(u)
    path, q = p.path.lower(), p.query.lower()
    if any(x in q for x in ("filter_by", "add-to-cart", "replytocom")): return False
    if "/page/" in path: return False
    if path.startswith(("/author/", "/tag/", "/wp-", "/feed")): return False
    if "/feed/" in path: return False
    if path.endswith((".xml",".css",".js",".png",".jpg",".jpeg",".gif",".webp",".ico",".txt",".pdf")): return False
    return True

def slugfile(u):
    p = urllib.parse.urlparse(u).path
    if p in ("", "/"): return "__home__.html"
    s = p.strip("/").replace("/", "__")
    s = urllib.parse.unquote(s)
    s = re.sub(r'[^0-9A-Za-z_\-]', "_", s)
    return (s[:180] or "index") + ".html"

def main():
    print("Recuperation de l'inventaire CDX...", flush=True)
    rows = get_inventory()
    seen = {}
    for orig, ts in rows:
        if keep(orig):
            seen[orig] = ts  # last wins (most recent capture due to collapse)
    urls = sorted(seen.items())
    total = len(urls)
    print("A telecharger:", total, "pages", flush=True)
    manifest = os.path.join(HERE, "manifest.csv")
    done = set()
    if os.path.exists(manifest):
        with open(manifest, encoding="utf-8") as f:
            for r in csv.reader(f):
                if r: done.add(r[0])
    mf = open(manifest, "a", newline="", encoding="utf-8")
    w = csv.writer(mf)
    ok = fail = skip = 0
    for i, (orig, ts) in enumerate(urls, 1):
        fn = slugfile(orig)
        fp = os.path.join(DUMP, fn)
        if orig in done and os.path.exists(fp):
            skip += 1
            continue
        wb = "http://web.archive.org/web/%sid_/%s" % (ts, orig)
        for attempt in range(3):
            try:
                html = fetch(wb, 60)
                with open(fp, "wb") as fo: fo.write(html)
                w.writerow([orig, ts, fn]); mf.flush()
                ok += 1
                break
            except Exception as e:
                if attempt == 2:
                    fail += 1
                    with open(os.path.join(HERE, "errors.log"), "a", encoding="utf-8") as el:
                        el.write("%s\t%s\n" % (orig, e))
                else:
                    time.sleep(2)
        if i % 20 == 0:
            print("  %d/%d  ok=%d fail=%d skip=%d" % (i, total, ok, fail, skip), flush=True)
        time.sleep(0.4)
    mf.close()
    print("TERMINE  ok=%d fail=%d skip=%d  ->  %s" % (ok, fail, skip, DUMP), flush=True)

if __name__ == "__main__":
    main()
