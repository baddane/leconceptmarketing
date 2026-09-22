import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const blog = defineCollection({
  // content/ est regenere depuis dump/ par tools/extract.py, qui efface tout
  // fichier n'en provenant pas. Les articles ecrits pour le site vivent donc
  // dans articles/, que les outils ne touchent jamais.
  loader: glob({ pattern: ["content/*.md", "articles/*.md"], base: "." }),
  schema: z.object({
    title: z.string(),
    permalink: z.string(),
    legacy_permalinks: z.array(z.string()).default([]),
    type: z.enum(["post", "page"]).default("post"),
    date: z.coerce.date().optional().catch(undefined),
    modified: z.coerce.date().optional().catch(undefined),
    author: z.string().default(""),
    categories: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    description: z.string().default(""),
    cover: z.string().default(""),
    source_url: z.string().default(""),
    source_capture: z.string().default(""),
  }),
});

export const collections = { blog };
