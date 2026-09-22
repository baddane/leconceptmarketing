#!/usr/bin/env python3
"""Insere les liens vers les sites partenaires dans les articles concernes.

content/ est regenere depuis dump/ : un lien ajoute a la main y serait efface
a la prochaine extraction. Ce script rejoue les insertions a partir de
tools/partner_links.json, apres extract.py.

Chaque insertion transforme une expression deja presente dans le texte en lien.
Rien n'est ajoute a l'article : l'ancre est une formulation de l'auteur, sur un
sujet que le site cible traite reellement.

Le script est idempotent : relancez-le, il ne double jamais un lien.

Usage:
  python3 tools/partner_links.py            # applique
  python3 tools/partner_links.py --check    # verifie sans ecrire
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(HERE, "content")
CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "partner_links.json")


def split_front_matter(text):
    parts = text.split("---", 2)
    return (parts[1], parts[2]) if len(parts) >= 3 else ("", text)


# Le drapeau DOTALL ne vaut que pour les blocs delimites : applique aux autres
# motifs, un « . » avalant les sauts de ligne protegerait tout le reste du texte.
PROTECTED = [
    (r"!?\[[^\]]*\]\([^)]*\)", 0),  # liens et images deja poses
    (r"```.*?```", re.S),           # blocs de code
    (r"`[^`\n]*`", 0),              # code en ligne
]


def protected_spans(body):
    """Zones ou une ancre ne doit pas etre posee : liens, images, code."""
    spans = []
    for rx, flags in PROTECTED:
        for m in re.finditer(rx, body, flags):
            spans.append((m.start(), m.end()))
    return spans


def find_anchor(body, anchor):
    """Premiere occurrence de l'ancre hors zone protegee, sinon None."""
    spans = protected_spans(body)
    for m in re.finditer(re.escape(anchor), body):
        if not any(start <= m.start() < end for start, end in spans):
            return m
    return None


def apply(entry, check=False):
    path = os.path.join(CONTENT, entry["slug"] + ".md")
    if not os.path.exists(path):
        return "article introuvable", None

    text = open(path, encoding="utf-8").read()
    front, body = split_front_matter(text)
    if entry["url"] in body:
        return "deja pose", None

    for anchor in entry["anchors"]:
        match = find_anchor(body, anchor)
        if not match:
            continue
        if not check:
            body = body[:match.start()] + "[%s](%s)" % (anchor, entry["url"]) + body[match.end():]
            open(path, "w", encoding="utf-8").write("---".join(["", front, body]))
        return "pose", anchor
    return "aucune ancre trouvee", None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    config = json.load(open(CONFIG, encoding="utf-8"))
    counts, failures = {}, []
    by_site = {}
    for entry in config["links"]:
        status, anchor = apply(entry, args.check)
        counts[status] = counts.get(status, 0) + 1
        if status in ("pose", "deja pose"):
            by_site.setdefault(entry["url"], []).append((entry["slug"], anchor))
        else:
            failures.append((entry["slug"], status))

    for status, n in sorted(counts.items()):
        print("  %-22s %d" % (status, n))
    for url, items in sorted(by_site.items()):
        print("\n%s : %d liens" % (url, len(items)))
        for slug, anchor in items:
            print("   %-58s %s" % (slug[:58], anchor or ""))
    if failures:
        print("\nA revoir :")
        for slug, why in failures:
            print("   %-58s %s" % (slug[:58], why))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
