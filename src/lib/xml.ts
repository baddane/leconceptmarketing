import { SITE } from "./site";

export function escapeXml(value: string): string {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

export function absolute(path: string, site?: URL): string {
  return new URL(path, site ?? SITE.url).href;
}

export interface SitemapEntry { loc: string; lastmod?: Date }

export function urlset(entries: SitemapEntry[]): Response {
  const body = entries
    .map(
      (entry) =>
        `<url><loc>${escapeXml(entry.loc)}</loc>` +
        (entry.lastmod ? `<lastmod>${entry.lastmod.toISOString()}</lastmod>` : "") +
        `</url>`
    )
    .join("");
  return xml(
    `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${body}</urlset>`
  );
}

export function xml(inner: string): Response {
  return new Response(`<?xml version="1.0" encoding="UTF-8"?>${inner}`, {
    headers: { "Content-Type": "application/xml; charset=utf-8" },
  });
}
