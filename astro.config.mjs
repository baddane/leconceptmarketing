import { defineConfig } from "astro/config";
import rehypeContent from "./src/lib/rehype-content.mjs";

export default defineConfig({
  site: "https://leconceptmarketing.com",
  trailingSlash: "always",
  build: { format: "directory" },
  markdown: {
    rehypePlugins: [rehypeContent],
    shikiConfig: { theme: "github-dark", wrap: true },
  },
});
