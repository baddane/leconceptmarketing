import type { APIContext } from "astro";
import { getAll, getPosts } from "../lib/posts";
import { absolute, escapeXml, xml } from "../lib/xml";

/** Index des sitemaps, decoupe par type de contenu comme sur le site d'origine. */
export async function GET({ site }: APIContext) {
  const [all, posts] = await Promise.all([getAll(), getPosts()]);
  const newest = (items: typeof all) =>
    items.reduce<Date | undefined>((latest, item) => {
      const date = item.data.modified ?? item.data.date;
      return date && (!latest || date > latest) ? date : latest;
    }, undefined);

  const sitemaps = [
    { loc: "/post-sitemap.xml", lastmod: newest(posts) },
    { loc: "/page-sitemap.xml", lastmod: newest(all.filter((i) => i.data.type === "page")) },
    { loc: "/category-sitemap.xml", lastmod: newest(posts) },
  ];

  const body = sitemaps
    .map(
      (entry) =>
        `<sitemap><loc>${escapeXml(absolute(entry.loc, site))}</loc>` +
        (entry.lastmod ? `<lastmod>${entry.lastmod.toISOString()}</lastmod>` : "") +
        `</sitemap>`
    )
    .join("");

  return xml(`<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${body}</sitemapindex>`);
}
