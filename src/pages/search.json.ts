import type { APIRoute } from "astro";
import { getPosts } from "../lib/posts";

/** Index client leger : titre, extrait et categories suffisent au filtrage. */
export const GET: APIRoute = async () => {
  const posts = await getPosts();
  const index = posts.map((p) => ({
    t: p.data.title,
    u: p.href,
    d: p.data.description.slice(0, 160),
    c: p.data.categories,
    y: p.data.date?.getUTCFullYear() ?? null,
  }));
  return new Response(JSON.stringify(index), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
