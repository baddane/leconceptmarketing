---
title: "Qu’est-ce que Google Tag Manager et pourquoi l’utiliser ? La vérité sur le gestionnaire de balises Google."
permalink: "/quest-ce-que-google-tag-manager-et-pourquoi-lutiliser-la-verite-sur-le-gestionnaire-de-balises-google/"
legacy_permalinks: []
type: "post"
date: "2022-01-30T08:00:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Google","Moteurs de recherche","SEO"]
tags: ["dataslayer chrome","google analytics google tag manager","google analytics gtag","google tag","google tag assistant","Google Tag Manager","google tag manager id","google tagmanager","le gestionnaire de balises Google","tag manager google analytics","tagmanager","tagmanager google"]
description: "Si vous n'êtes pas très familier avec Google Tag Manager, vous vous demandez probablement ce que c'est et pourquoi vous devriez l'utiliser"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/01/sss-1.jpg"
source_url: "https://leconceptmarketing.com/quest-ce-que-google-tag-manager-et-pourquoi-lutiliser-la-verite-sur-le-gestionnaire-de-balises-google/"
source_capture: "20220221155027"
---
Si vous n’êtes pas très familier avec Google Tag Manager, vous vous demandez probablement ce que c’est et pourquoi vous devriez l’utiliser. Nous allons répondre aux questions les plus courantes sur Google Tag Manager.

