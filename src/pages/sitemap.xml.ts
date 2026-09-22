import type { APIContext } from "astro";
import { sitemapIndex } from "../lib/sitemap";

export const GET = (context: APIContext) => sitemapIndex(context);
