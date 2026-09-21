import type { APIContext } from "astro";
import { getAll } from "../lib/posts";
import { absolute, urlset } from "../lib/xml";

const STATIC_PAGES = ["/", "/sitemap/", "/nous-contacter/"];

export async function GET({ site }: APIContext) {
  const pages = (await getAll()).filter((item) => item.data.type === "page");
  return urlset([
    ...STATIC_PAGES.map((path) => ({ loc: absolute(path, site) })),
    ...pages.map((page) => ({
      loc: absolute(page.href, site),
      lastmod: page.data.modified ?? page.data.date,
    })),
  ]);
}
