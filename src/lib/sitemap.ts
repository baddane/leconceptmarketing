import type { APIContext } from "astro";
import { getAll, getPosts } from "./posts";
import { absolute, escapeXml, xml } from "./xml";

const SITEMAPS = ["/post-sitemap.xml", "/page-sitemap.xml", "/category-sitemap.xml"];

/**
 * Index des sitemaps, decoupe par type de contenu comme sur le site d'origine.
 * Servi a la fois sur /sitemap.xml, que les outils testent par defaut, et sur
 * /sitemap_index.xml, l'adresse historique du site.
 */
export async function sitemapIndex({ site }: APIContext): Promise<Response> {
  const [all, posts] = await Promise.all([getAll(), getPosts()]);
  const newest = (items: typeof all) =>
    items.reduce<Date | undefined>((latest, item) => {
      const date = item.data.modified ?? item.data.date;
      return date && (!latest || date > latest) ? date : latest;
    }, undefined);

  const lastmod: Record<string, Date | undefined> = {
    "/post-sitemap.xml": newest(posts),
    "/page-sitemap.xml": newest(all.filter((i) => i.data.type === "page")),
    "/category-sitemap.xml": newest(posts),
  };

  const body = SITEMAPS.map(
    (path) =>
      `<sitemap><loc>${escapeXml(absolute(path, site))}</loc>` +
      (lastmod[path] ? `<lastmod>${lastmod[path]!.toISOString()}</lastmod>` : "") +
      `</sitemap>`
  ).join("");

  return xml(`<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${body}</sitemapindex>`);
}