![](https://vividreal.com/wp-content/uploads/2019/04/Google-Tag-Manager.png)

- Qu’est-ce que Google Tag Manager ?
- À quoi sert Google Tag Manager ? Est-il facile à utiliser ?
- En quoi Google Tag Manager est-il différent de Google Analytics ?
- Pourquoi devrais-je utiliser Google Tag Manager ? Quels sont les avantages ?
- Quels sont les inconvénients ?
- Que puis-je suivre dans Google Tag Manager ?

- 1 Qu’est-ce que Google Tag Manager (GTM) ?
- 2 Google Tag Manager est-il facile à utiliser ?
- 3 Découvrons comment fonctionne Google Tag Manager…
  - 3.1 Que sont les balises ?
  - 3.2 Que sont les déclencheurs “Triggers” ?
  - 3.3 Que sont les variables ?
- 4 En quoi Google Tag Manager est-il différent de Google Analytics ?
- 5 Quels sont les avantages de Google Tag Manager ?
- 6 Quels sont les inconvénients ?
  - 6.1 Vous devez avoir des connaissances techniques, même pour la configuration de base.
  - 6.2 C’est un investissement en temps.
  - 6.3 Prenez le temps de résoudre les problèmes.
- 7 Que pouvez-vous suivre dans Google Tag Manager (GTM) ?
- 8 À vous de jouer. Que pensez-vous de Google Tag Manager ?

## Qu’est-ce que Google Tag Manager (GTM) ?

**Google Tag Manager**, est un système de gestion de balises gratuit qui vous permet de gérer et de déployer des balises marketing (extraits de code ou pixels de suivi) sur votre site Web (ou [application mobile](https://leconceptmarketing.com/quest-ce-que-le-marketing-mobile-et-pourquoi-est-il-si-important/)) sans avoir à modifier le code.

![](https://leconceptmarketing.com/wp-content/uploads/2022/01/sss-1-1024x544.jpg)

Voici un exemple très simple du fonctionnement de **[Google Tag Manager](https://support.google.com/tagmanager/answer/6103696?hl=fr)**. Les informations provenant d’une source de données (votre site Web) sont partagées avec une autre source de données ([Google Analytics](https://www.google.com/analytics/web/?hl=fr)) via Google Tag Manager. **GTM** devient très pratique lorsque vous avez beaucoup de balises à gérer, car tout le code est stocké au même endroit.

👉🏼 **Lecture complémentaire :** [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)

## Google Tag Manager est-il facile à utiliser ?

**Selon Google,**

> Google Tag Manager contribue à rendre la gestion des balises simple, facile et fiable en permettant aux spécialistes du marketing et aux webmasters de déployer des balises de site Web en un seul endroit

Ils disent que c’est un outil “**simple**” que n’importe quel spécialiste du marketing peut utiliser sans avoir besoin d’un développeur web.

Je risque de me faire écraser dans la section des commentaires pour avoir dit cela, mais je reste sur mes positions. **Google Tag Manager** n’est pas “facile” à utiliser sans quelques connaissances techniques ou une formation (**cours ou autodidacte**).

Vous devez avoir des connaissances techniques pour comprendre comment configurer les balises, les déclencheurs et les variables. Si vous utilisez des pixels Facebook, vous devez comprendre le fonctionnement des pixels de suivi Facebook.

Si vous souhaitez configurer le suivi des événements dans **Google Tag Manager**, vous devez savoir ce que sont les “**événements**“, comment fonctionne **Google Analytics**, quelles données vous pouvez suivre avec des événements, à quoi ressemblent les rapports dans **Google Analytics** et comment nommer vos catégories, actions et étiquettes.

Bien qu’il soit “facile” de gérer plusieurs étiquettes dans **GTM**, il y a une courbe d’apprentissage. Une fois que vous avez franchi le cap, GTM est assez astucieux quant aux données que vous pouvez suivre.

👉🏼 **Lecture complémentaire :** [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)

## Découvrons comment fonctionne Google Tag Manager…

Google Tag Manager se compose de trois parties principales :

- Les balises “**Tags**” : Des extraits de Javascript ou des pixels de suivi
- Déclencheurs “**Triggers**“: Ils indiquent à Google Tag Manager quand, où et comment lancer une balise.
- Variables : Informations supplémentaires dont GTM peut avoir besoin pour que la balise et le déclencheur fonctionnent.

### Que sont les balises ?

![Que sont les balises ?](https://www.orbitmedia.com/wp-content/uploads/2017/03/Examples-Tags-Google-Tag-Manager.png)

Les balises sont des extraits de code ou des pixels de suivi provenant d’outils tiers. Ces balises indiquent à Google Tag Manager ce qu’il doit faire.

**Voici des exemples d’étiquettes courantes dans Google Tag Manager :**

- Le code de suivi universel de Google Analytics ou le code de suivi GA4
- Code de Remarketing Adwords
- Code de suivi de conversion Adwords
- Code de suivi Heatmap (Hotjar, CrazyEgg, etc…)
- Pixels Facebook
- Scripts HTML personnalisés
- Cookiebot et autres scripts de confidentialité des données GDPR

### Que sont les déclencheurs “**Triggers**” ?

![Que sont les déclencheurs "Triggers" ?](https://www.orbitmedia.com/wp-content/uploads/2017/03/Examples-Triggers-Google-Tag-Manager.png)

Les déclencheurs sont un moyen d’activer l’étiquette que vous avez configurée. Ils indiquent à Tag Manager quand, où et comment faire ce que vous voulez qu’il fasse. Vous voulez déclencher une étiquette à la vue d’une page, au clic sur un lien ou à une action personnalisée ?

**Voici des exemples de déclencheurs courants dans Google Tag Manager :**

- Pages vues
- Clics sur des liens
- Soumissions de formulaires
- Profondeur de défilement
- Événements personnalisés

### Que sont les variables ?

Les variables sont des informations supplémentaires dont GTM peut avoir besoin pour que votre balise et votre déclencheur fonctionnent. Voici quelques exemples de différentes variables.

Le type de variable le plus basique que vous pouvez créer dans GTM est le numéro UA de Google Analytics (le numéro d’identification de suivi).

Ce sont les éléments de base de GTM que vous devez connaître pour commencer à gérer les balises par vous-même.

Si vous vous ennuyez en lisant ceci, vous n’aurez aucun [problème à gérer vos balises](https://support.google.com/google-ads/answer/7287822?hl=fr#:~:text=Dans%20votre%20compte%20Google%20Ads,d'%C3%A9v%C3%A9nement%20sont%20correctement%20configur%C3%A9s.&text=en%20haut%20%C3%A0%20droite%20de,%2C%20s%C3%A9lectionnez%20Sources%20d'audience.). Si vous êtes complètement perdu, vous aurez besoin de l’aide de quelqu’un de plus technique.

👉🏼 **Lecture complémentaire :** [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)

## En quoi Google Tag Manager est-il différent de Google Analytics ?

Google Tag Manager est un outil complètement différent, utilisé uniquement pour le stockage et la gestion du code tiers. Il n’existe pas de rapports ni de moyens d’effectuer des analyses dans GTM.

![En quoi Google Tag Manager est-il différent de Google Analytics ?](https://user-images.githubusercontent.com/52087100/84321347-55e11c80-ab49-11ea-9445-24eec6a07785.png)

[Source : GitHub](https://github.com/vtex-apps/google-tag-manager)

Google Analytics est utilisé pour les rapports et les analyses proprement dits. Tous les objectifs ou filtres de suivi des conversions sont gérés par Analytics.

Tous les rapports (rapports de conversion, segments personnalisés, [ventes de commerce électronique](https://leconceptmarketing.com/quest-ce-que-shopify-et-comment-lutiliser-en-2022/), temps passé sur la page, rapports d’engagement, etc…) sont réalisés dans Google Analytics.

![What Is Google Analytics? Definition and Benefits | Indeed.com](https://d4y70tum9c2ak.cloudfront.net/contentImage/rlyWivNOLERwSWwmUSg3wr6b5m55rjbp-ettNgXem7g/resized.png)

## Quels sont les avantages de Google Tag Manager ?

Une fois que vous avez surmonté la courbe d’apprentissage, ce que vous pouvez faire dans Google Tag Manager est assez étonnant. Vous pouvez personnaliser les données qui sont envoyées à Analytics.

Vous pouvez configurer et suivre des événements de base comme les téléchargements de PDF, les clics de liens sortants ou les clics de boutons. Ou encore, un suivi complexe et amélioré des produits de commerce électronique et des promotions.

## Quels sont les inconvénients ?

### Vous devez avoir des connaissances techniques, même pour la configuration de base.

Consultez la documentation de Google sur la façon de configurer Google Tag Manager. Une fois que vous avez dépassé le “Guide de démarrage rapide”, vous accédez à un guide du développeur. Ce n’est pas un guide pour les spécialistes du marketing. Si vous êtes un utilisateur novice, vous aurez l’impression de lire du charabia.

### C’est un investissement en temps.

À moins que vous ne soyez un développeur chevronné, vous devrez consacrer une partie de votre temps à la recherche et aux tests. Même s’il s’agit de lire quelques articles de [blog ](https://leconceptmarketing.com/comment-creer-un-blog-et-vivre-de-son-blog-a-partir-de-zero-guide-ultime/)ou de suivre un cours en ligne.

### Prenez le temps de résoudre les problèmes.

La mise en place de balises, de déclencheurs et de variables implique de nombreux dépannages. Surtout si vous n’utilisez pas régulièrement Tag Manager, il est très facile d’oublier ce que vous venez d’apprendre. Pour les balises plus complexes, vous aurez probablement besoin d’un développeur qui sait comment [le site Web](https://leconceptmarketing.com/comment-creer-un-site-web-etape-par-etape-pour-les-debutants/) a été construit.

## Que pouvez-vous suivre dans Google Tag Manager (GTM) ?

- Événements (clics sur des liens, téléchargements de PDF, clics pour ajouter au panier, clics pour retirer du panier)
- Suivi du défilement
- Abandon de formulaire
- Abandon du panier d’achat
- Suivi des vues de vidéos
- Tous les clics sur les liens de sortie

👉🏼 **Lecture complémentaire :** [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)

## À vous de jouer. Que pensez-vous de Google Tag Manager ?

**Google Tag Manager** peut certainement vous faciliter la vie si vous êtes prêt à apprendre comment il fonctionne. Assurez-vous que vous utilisez réellement les données que vous configurez dans GTM. Sinon, à quoi bon ?

Je suis curieux de connaître votre expérience avec Google Tag Manager. A-t-elle été facile ou difficile ? Comment l’utilisez-vous dans votre marketing ?

**À Lire Aussi :**
