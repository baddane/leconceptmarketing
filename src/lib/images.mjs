import fs from "node:fs";
import path from "node:path";

const ROOT = process.cwd();
const MANIFEST = path.join(ROOT, "public", "images", "manifest.json");

/**
 * Table URL d'origine -> fichier local, produite par tools/fetch_images.py.
 * Absente tant que les medias n'ont pas ete rapatries : le site doit alors
 * se rendre sans image plutot que d'afficher des liens morts.
 */
function loadManifest() {
  try {
    return JSON.parse(fs.readFileSync(MANIFEST, "utf8"));
  } catch {
    return {};
  }
}

const manifest = loadManifest();

export const manifestSize = Object.keys(manifest).length;

/** Cle stable : on ignore le protocole et le prefixe CDN Jetpack. */
export function imageKey(url) {
  const bare = String(url)
    .replace(/^https?:\/\//, "")
    .replace(/^i[0-9]\.wp\.com\//, "")
    .split("?")[0];
  try {
    return decodeURIComponent(bare);
  } catch {
    return bare;
  }
}

export function isLostMedia(url) {
  return /^(https?:\/\/)?(i[0-9]\.wp\.com\/)?leconceptmarketing\.com\//.test(String(url));
}

/**
 * Renvoie le chemin local d'une image rapatriee, l'URL d'origine si elle est
 * hebergee ailleurs et donc toujours vivante, ou null si le media est perdu.
 */
export function resolveImage(url) {
  if (!url) return null;
  const local = manifest[imageKey(url)];
  if (local) return `/images/${local}`;
  if (isLostMedia(url)) return null;
  return url;
}
