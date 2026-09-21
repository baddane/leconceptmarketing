export const SITE = {
  title: "Le Concept Marketing",
  tagline: "Le web pour tous !",
  description:
    "Archive éditoriale du Concept Marketing : plus de 1 100 articles sur le marketing digital, le SEO, les réseaux sociaux, la crypto, l'IA et le e-commerce.",
  url: "https://leconceptmarketing.com",
  lang: "fr",
  locale: "fr_FR",
  postsPerPage: 24,
} as const;

/** Slug WordPress d'un libellé de catégorie (accents retirés, apostrophes absorbées). */
export function slugify(value: string): string {
  return value
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/['‘’“”"]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

/** Dernier segment d'un permalien WordPress : "/mon-article/" -> "mon-article". */
export function permalinkSlug(permalink: string, fallback: string): string {
  const parts = permalink.split("/").filter(Boolean);
  return parts.length ? parts[parts.length - 1] : fallback;
}

export function formatDate(value: Date | undefined): string {
  if (!value) return "";
  return new Intl.DateTimeFormat("fr-FR", {
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  }).format(value);
}

/** Estimation de temps de lecture, base 220 mots/minute. */
export function readingTime(body: string): number {
  return Math.max(1, Math.round(body.trim().split(/\s+/).length / 220));
}
