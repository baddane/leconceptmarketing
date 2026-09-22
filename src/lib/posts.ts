import { getCollection, type CollectionEntry } from "astro:content";
import { permalinkSlug, readingTime, slugify } from "./site";
import { resolveImage } from "./images.mjs";

const BODY_IMAGE = /!\[[^\]]*\]\((https?:\/\/[^)\s]+)\)/g;

// Une image qui revient dans plusieurs articles est un encart maison ou une
// banniere d'affiliation, pas l'illustration de l'article: elle ne doit jamais
// servir de vignette, meme si c'est la seule image disponible.
const SHARED_IMAGE_THRESHOLD = 3;

function bodyImages(entry: CollectionEntry<"blog">): string[] {
  return [...(entry.body ?? "").matchAll(BODY_IMAGE)].map((match) => match[1]);
}

function countImageUse(entries: CollectionEntry<"blog">[]): Map<string, number> {
  const counts = new Map<string, number>();
  for (const entry of entries) {
    const urls = new Set(bodyImages(entry));
    if (entry.data.cover) urls.add(entry.data.cover);
    for (const url of urls) counts.set(url, (counts.get(url) ?? 0) + 1);
  }
  return counts;
}

/**
 * Vignette de l'article : sa couverture, sinon la premiere illustration du
 * corps qui lui soit propre. Renvoie null quand rien n'est servable, la carte
 * compose alors sa couverture a partir du titre.
 */
function thumbnail(entry: CollectionEntry<"blog">, counts: Map<string, number>): string | null {
  for (const url of [entry.data.cover, ...bodyImages(entry)]) {
    if (!url || (counts.get(url) ?? 0) >= SHARED_IMAGE_THRESHOLD) continue;
    const resolved: string | null = resolveImage(url);
    if (resolved) return resolved;
  }
  return null;
}

export interface Post {
  slug: string;
  href: string;
  entry: CollectionEntry<"blog">;
  data: CollectionEntry<"blog">["data"];
  minutes: number;
  image: string | null;
}

function toItem(entry: CollectionEntry<"blog">, counts: Map<string, number>): Post {
  const slug = permalinkSlug(entry.data.permalink, entry.id);
  return {
    slug,
    href: `/${slug}/`,
    entry,
    data: entry.data,
    minutes: readingTime(entry.body ?? ""),
    image: thumbnail(entry, counts),
  };
}

let cache: Post[] | null = null;

/** Toutes les entrees du site, articles et pages confondus. */
export async function getAll(): Promise<Post[]> {
  if (!cache) {
    const entries = await getCollection("blog");
    const counts = countImageUse(entries);
    const seen = new Set<string>();
    cache = entries
      .map((entry) => toItem(entry, counts))
      // Deux captures peuvent partager un permalien : on garde la premiere.
      .filter((item) => !seen.has(item.slug) && seen.add(item.slug));
  }
  return cache;
}

/** Articles datés, du plus recent au plus ancien. */
export async function getPosts(): Promise<Post[]> {
  const all = await getAll();
  return all
    .filter((i) => i.data.type === "post")
    .sort((a, b) => (b.data.date?.getTime() ?? 0) - (a.data.date?.getTime() ?? 0));
}

export interface CategoryInfo { name: string; slug: string; count: number }

export async function getCategories(): Promise<CategoryInfo[]> {
  const posts = await getPosts();
  const byName = new Map<string, number>();
  for (const post of posts) {
    for (const name of post.data.categories) {
      byName.set(name, (byName.get(name) ?? 0) + 1);
    }
  }
  return [...byName.entries()]
    .map(([name, count]) => ({ name, slug: slugify(name), count }))
    .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name, "fr"));
}

export async function getTags(): Promise<CategoryInfo[]> {
  const posts = await getPosts();
  const byName = new Map<string, number>();
  for (const post of posts) {
    for (const name of post.data.tags) byName.set(name, (byName.get(name) ?? 0) + 1);
  }
  return [...byName.entries()]
    .map(([name, count]) => ({ name, slug: slugify(name), count }))
    .sort((a, b) => b.count - a.count || a.name.localeCompare(b.name, "fr"));
}
