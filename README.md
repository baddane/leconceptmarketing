# Le Concept Marketing

Blog statique [Astro](https://astro.build) : marketing digital, SEO, réseaux
sociaux, e-commerce, crypto et IA. 1 110 articles répartis dans 38 rubriques.

Le contenu provient du WordPress d'origine, qui avait perdu ses publications et
sa médiathèque ; il est reconstitué à partir des captures publiques du site et
régénérable à tout moment via `tools/`.

## Démarrer

```bash
npm install
npm run dev          # http://localhost:4321
npm run build        # génère dist/
npm run preview
```

Node 18+ et Python 3.9+ (pour les outils de contenu uniquement).

## Déploiement Vercel

Le projet est détecté automatiquement comme un site Astro : `astro build`,
sortie dans `dist/`, aucune variable d'environnement requise.

`vercel.json` est **généré** par `tools/extract.py` et contient :

- les redirections 301 des anciens permaliens (URL préfixées d'un caractère
  décoratif, liens courts `?p=1234`) vers les permaliens canoniques ;
- les en-têtes de cache long pour `/images/` et `/_astro/` ;
- `trailingSlash: true`, cohérent avec la sortie en répertoires d'Astro.

Ne l'éditez pas à la main : modifiez `write_vercel_config()` puis relancez
l'extraction.

## Organisation

| Chemin | Rôle |
| --- | --- |
| `dump/` | Captures HTML brutes du site d'origine. **Source de vérité**, jamais éditée, exclue du déploiement. |
| `content/` | Markdown généré depuis `dump/`. Une page par fichier, frontmatter YAML. |
| `public/images/` | Illustrations rapatriées + `manifest.json` (table URL d'origine → fichier local). |
| `src/` | Le site Astro. |
| `tools/` | Scripts de reconstruction du contenu. |
| `manifest.csv` | Journal du téléchargement Wayback (URL, horodatage, fichier). |

## Chaîne de reconstruction

### 1. Contenu — `python3 tools/extract.py`

Reconstruit `content/` **intégralement** depuis `dump/` et réécrit `vercel.json`.
L'opération est idempotente : relancez-la après toute modification des règles
d'extraction.

Ce que fait le script :

- décompresse les captures servies en gzip brut (sinon illisibles) ;
- isole le corps de l'article selon le gabarit rencontré (`td-post-content`,
  `td-page-content`, variante AMP, pages WPBakery) ;
- retire publicités, sommaires automatiques, encadrés auteur, blocs de partage
  et formulaires de commentaire ;
- extrait titre, permalien, date UTC, auteur, catégories et mots-clés depuis le
  balisage schema.org et le thème ;
- normalise les permaliens en ASCII et note les anciens dans
  `legacy_permalinks` pour générer les redirections.

Sont ignorés : archives de catégories et d'auteurs (le site les regénère),
doublons AMP, et les pages sans corps de texte exploitable.

### 2. Liens partenaires — `python3 tools/partner_links.py`

`content/` étant régénéré depuis `dump/`, un lien ajouté à la main y serait
effacé. Ce script rejoue les insertions décrites dans
`tools/partner_links.json`, juste après l'extraction — d'où le `&&` dans
`npm run content:extract`.

Chaque insertion transforme **une expression déjà écrite par l'auteur** en lien :
rien n'est ajouté à l'article. Les règles tenues dans la configuration :

- un seul lien par article, et seulement là où le sujet de l'article recoupe
  réellement celui du site cible ;
- une ancre différente à chaque fois — répéter la même expression exacte d'un
  article à l'autre est ce que Google traite comme un schéma de liens ;
- l'ancre est vérifiée dans le texte : `--check` signale toute entrée dont
  l'expression n'existe pas, plutôt que d'inventer une phrase.

Le script est idempotent : relancez-le, il ne double jamais un lien.

### 3. Images — `python3 tools/fetch_images.py`

Les URL `wp-content` d'origine renvoient toutes 404. Le script retrouve chaque
image dans l'Internet Archive, la stocke dans `public/images/` et met à jour
`manifest.json`.

```bash
python3 tools/fetch_images.py --dry-run     # ce qui reste à faire
python3 tools/fetch_images.py               # rapatriement (reprenable)
python3 tools/fetch_images.py --retry-failed
```

Le script est **reprenable** : il ne retélécharge jamais une image déjà
présente, met en cache l'index CDX dossier par dossier et consigne les échecs
dans `.failed.json`. L'Internet Archive étant fréquemment saturée, plusieurs
passes sont normales.

Tant qu'une image n'est pas rapatriée, le site affiche un emplacement neutre à
sa place plutôt qu'un lien mort, et les vignettes de cartes retombent sur un
dégradé déterministe. **Relancez `npm run build` après un rapatriement** pour
que les images apparaissent.

## Choix de rendu

- **Permaliens d'origine conservés**, pour préserver liens entrants et
  référencement ; les anciennes formes d'URL sont redirigées en 301.
- **Menu et pied de page repris de l'arborescence d'origine** : rubriques de
  tête et sous-rubriques identiques.
- **Sitemaps découpés par type** comme sur le site d'origine :
  `/sitemap_index.xml` pointe vers `post-sitemap.xml`, `page-sitemap.xml` et
  `category-sitemap.xml`, chacun avec `lastmod`. Une version lisible est servie
  à `/sitemap/`.
- **Liens sortants qualifiés** : un lien éditorial reste suivi, un lien
  d'affiliation reçoit `rel="sponsored nofollow"` (réseaux et paramètres de
  tracking détectés dans `src/lib/rehype-content.mjs`).
- **Données structurées** : `BlogPosting`, `BreadcrumbList` sur les articles,
  `WebSite` + `SearchAction` sur l'accueil.
- **Liens internes recâblés au build** (`src/lib/rehype-content.mjs`) : un lien
  vers une page archivée devient relatif, un lien vers une page jamais capturée
  est dégradé en texte plutôt que laissé mort. Les liens externes reçoivent
  `rel="nofollow noopener noreferrer"`.
- **Titres du corps rétrogradés** : le titre de la page est le seul `<h1>`.
- **Aucun JavaScript côté client** en dehors de la page de recherche, qui filtre
  un index JSON servi à `/search.json`.

> Astro met en cache le rendu Markdown. Après une modification de
> `src/lib/rehype-content.mjs`, supprimez `.astro/` avant de rebuilder, sinon
> les pages sont resservies telles quelles.
