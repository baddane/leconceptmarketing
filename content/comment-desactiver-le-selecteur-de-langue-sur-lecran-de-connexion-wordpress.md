---
title: "Comment désactiver le sélecteur de langue sur l’écran de connexion WordPress"
permalink: "/comment-desactiver-le-selecteur-de-langue-sur-lecran-de-connexion-wordpress/"
legacy_permalinks: []
type: "post"
date: "2022-02-17T09:38:23+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Meilleur du Web","WordPress"]
tags: ["désactiver le sélecteur de langue","wordpress"]
description: "La désactivation du sélecteur de langue fait de votre langue par défaut la seule option sur la page de connexion, mais les utilisateurs pourront toujours changer la langue dans leurs paramètres de profil"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/02/www.jpg"
source_url: "https://leconceptmarketing.com/comment-desactiver-le-selecteur-de-langue-sur-lecran-de-connexion-wordpress/"
source_capture: "20220521225821"
---
Voulez-vous désactiver le sélecteur de langue sur l’écran de connexion [WordPress](https://leconceptmarketing.com/quest-ce-que-cest-systeme-de-gestion-de-contenu-cms/) ?

La désactivation du sélecteur de langue fait de votre langue par défaut la seule option sur la page de connexion, mais les utilisateurs pourront toujours changer la langue dans leurs paramètres de profil.

Dans cet article, nous allons vous montrer comment désactiver le menu déroulant du sélecteur de langue sur l’écran de connexion WordPress.

- 1 Pourquoi désactiver le sélecteur de langue sur l’écran de connexion WordPress ?
- 2 Méthode 1. Désactiver le sélecteur de langue sur l’écran de connexion WordPress avec un plugin WordPress
- 3 Méthode 2. Désactiver le sélecteur de langue de connexion WordPress sans plugin

## Pourquoi désactiver le sélecteur de langue sur l’écran de connexion WordPress ?

La version de WordPress 5.9 a introduit une nouvelle option de connexion déroulante qui permet aux utilisateurs de sélectionner une nouvelle langue lors de la connexion au site Web.

**S’il y a plus d’une langue active sur le site, cette option apparaîtra.**

Cela fonctionne bien pour les sites Web multilingues et les équipes avec différents utilisateurs qui pourraient vouloir accéder au tableau de bord WordPress dans une langue différente.

Mais si vous souhaitez que votre page de connexion reste simple et que vos utilisateurs n’aient pas besoin de changer fréquemment de langue, sa suppression peut aider à désencombrer la page de connexion. Cela peut également vous aider à garder le contrôle sur la conception de votre page de connexion personnalisée.

**Noter:** Le sélecteur de langue ne rend pas votre site Web WordPress multilingue, il traduit simplement les pages de connexion et de réinitialisation du mot de passe WordPress et le tableau de bord WordPress.

Cela dit, montrons comment désactiver le sélecteur de langue sur votre site WordPress. Utilisez simplement les liens rapides ci-dessous pour accéder directement à la méthode que vous souhaitez utiliser.

**👉🏼 Lecture complémentaire : [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)**

## Méthode 1. Désactiver le sélecteur de langue sur l’écran de connexion WordPress avec un plugin WordPress

Le moyen le plus convivial pour les débutants de supprimer le sélecteur de langue WordPress sur l’écran de connexion WordPress consiste à utiliser le [Désactiver le sélecteur de langue de connexion](https://wordpress.org/plugins/disable-login-language-switcher/) brancher.

La première chose que vous devez faire est d’installer et d’activer le plugin. Pour plus de détails, consultez notre guide étape par étape sur la façon d’installer un plugin WordPress.

Lors de l’activation, l’option de changement de langue sera automatiquement supprimée. Vous n’avez aucun paramètre supplémentaire à configurer.

Maintenant, lorsque vous accédez à votre écran de connexion, vous verrez l’écran de connexion standard sans l’option de changement de langue.

![Exemple d'écran de connexion WordPress standard](https://www.wpbeginner.com/wp-content/uploads/2022/02/standard-wordpress-login-screen.png)

## Méthode 2. Désactiver le sélecteur de langue de connexion WordPress sans plugin

Une autre façon de désactiver le sélecteur de langue consiste à ajouter du code à WordPress. Si vous ne l’avez pas encore fait, consultez notre guide sur la façon de copier et coller du code dans WordPress.

Ensuite, vous pouvez ajouter l’extrait de code suivant à votre fichier functions.php, dans un plugin spécifique au site ou en utilisant un plugin d’extraits de code.

```
add_filter( 'login_display_language_dropdown', '__return_false' );
```

Cet extrait désactivera automatiquement le sélecteur de langue sur votre site Web WordPress. Maintenant, lorsque vous visitez la page de connexion, l’option de changer de langue disparaîtra.

Si vous devez activer le changement de langue à l’avenir, supprimez simplement la ligne de code que vous avez ajoutée.

Nous espérons que cet article vous a aidé à apprendre comment désactiver le sélecteur de langue sur l’écran de connexion WordPress. Vous pouvez également consulter notre guide sur la façon d’obtenir un certificat SSL gratuit pour votre site Web WordPress, et nos sélections d’experts des meilleurs logiciels de paie RH pour les petites entreprises.

Si cet article vous a plu, abonnez-vous à notre [Chaîne Youtube](https://www.youtube.com/channel/UCcdoz8n5sRWC--T3tCy9Erg) pour les didacticiels vidéo WordPress. Vous pouvez également nous retrouver sur Twitter et Facebook.

**👉🏼 Lecture complémentaire : [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)**

**À Lire Aussi :**
