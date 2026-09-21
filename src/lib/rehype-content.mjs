import fs from "node:fs";
import path from "node:path";
import { resolveImage } from "./images.mjs";

const CONTENT_DIR = path.join(process.cwd(), "content");

/** Permaliens presents dans l'archive : sert a distinguer lien interne vivant et lien mort. */
function knownSlugs() {
  const slugs = new Set();
  let files = [];
  try {
    files = fs.readdirSync(CONTENT_DIR).filter((f) => f.endsWith(".md"));
  } catch {
    return slugs;
  }
  for (const file of files) {
    const head = fs.readFileSync(path.join(CONTENT_DIR, file), "utf8").slice(0, 2048);
    const match = head.match(/^permalink: "(.*)"$/m);
    const permalink = match ? match[1] : `/${file.slice(0, -3)}/`;
    const parts = permalink.split("/").filter(Boolean);
    if (parts.length) slugs.add(parts[parts.length - 1]);
  }
  return slugs;
}

const SLUGS = knownSlugs();
const INTERNAL = /^https?:\/\/(www\.)?leconceptmarketing\.com(\/.*)?$/i;

// Reseaux d'affiliation et parametres de tracking rencontres dans les articles.
// Ces liens sont remuneres : Google demande rel="sponsored".
const AFFILIATE_HOSTS =
  /(^|\.)(amzn\.to|tidd\.ly|envato\.market|pxf\.io|sjv\.io|prf\.hn|go2cloud\.org|shareasale\.com|awin1\.com|clickbank\.net|1tpe\.net|digistore24\.com|jvzoo\.com|warriorplus\.com|gumroad\.com|do\.co)$/i;
const AFFILIATE_SUBDOMAIN = /^(partners?|affiliates?|go|track|click)\./i;
const AFFILIATE_QUERY =
  /[?&](tag|aff|aff_id|affiliate|ref|refcode|referral|partner|irclickid|a_aid|sscid|utm_medium=affiliate)=/i;
const AFFILIATE_PATH = /\/(aff|affiliate|partners?|recommends|go)\//i;

function isSponsored(url) {
  try {
    const parsed = new URL(url);
    return (
      AFFILIATE_HOSTS.test(parsed.hostname) ||
      AFFILIATE_SUBDOMAIN.test(parsed.hostname) ||
      AFFILIATE_QUERY.test(parsed.search) ||
      AFFILIATE_PATH.test(parsed.pathname)
    );
  } catch {
    return false;
  }
}

function placeholder(alt) {
  const label = alt && alt.trim() ? alt.trim() : "Image indisponible";
  return {
    type: "element",
    tagName: "span",
    properties: { className: ["media", "media--missing"], role: "img", "aria-label": label },
    children: [
      { type: "element", tagName: "span", properties: { className: ["media__icon"], "aria-hidden": "true" }, children: [{ type: "text", value: "▨" }] },
      { type: "element", tagName: "span", properties: { className: ["media__label"] }, children: [{ type: "text", value: label }] },
    ],
  };
}

function handleImage(node) {
  const src = node.properties?.src;
  const resolved = resolveImage(src);
  if (!resolved) return placeholder(node.properties?.alt);
  node.properties.src = resolved;
  node.properties.loading = "lazy";
  node.properties.decoding = "async";
  node.properties.className = ["media__img"];
  return node;
}

function handleLink(node) {
  const href = node.properties?.href;
  if (typeof href !== "string") return node;

  if (INTERNAL.test(href)) {
    const url = new URL(href);
    if (url.pathname.startsWith("/wp-content/")) {
      // Lien vers un media disparu : on ne garde que le texte.
      return { type: "element", tagName: "span", properties: {}, children: node.children };
    }
    const parts = url.pathname.split("/").filter(Boolean);
    const slug = parts[parts.length - 1];
    if (slug && SLUGS.has(slug)) {
      node.properties.href = `/${slug}/`;
      return node;
    }
    if (url.pathname === "/" || !slug) {
      node.properties.href = "/";
      return node;
    }
    // Article jamais archive : le lien serait mort, on degrade en texte.
    return { type: "element", tagName: "span", properties: { className: ["dead-link"] }, children: node.children };
  }

  if (/^https?:\/\//i.test(href)) {
    node.properties.target = "_blank";
    // Un lien editorial reste suivi : c'est le maillage sortant naturel que
    // Google attend. Seuls les liens remuneres sont marques sponsored.
    node.properties.rel = isSponsored(href)
      ? "sponsored nofollow noopener noreferrer"
      : "noopener noreferrer";
  }
  return node;
}

// Le titre de la page est deja un <h1>: ceux qui viennent du corps de
// l'article d'origine sont retrogrades pour garder une hierarchie valide.
function demoteHeading(node) {
  if (node.tagName === "h1") node.tagName = "h2";
  return node;
}

function walk(node) {
  if (!node.children) return;
  const out = [];
  for (const child of node.children) {
    let next = child;
    if (child.type === "element") {
      if (child.tagName === "img") next = handleImage(child);
      else if (child.tagName === "a") next = handleLink(child);
      else if (child.tagName === "h1") next = demoteHeading(child);
      walk(next);
    }
    out.push(next);
  }
  node.children = out;
}

/** Recable images, liens internes et attributs rel des articles. */
export default function rehypeContent() {
  return (tree) => walk(tree);
}
