---
title: "Comment rendre un thème WordPress compatible avec WooCommerce"
permalink: "/comment-rendre-un-theme-wordpress-compatible-avec-woocommerce/"
date: "2021-11-30T18:49:43+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "Vous voulez donc ajouter une boutique à votre thème - génial ! WooCommerce est un excellent choix. Techniquement parlant, TOUS les thèmes sont &quot;compatibles"
cover: "https://leconceptmarketing.com/wp-content/uploads/2021/11/EEEEE.jpeg"
source_capture: "20211202172751"
method: "regex"
---
Accueil  Thémes  Comment rendre un thème WordPress compatible avec  WooCommerce

- Thémes
- Woocommerce

# Comment rendre un thème WordPress compatible avec  WooCommerce

30 novembre 202135
0

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Vous voulez donc ajouter une boutique à votre thème &#8211; génial ! WooCommerce est un excellent choix. Techniquement parlant, TOUS les thèmes sont &#8220;compatibles WooCommerce&#8221; parce que c’est un plugin.
En théorie, tout plugin devrait fonctionner avec n’importe quel thème WordPress (s’il est codé correctement).

Cependant, en tant que développeur de thème, vous pouvez vouloir modifier la sortie de WooCommerce pour mieux l’adapter à votre thème ou pour fournir des options à vos utilisateurs finaux qui ne sont pas facilement disponibles dans les paramètres de WooCommerce (comme modifier le nombre de colonnes de la boutique).
Vous trouverez ci-dessous quelques extraits utiles que vous pouvez utiliser pour fournir un &#8220;meilleur&#8221; support pour WooCommerce dans votre thème et/ou pour modifier des choses pour votre conception spécifique.
Important : La plupart des extraits ci-dessous utilisent des fonctions disponibles uniquement dans WooCommerce. Assurez-vous donc que ces extraits ne sont pas simplement déposés au bas de votre fichier functions.php dans un thème créé pour la distribution. Si vous avez l'intention de partager votre thème avec d'autres ou de le vendre, assurez-vous de placer les extraits dans leur propre fichier qui n'est chargé que lorsque le plugin WooCommerce est actif.Table Des Mati&egrave;res
- 1 Vérifier si WooCommerce est activé :
- 2 Déclarer le support WooCommerce :
- 3 Supprimer les CSS de WooCommerce :
- 4 Activer la galerie de produits, le zoom et la lightbox de WooCommerce (v3.0+) :
- 5 Supprimer le titre de la boutique :
- 6 Modifier le titre des archives pour la boutique :
- 7 Modifier le nombre de produits affichés par page sur la boutique :
- 8 Modifier le nombre de colonnes affichées sur la boutique par ligne :
- 9 Modifier les flèches de pagination suivante et précédente :
- 10 Modifiez le nombre de colonnes par ligne pour les sections relatives et les ventes incitatives des produits :
- 11 Conclusion :

## Vérifier si WooCommerce est activé :
Dans mon thème Divi,le thème WordPress le plus populaire au monde, Complet, facile à utiliser et livré avec plus de 62 templates gratuits. j’aime définir une constante personnalisée qui peut être utilisée pour vérifier si WooCommerce est activé.
De cette façon, je peux inclure des fichiers ou exécuter des fonctions uniquement lorsque WooCommerce est actif (voir le message important ci-dessus si vous ne l’avez pas encore fait).

## Déclarer le support WooCommerce :
C’est le premier et le plus important morceau de code à ajouter à votre thème qui &#8220;active&#8221; le support WooCommerce et empêche les avertissements du plugin indiquant à l’utilisateur final que le thème n’est pas compatible.

## Supprimer les CSS de WooCommerce :
Personnellement, je préfère remplacer les styles de WooCommerce pour éviter tout problème éventuel avec les plugins WooCommerce tiers. Cependant, si vous voulez supprimer tous les styles de WooCommerce, c’est très facile.
Le snippet suivant permet de supprimer TOUS les styles WooCommerce :

Cet extrait est un exemple de suppression conditionnelle de styles CSS spécifiques :

## Activer la galerie de produits, le zoom et la lightbox de WooCommerce (v3.0+) :
Dans WooCommerce 3.0, ils ont introduit une nouvelle galerie de produits, un zoom et une lightbox. Ils doivent tous être activés via &#8220;add_theme_support&#8221; si vous voulez les utiliser dans votre thème.

## Supprimer le titre de la boutique :
Beaucoup de thèmes ont déjà des fonctions pour afficher les titres des archives. Ce code supprime le titre supplémentaire de WooCommerce, ce qui est mieux que de le cacher via CSS.

## Modifier le titre des archives pour la boutique :
Si votre thème utilise les fonctions archive_title() ou get_archive_title() pour afficher le titre de vos archives, vous pouvez facilement le modifier via un filtre pour récupérer le nom de votre page produit à la place du titre de l’archive de la boutique.

