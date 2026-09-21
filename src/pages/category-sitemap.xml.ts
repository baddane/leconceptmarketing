import type { APIContext } from "astro";
import { getCategories, getPosts } from "../lib/posts";
import { absolute, urlset } from "../lib/xml";

export async function GET({ site }: APIContext) {
  const [categories, posts] = await Promise.all([getCategories(), getPosts()]);
  return urlset(
    categories.map((category) => {
      // lastmod = article le plus recent de la rubrique.
      const latest = posts.find((p) => p.data.categories.includes(category.name));
      return {
        loc: absolute(`/category/${category.slug}/`, site),
        lastmod: latest?.data.date,
      };
    })
  );
}
