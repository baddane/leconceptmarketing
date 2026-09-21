export const SITE = {
  title: "Le Concept Marketing",
  tagline: "Le web pour tous !",
  description:
    "Trouvez dans ce Blog l'actualité du marketing digital, stratégie Digitale, Outils SEO, Marketing de contenu et des conseils référencement.",
  url: "https://leconceptmarketing.com",
  email: "contact@leconceptmarketing.com",
  lang: "fr",
  locale: "fr_FR",
  postsPerPage: 24,
} as const;

/**
 * Menu principal, repris à l'identique de l'arborescence du site :
 * une rubrique de tête par univers, ses sous-rubriques en déroulant.
 */
export const MENU: { label: string; category?: string; children?: { label: string; category: string }[] }[] = [
  { label: "Accueil" },
  {
    label: "Actualité Web",
    category: "Actualité Web",
    children: [
      { label: "Crypto-monnaies", category: "Crypto-monnaies" },
      { label: "Le Journal E-marketing", category: "Le Journal E-marketing" },
      { label: "Meilleur du Web", category: "Meilleur du Web" },
      { label: "Elearning & Marketing", category: "Elearning & Marketing" },
      { label: "Inbound Marketing", category: "Inbound Marketing" },
      { label: "Manga", category: "Manga" },
    ],
  },
  {
    label: "Réseaux sociaux",
    category: "Réseaux sociaux",
    children: [
      { label: "Espace Réseaux Sociaux", category: "Espace Réseaux Sociaux" },
      {
        label: "Top #Hashtags",
        category: "Top #Hashtags en français pour Instagram, Twitter, Facebook…",
      },
    ],
  },
  {
    label: "E-commerce",
    category: "E-commerce",
    children: [
      { label: "WooCommerce", category: "WooCommerce" },
      { label: "Shopify", category: "Shopify" },
    ],
  },
  {
    label: "WordPress",
    category: "WordPress",
    children: [
      { label: "Le Guide", category: "Le Guide" },
      { label: "Thèmes", category: "Thèmes" },
      { label: "Plugins", category: "Plugins" },
    ],
  },
  {
    label: "SEO",
    category: "SEO",
    children: [
      { label: "Google", category: "Google" },
      { label: "Moteurs de recherche", category: "Moteurs de recherche" },
    ],
  },
  {
    label: "Produits & Services",
    category: "Produits & Services",
    children: [
      { label: "L’équipement Digitale", category: "L’équipement Digitale" },
      { label: "Hébergement", category: "Hébergement" },
      { label: "Ressources", category: "Ressources" },
      { label: "Gagner de l’Argent", category: "Gagner de l'Argent" },
      { label: "Affiliation", category: "Affiliation" },
    ],
  },
  { label: "Logiciels de business", category: "Logiciels de business" },
];

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

/** Dernier segment d'un permalien : "/mon-article/" -> "mon-article". */
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