## Modifier le nombre de produits affichés par page sur la boutique :
Permet de modifier le nombre de produits affichés par page sur la boutique et les archives de produits (catégories et tags).

## Modifier le nombre de colonnes affichées sur la boutique par ligne :
Je ne comprends pas pourquoi WooCommerce fonctionne de cette façon, mais vous ne pouvez pas simplement modifier le filtre &#8216;loop_shop_columns’, vous devez également ajouter les classes uniques à la balise body pour que les colonnes fonctionnent.
Alors que les Shortcodes Woo ont un div wrapper avec les classes correctes, les pages de la boutique n’en ont pas, c’est pourquoi nous avons besoin de deux fonctions.

## Modifier les flèches de pagination suivante et précédente :
Cet extrait vous permettra de modifier les flèches de pagination de la boutique pour qu’elles correspondent à celles de votre thème.

## Modifiez le nombre de colonnes par ligne pour les sections relatives et les ventes incitatives des produits :
Comme dans le cas de la boutique, si vous souhaitez modifier correctement le nombre de colonnes pour les produits connexes et les ventes incitatives sur les pages de produits individuels, vous devez filtrer les colonnes et modifier les classes de corps en conséquence.

## Conclusion :
WooCommerce fonctionne par défaut avec tous les thèmes, mais il est très facile d’ajouter un support supplémentaire pour le plugin afin qu’il s’adapte mieux à votre thème.
J’ai en fait écrit cet article pendant le codage de notre thème Divi, donc la plupart de ces modifications sont incluses dans notre thème. Si vous préférez, vous pouvez essayer le thème pour voir comment tout a été fait  &#8211; c’est peut-être un moyen plus facile pour vous d’apprendre comment ajouter un support personnalisé pour le plugin WooCommerce en regardant un thème déjà codé.
   À lire Aussi :
- Comment choisir un nom de domaine  idéal pour votre site web
- 15 meilleures alternatives à Google AdSense pour gagner de l’argent
- Comment rendre un thème WordPress compatible avec  WooCommerce
- Comment accepter les paiements via votre site Web WordPress
- Comment créer et gérer une agence du digitale ? Les 8 points à avoir en tête
- Référencement payant : Qu’est-ce que c’est et comment ça marche ?
- Comment gagner de l’argent rapidement sur TikTok en 6 points
- Ads Twitter  : Un guide en 6 étapes pour utiliser la publicité Twitter
- 9 façons pour faire connaître son restaurant sur les réseaux sociaux
- Comment utiliser l’application WordPress sur votre iPhone, iPad et Android (Guide)

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- boutique WooCommerce
- Télécharger théme WooCommerce
- WooCommerce
- woocommerce plugin
- woocommerce pricing
- woocommerce theme
- woocommerce wordpress
- wordpress ecommerce

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Article précédentComment accepter les paiements via votre site Web WordPress

Article suivant15 meilleures alternatives à Google AdSense pour gagner de l’argent

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Comment accepter les paiements via votre site Web WordPress

### Comment utiliser l’application WordPress sur votre iPhone, iPad et Android (Guide)

### 10+ Meilleurs thèmes WordPress pour les cabinets de conseil et de consulting

### Comment augmenter les ventes et le taux de conversion  sur Shopify

### 10+ Meilleurs thèmes WordPress pour les agences immobilières

### Comment partager automatiquement ses articles WordPress sur les réseaux sociaux

### LAISSER UN COMMENTAIRE Annuler la réponse

S'il vous plaît entrer votre commentaire!

S'il vous plaît entrez votre nom ici

Vous avez entré une adresse email incorrecte!
Veuillez entrer votre adresse email ici

Rejoignez l'élite des experts d'internet

Bénéficiez de conseils, des documents exclusifs et  des informations non divulguées...

Nous respectons votre vie privée.

#### Ne Manquez Pas

### Comment choisir un nom de domaine  idéal pour votre site...

Sébastian Magni @ Responsable du contenu -                 2 décembre 20210

Le choix du bon nom de domaine pour votre site Web est crucial pour votre réussite. Si vous choisissez le mauvais nom...

### 15 meilleures alternatives à Google AdSense pour gagner de l’argent

1 décembre 2021

### Comment rendre un thème WordPress compatible avec  WooCommerce

30 novembre 2021

### Comment accepter les paiements via votre site Web WordPress

29 novembre 2021

### Comment créer et gérer une agence du digitale ? Les 8...

28 novembre 2021

#### Articles récents
-
Comment choisir un nom de domaine  idéal pour votre site web
-
15 meilleures alternatives à Google AdSense pour gagner de l’argent
-
Comment rendre un thème WordPress compatible avec  WooCommerce
-
Comment accepter les paiements via votre site Web WordPress
-
Comment créer et gérer une agence du digitale ? Les 8 points à avoir en tête
-
Référencement payant : Qu’est-ce que c’est et comment ça marche ?
-
Comment gagner de l’argent rapidement sur TikTok en 6 points