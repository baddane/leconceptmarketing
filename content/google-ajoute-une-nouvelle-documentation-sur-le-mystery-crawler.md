---
title: "Google ajoute une nouvelle documentation sur le Mystery Crawler"
permalink: "/google-ajoute-une-nouvelle-documentation-sur-le-mystery-crawler/"
legacy_permalinks: []
type: "post"
date: "2023-12-04T09:57:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["SEO"]
tags: ["Google","le Mystery Crawler"]
description: "Google a mis à jour la liste de ses crawlers officiels en y ajoutant le nom et les informations d'un crawler relativement inconnu que les éditeurs"
cover: ""
source_url: "https://leconceptmarketing.com/google-ajoute-une-nouvelle-documentation-sur-le-mystery-crawler/"
source_capture: "20240221141450"
---
Google a mis à jour la liste de ses crawlers officiels en y ajoutant le nom et les informations d’un crawler relativement inconnu que les éditeurs voient de temps en temps mais pour lequel aucune documentation n’existait auparavant.

Bien que Google ait ajouté une documentation officielle pour ce crawler, les informations fournies semblent encourager une plus grande clarification.

## Crawlers spéciaux :

**[Google dispose de plusieurs types de robots d’indexation](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers?hl=fr)** (également appelés “bots” et “spiders”).

### Les différentes formes de robots sont les suivantes :

#### 1. Crawlers communs :

Ces robots sont principalement utilisés pour indexer différents types de contenu. Mais certains crawlers communs sont également utilisés pour les outils de test de recherche, pour l’usage interne de l’équipe produit de Google et pour l’exploration liée à l’intelligence artificielle.

#### 2. Extracteurs déclenchés par l’utilisateur :

Il s’agit de robots déclenchés par les utilisateurs. Ils sont notamment utilisés pour récupérer des flux ou vérifier des sites.

#### 3. Crawlers spéciaux :

Ils sont utilisés dans des cas particuliers, par exemple pour les contrôles de qualité des pages web d’annonces mobiles ou pour les messages de notification push via les API de Google. Ces robots n’obéissent pas aux directives globales relatives à l’agent utilisateur dans le fichier robots.txt, qui sont signalées par l’astérisque (\*).

La nouvelle documentation sur les robots d’exploration concerne l’agent utilisateur Google-Safety. Le crawler n’est pas nouveau, mais la documentation l’est.

## Crawler Google-Safety :

La documentation du crawler Google-Safety de Special-case Crawlers est utilisée par les processus de Google pour trouver des logiciels malveillants.

Unique parmi les crawlers spéciaux, le crawler Google-Safety ignore complètement toutes les directives **[robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=fr)**.

**La nouvelle documentation pour le Google-Safety Crawler :**

```
"L'agent utilisateur Google-Safety gère l'exploration spécifique aux abus, telle que la découverte de logiciels malveillants pour les liens affichés publiquement sur les propriétés de Google.
```

**Cet agent utilisateur ignore les règles de robots.txt.”**

**La chaîne complète de l’agent pour le crawler :**

“Google-Safety”
Consultez la nouvelle documentation relative à l’agent utilisateur Google-Safety sur la page Google Search Central consacrée aux robots d’indexation, dans la section consacrée aux robots d’indexation spéciaux.

Vue d’ensemble des robots d’exploration et des agents utilisateurs (fetchers) de Google – Cas particuliers de robots d’exploration

→ 🔥 **D’autres articles qui pourraient vous intéresser** :
