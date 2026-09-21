import rss from "@astrojs/rss";
import type { APIContext } from "astro";
import { getPosts } from "../lib/posts";
import { SITE } from "../lib/site";

export async function GET(context: APIContext) {
  const posts = (await getPosts()).slice(0, 50);
  return rss({
    title: SITE.title,
    description: SITE.description,
    site: context.site ?? SITE.url,
    customData: `<language>fr-FR</language>`,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      link: post.href,
      pubDate: post.data.date,
      categories: post.data.categories,
    })),
  });
}
