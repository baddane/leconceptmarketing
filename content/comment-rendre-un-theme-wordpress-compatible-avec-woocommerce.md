---
title: "Comment rendre un thème WordPress compatible avec WooCommerce"
permalink: "/comment-rendre-un-theme-wordpress-compatible-avec-woocommerce/"
legacy_permalinks: []
type: "post"
date: "2021-11-30T19:49:43+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Thèmes","WooCommerce"]
tags: ["boutique WooCommerce","Télécharger théme WooCommerce","WooCommerce","woocommerce plugin","woocommerce pricing","woocommerce theme","woocommerce wordpress","wordpress ecommerce"]
description: "En théorie, WooCommerce devrait fonctionner avec n'importe quel thème WordPress (s'il est codé correctement). Cependant, vous pouvez vouloir"
cover: "https://leconceptmarketing.com/wp-content/uploads/2021/11/EEEEE.jpeg"
source_url: "https://leconceptmarketing.com/comment-rendre-un-theme-wordpress-compatible-avec-woocommerce/"
source_capture: "20211202172751"
---
Vous voulez donc ajouter une boutique à votre thème – génial ! **[WooCommerce](http://1.envato.market/do5qbQ)** est un excellent choix. Techniquement parlant, TOUS les thèmes sont “**compatibles WooCommerce**” parce que c’est un plugin.

En théorie, tout plugin devrait fonctionner avec n’importe quel thème WordPress (s’il est codé correctement).

![](https://booklovinmamas.com/wp-content/uploads/2017/04/woocommerce-logo-black.png)

Cependant, en tant que développeur de thème, vous pouvez vouloir modifier la sortie de WooCommerce pour mieux l’adapter à votre thème ou pour fournir des options à vos utilisateurs finaux qui ne sont pas facilement disponibles dans les paramètres de WooCommerce (comme modifier le nombre de colonnes de la boutique).

Vous trouverez ci-dessous quelques extraits utiles que vous pouvez utiliser pour fournir un “meilleur” support pour WooCommerce dans votre thème et/ou pour modifier des choses pour votre conception spécifique.

```
Important : La plupart des extraits ci-dessous utilisent des fonctions disponibles uniquement dans WooCommerce. Assurez-vous donc que ces extraits ne sont pas simplement déposés au bas de votre fichier functions.php dans un thème créé pour la distribution. Si vous avez l'intention de partager votre thème avec d'autres ou de le vendre, assurez-vous de placer les extraits dans leur propre fichier qui n'est chargé que lorsque le plugin WooCommerce est actif.
```

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

Dans mon **[thème Divi](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=50197)**,le thème WordPress le plus populaire au monde, Complet, facile à utiliser et livré avec plus de 62 templates gratuits. j’aime définir une constante personnalisée qui peut être utilisée pour vérifier si WooCommerce est activé.

De cette façon, je peux inclure des fichiers ou exécuter des fonctions uniquement lorsque [WooCommerce](http://1.envato.market/do5qbQ) est actif (voir le message important ci-dessus si vous ne l’avez pas encore fait).

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.20.29-1.png)

## Déclarer le support WooCommerce :

C’est le premier et le plus important morceau de code à ajouter à votre thème qui “active” le support WooCommerce et empêche les avertissements du plugin indiquant à l’utilisateur final que le thème n’est pas compatible.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.22.02.png)

## Supprimer les CSS de WooCommerce :

Personnellement, je préfère remplacer les styles de WooCommerce pour éviter tout problème éventuel avec les plugins WooCommerce tiers. Cependant, si vous voulez supprimer tous les styles de WooCommerce, c’est très facile.

Le snippet suivant permet de supprimer TOUS les styles WooCommerce :

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.27.38.png)

Cet extrait est un exemple de suppression conditionnelle de styles CSS spécifiques :

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.28.41-1.png)

## Activer la galerie de produits, le zoom et la lightbox de WooCommerce (v3.0+) :

Dans WooCommerce 3.0, ils ont introduit une nouvelle galerie de produits, un zoom et une lightbox. Ils doivent tous être activés via “add\_theme\_support” si vous voulez les utiliser dans votre thème.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.32.44.png)

## Supprimer le titre de la boutique :

Beaucoup de thèmes ont déjà des fonctions pour afficher les titres des archives. Ce code supprime le titre supplémentaire de WooCommerce, ce qui est mieux que de le cacher via CSS.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.34.25-1.png)

## Modifier le titre des archives pour la boutique :

Si votre [thème](https://leconceptmarketing.com/10-meilleurs-themes-wordpress-pour-les-cabinets-de-conseil-et-de-consulting/) utilise les fonctions archive\_title() ou get\_archive\_title() pour afficher le titre de vos archives, vous pouvez facilement le modifier via un filtre pour récupérer le nom de votre page produit à la place du titre de l’archive de la boutique.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.35.36.png)

## Modifier le nombre de produits affichés par page sur la boutique :

Permet de modifier le nombre de produits affichés par page sur la boutique et les archives de produits (catégories et tags).

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.36.54.png)

## Modifier le nombre de colonnes affichées sur la boutique par ligne :

Je ne comprends pas pourquoi WooCommerce fonctionne de cette façon, mais vous ne pouvez pas simplement modifier le filtre ‘loop\_shop\_columns’, vous devez également ajouter les classes uniques à la balise body pour que les colonnes fonctionnent.

Alors que les Shortcodes Woo ont un div wrapper avec les classes correctes, les pages de la boutique n’en ont pas, c’est pourquoi nous avons besoin de deux fonctions.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.37.41.png)

## Modifier les flèches de pagination suivante et précédente :

Cet extrait vous permettra de modifier les flèches de pagination de la boutique pour qu’elles correspondent à celles de votre thème.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.39.48.png)

## Modifiez le nombre de colonnes par ligne pour les sections relatives et les ventes incitatives des produits :

Comme dans le cas de la boutique, si vous souhaitez modifier correctement le nombre de colonnes pour les produits connexes et les ventes incitatives sur les pages de produits individuels, vous devez filtrer les colonnes et modifier les classes de corps en conséquence.

![](https://leconceptmarketing.com/wp-content/uploads/2021/11/Capture-décran-2021-11-30-à-10.40.56.png)

## Conclusion :

WooCommerce fonctionne par défaut avec tous les thèmes, mais il est très facile d’ajouter un support supplémentaire pour le plugin afin qu’il s’adapte mieux à votre thème.

J’ai en fait écrit cet article pendant le codage de notre thème [Divi](https://www.elegantthemes.com/affiliates/idevaffiliate.php?id=50197), donc la plupart de ces modifications sont incluses dans notre thème. Si vous préférez, vous pouvez essayer le thème pour voir comment tout a été fait – c’est peut-être un moyen plus facile pour vous d’apprendre comment ajouter un support personnalisé pour le plugin WooCommerce en regardant un thème déjà codé.

**À lire Aussi :**
