# Le Concept Marketing — archive statique

Site statique [Astro](https://astro.build) qui restitue le contenu éditorial de
`leconceptmarketing.com`. Le WordPress d'origine a perdu ses publications et sa
médiathèque : ce dépôt reconstruit le site à partir des captures publiques de
l'Internet Archive.

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
| `dump/` | Captures HTML brutes de l'Internet Archive. **Source de vérité**, jamais éditée, exclue du déploiement. |
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

### 2. Images — `python3 tools/fetch_images.py`

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
- **Liens internes recâblés au build** (`src/lib/rehype-archive.mjs`) : un lien
  vers une page archivée devient relatif, un lien vers une page jamais capturée
  est dégradé en texte plutôt que laissé mort. Les liens externes reçoivent
  `rel="nofollow noopener noreferrer"`.
- **Aucun JavaScript côté client** en dehors de la page de recherche, qui filtre
  un index JSON servi à `/search.json`.
