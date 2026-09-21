import type { APIContext } from "astro";
import { getPosts } from "../lib/posts";
import { absolute, urlset } from "../lib/xml";

export async function GET({ site }: APIContext) {
  const posts = await getPosts();
  return urlset(
    posts.map((post) => ({
      loc: absolute(post.href, site),
      lastmod: post.data.modified ?? post.data.date,
    }))
  );
}
