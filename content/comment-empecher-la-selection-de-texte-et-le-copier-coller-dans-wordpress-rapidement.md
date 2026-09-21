---
title: "Comment Empêcher la Sélection de Texte et le Copier/Coller dans WordPress (Rapidement)"
permalink: "/comment-empecher-la-selection-de-texte-et-le-copier-coller-dans-wordpress-rapidement/"
legacy_permalinks: []
type: "post"
date: "2023-09-27T12:51:56+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["WordPress"]
tags: ["copier/coller","wordpress"]
description: "Vous voulez rendre la vie dure aux voleurs de contenu ? Voici comment désactiver facilement les fonctions de clic droit, de sélection de texte, de copier/coller et d'impression dans"
cover: "https://leconceptmarketing.com/wp-content/uploads/2023/09/image-29.png"
source_url: "https://leconceptmarketing.com/comment-empecher-la-selection-de-texte-et-le-copier-coller-dans-wordpress-rapidement/?noamp=mobile"
source_capture: "20231201085856"
---
Récemment, un de nos lecteurs nous a demandé comment empêcher la sélection de texte et le copier/coller dans WordPress ?

![](https://leconceptmarketing.com/wp-content/uploads/2023/09/image-29.png)

Beaucoup d’éditeurs qui veulent empêcher les gens de voler leur contenu peuvent vouloir appliquer cette méthode. En fait, il s’agit simplement de rendre un peu plus difficile pour les gens de copier le texte de votre site web.

Dans cet article, nous allons vous montrer comment empêcher facilement la sélection de texte et le copier/coller dans WordPress.

## Pourquoi empêcher la sélection de texte et le copier/coller sur votre site WordPress ?

De nombreux blogueurs constatent que leur contenu est volé et utilisé sans autorisation.

Cela peut se produire par le biais d’un système automatisé de récupération de contenu. Cela peut également se produire si quelqu’un copie manuellement une partie ou la totalité de votre contenu.

L’une des façons de rendre cette situation plus difficile est d’empêcher les gens de copier et de coller votre texte. Vous pouvez le faire en rendant plus difficile la sélection du texte sur votre site web.

N’oubliez pas que les utilisateurs avertis peuvent toujours consulter le code source ou utiliser l’outil Inspect pour copier ce qu’ils veulent. Ces techniques n’arrêteront pas non plus les personnes qui utilisent des outils d’auto-blogging pour récupérer le contenu par RSS.

En gardant cela à l’esprit, examinons quelques moyens d’empêcher la sélection et la copie de texte dans WordPress.

## Méthode n° 1 : Empêcher la sélection de texte à l’aide d’une feuille de style CSS

Cette méthode est plus simple, et il vous suffit d’ajouter [un code CSS ](https://www.atinternet.com/glossaire/css/#:~:text=Le%20CSS%20correspond%20%C3%A0%20un,contient%20des%20%C3%A9l%C3%A9ments%20de%20codage.)personnalisé à votre thème WordPress. S

Tout d’abord, vous devez visiter la page Apparence ” Personnaliser dans la zone d’administration de WordPress pour lancer le personnalisateur de thème.

![](https://leconceptmarketing.com/wp-content/uploads/2023/09/image-27.png)

Dans le personnalisateur de thème, vous devez cliquer sur l’onglet “Additional CSS” dans la colonne de gauche.

Maintenant, vous verrez une boîte pour ajouter un CSS personnalisé à votre [thème WordPress](http://1.envato.market/DVnrqn). Copiez et collez simplement le code CSS suivant dans cette boîte.

```
* {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
   user-select: none; /* Non-prefixed version, currently supported by Chrome, Opera and Firefox */
}
```

**Voici à quoi ressemblera le code une fois ajouté.**

![](https://leconceptmarketing.com/wp-content/uploads/2023/09/image-28.png)

Maintenant, essayez de sélectionner une partie du texte de votre page dans le personnalisateur en direct. Vous constaterez que vous ne pouvez pas le sélectionner.

N’oubliez pas de cliquer sur le bouton “Publier” en haut de l’écran pour rendre vos modifications accessibles à tous.

## Méthode n°2 : Empêcher la sélection de texte à l’aide d’un plugin

Pour cette méthode, nous utiliserons un plugin WordPress qui désactive la sélection de texte et le clic droit. Cela permet également de protéger les images contre le téléchargement et la réutilisation.

Tout d’abord, vous devez installer et activer le plugin WP Content Copy Protection. Pour plus de détails, consultez notre guide pas à pas sur [l’installation d’un plugin WordPress](https://wordpress.org/plugins/wp-content-copy-protector/).

Une fois activé, le plugin fonctionnera directement. Les utilisateurs ne pourront plus copier et coller du texte sur votre site. Ils ne pourront pas non plus faire un clic droit ou imprimer votre contenu.

**[Télécharger le plugin gratuitement ici.](https://wordpress.org/plugins/wp-content-copy-protector/)**

Si vous souhaitez modifier les paramètres du plugin, c’est très simple. Il vous suffit de vous rendre sur la page “**Protection contre la copie**” dans l’interface d’administration de WordPress.

Ici, vous pouvez choisir d’activer ou de désactiver la protection pour des types de contenus spécifiques.

![](https://leconceptmarketing.com/wp-content/uploads/2023/09/image-30.png)

Veillez à cliquer sur le bouton “Enregistrer les paramètres” après toute modification.

Vous pouvez également modifier le message qui apparaîtra si quelqu’un tente d’imprimer votre contenu. Le message s’affichera comme suit dans l’aperçu avant impression et sur l’impression elle-même.

## Est-ce une bonne idée d’empêcher la sélection de texte dans WordPress ?

Bien que de nombreux nouveaux propriétaires de sites web veuillent empêcher les gens de copier/coller le contenu de leur site, ces techniques n’empêchent pas vraiment le vol de contenu.

N’importe quel utilisateur un peu doué en technologie peut facilement ouvrir le code source de votre site web pour copier le contenu qu’il souhaite.

En outre, toutes les personnes qui copient votre texte ne sont pas forcément des voleurs de contenu. Par exemple, certaines personnes peuvent vouloir copier le titre pour partager votre article sur les médias sociaux.

C’est pourquoi empêcher la sélection de texte n’est pas une bonne pratique. Nous vous recommandons de n’utiliser cette méthode que si vous estimez qu’elle est vraiment nécessaire pour votre site.

Dans la plupart des cas, il est préférable de chercher un autre moyen d’empêcher le vol de contenu.

Nous espérons que cet article vous a aidé à apprendre comment empêcher la sélection de texte et le copier/coller dans WordPress. Vous pouvez également consulter notre guide sur la création d’un site d’adhésion avec un contenu protégé, et notre comparaison des meilleurs services d’email marketing pour les contenus réservés aux abonnés.

**Si vous avez aimé cet article, n’hésitez pas à vous abonner à notre chaîne YouTube pour des tutoriels vidéo sur WordPress. Vous pouvez également nous trouver sur Twitter et Facebook.**
