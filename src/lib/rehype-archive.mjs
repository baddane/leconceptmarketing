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

function placeholder(alt) {
  const label = alt && alt.trim() ? alt.trim() : "Illustration non archivée";
  return {
    type: "element",
    tagName: "span",
    properties: { className: ["archive-image", "archive-image--missing"], role: "img", "aria-label": label },
    children: [
      { type: "element", tagName: "span", properties: { className: ["archive-image__icon"], "aria-hidden": "true" }, children: [{ type: "text", value: "▨" }] },
      { type: "element", tagName: "span", properties: { className: ["archive-image__label"] }, children: [{ type: "text", value: label }] },
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
  node.properties.className = ["archive-image__img"];
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
    node.properties.rel = "nofollow noopener noreferrer";
  }
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
      walk(next);
    }
    out.push(next);
  }
  node.children = out;
}

/** Recable images et liens internes des articles archives. */
export default function rehypeArchive() {
  return (tree) => walk(tree);
}
