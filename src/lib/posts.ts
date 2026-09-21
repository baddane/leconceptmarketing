import { getCollection, type CollectionEntry } from "astro:content";
import { permalinkSlug, readingTime, slugify } from "./site";

export interface Post {
  slug: string;
  href: string;
  entry: CollectionEntry<"blog">;
  data: CollectionEntry<"blog">["data"];
  minutes: number;
}

function toItem(entry: CollectionEntry<"blog">): Post {
  const slug = permalinkSlug(entry.data.permalink, entry.id);
  return {
    slug,
    href: `/${slug}/`,
    entry,
    data: entry.data,
    minutes: readingTime(entry.body ?? ""),
  };
}

let cache: Post[] | null = null;

/** Toutes les entrees du site, articles et pages confondus. */
export async function getAll(): Promise<Post[]> {
  if (!cache) {
    const entries = await getCollection("blog");
    const seen = new Set<string>();
    cache = entries
      .map(toItem)
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
