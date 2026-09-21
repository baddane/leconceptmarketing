import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import rehypeArchive from "./src/lib/rehype-archive.mjs";

export default defineConfig({
  site: "https://leconceptmarketing.com",
  trailingSlash: "always",
  build: { format: "directory" },
  markdown: {
    rehypePlugins: [rehypeArchive],
    shikiConfig: { theme: "github-dark", wrap: true },
  },
  integrations: [sitemap({ filter: (page) => !page.includes("/recherche/") })],
});
