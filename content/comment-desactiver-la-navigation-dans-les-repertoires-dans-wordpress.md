---
title: "Comment désactiver la navigation dans les répertoires dans WordPress"
permalink: "/comment-desactiver-la-navigation-dans-les-repertoires-dans-wordpress/"
legacy_permalinks: []
type: "post"
date: "2022-07-08T10:26:02+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Plugins","Thèmes","WordPress"]
tags: ["CMS","créer un site wordpress","désactiver l'index de répertoire dans wordpress","désactiver la navigation dans les répertoires dans wordpress","extensions","Plugins","sécurité wordpress","site web","thèmes","wordpress"]
description: "Wordpress News, les actualités du Wordpress.. Comment désactiver la navigation dans les répertoires dans WordPress"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/07/Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png"
source_url: "https://leconceptmarketing.com/comment-desactiver-la-navigation-dans-les-repertoires-dans-wordpress/"
source_capture: "20220812185335"
---
Voulez-vous désactiver la navigation dans les répertoires dans WordPress ?

La navigation dans les répertoires peut mettre votre site en danger en montrant des informations importantes aux pirates qui peuvent être utilisées pour exploiter les vulnérabilités des plugins, des thèmes ou même de votre serveur d’hébergement de votre site.

Dans cet article, nous allons vous montrer comment vous pouvez désactiver la navigation dans les répertoires dans WordPress.

- 1 Que fait la désactivation de la navigation dans les répertoires dans WordPress ?
- 2 Comment vérifier si la navigation dans les répertoires est activée dans WordPress
- 3 Comment désactiver la navigation dans les répertoires dans WordPress

#### Que fait la désactivation de la navigation dans les répertoires dans WordPress ?

Chaque fois que quelqu’un visite votre site Web, votre serveur Web traitera cette demande.

Habituellement, le serveur fournit un fichier d’index au navigateur du visiteur, tel que index.html. Cependant, si le serveur ne trouve pas de fichier d’index, il peut afficher à la place tous les fichiers et dossiers du répertoire demandé.

Il s’agit de la navigation dans les répertoires, et elle est souvent activée par défaut.

Si vous avez déjà visité un site et vu une liste de fichiers et de dossiers au lieu d’une page Web, vous avez vu la navigation dans les répertoires en action.

![Un site WordPress avec la navigation dans les répertoires activée](https://leconceptmarketing.com/wp-content/uploads/2022/07/1657272362_661_Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png)

Le problème est que les pirates peuvent utiliser la navigation dans les répertoires pour voir les fichiers qui composent votre site Web, y compris tous les thèmes et plugins que vous utilisez.

Si l’un de ces thèmes ou plugins présente des vulnérabilités connues, les pirates peuvent utiliser ces connaissances pour prendre le contrôle de votre blog ou site Web WordPress, voler vos données ou effectuer d’autres actions.

Les attaquants peuvent également utiliser la navigation dans les répertoires pour consulter les informations confidentielles contenues dans vos fichiers et dossiers. Ils peuvent même copier le contenu de votre site Web, y compris le contenu que vous factureriez habituellement, comme les téléchargements d’ebooks ou les cours en ligne.

C’est pourquoi il est considéré comme une bonne pratique de désactiver la navigation dans les répertoires dans WordPress.

#### Comment vérifier si la navigation dans les répertoires est activée dans WordPress

Le moyen le plus simple de vérifier si la navigation dans les répertoires est actuellement activée pour votre site Web WordPress consiste simplement à visiter le lien du dossier /wp-includes/ comme ceci : https://example.com/wp-includes/.

Vous voudrez remplacer www.example.com par l’URL de votre site Web.

Si vous recevez un message 403 Forbidden ou similaire, la navigation dans les répertoires est déjà désactivée sur votre site Web WordPress.

![Un site Web avec la navigation dans les répertoires désactivée](https://leconceptmarketing.com/wp-content/uploads/2022/07/1657272362_73_Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png)

Si vous voyez plutôt une liste de fichiers et de dossiers, cela signifie que la navigation dans les répertoires est activée pour votre site Web.

![Un site WordPress avec la navigation dans les répertoires activée](https://leconceptmarketing.com/wp-content/uploads/2022/07/1657272362_661_Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png)

Étant donné que cela rend votre site Web plus vulnérable aux attaques, vous souhaiterez généralement bloquer la navigation dans les répertoires dans WordPress.

#### Comment désactiver la navigation dans les répertoires dans WordPress

Pour désactiver la liste des répertoires, vous devrez ajouter du code au fichier .htaccess de votre site.

Pour accéder au fichier, vous aurez besoin d’un client FTP, ou vous pouvez utiliser l’application de gestion de fichiers dans votre panneau de contrôle d’hébergement WordPress.

Si c’est la première fois que vous utilisez FTP, vous pouvez consulter notre guide complet sur la façon de vous connecter à votre site en utilisant FTP.

Après vous être connecté à votre site, ouvrez simplement le dossier « public » de votre site Web et recherchez le fichier .htaccess. Vous pouvez modifier le fichier .htaccess en le téléchargeant sur votre bureau, puis en l’ouvrant dans un éditeur de texte tel que le Bloc-notes.

Tout en bas du fichier, ajoutez simplement le code suivant :

Cela ressemblera à ceci :

![Le fichier WordPress .htaccess](https://leconceptmarketing.com/wp-content/uploads/2022/07/1657272362_223_Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png)

Une fois que vous avez terminé, enregistrez votre fichier .htaccess et téléchargez-le sur votre serveur à l’aide d’un client FTP.

C’est ça. Maintenant, si vous visitez la même URL http://example.com/wp-includes/, vous obtiendrez un message 403 Forbidden ou similaire.

![Comment désactiver la navigation dans les répertoires dans WordPress](https://leconceptmarketing.com/wp-content/uploads/2022/07/1657272362_393_Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png)

Nous espérons que cet article vous a aidé à apprendre comment désactiver la navigation dans les répertoires dans WordPress. Vous pouvez également consulter notre guide de sécurité WordPress ultime ou consulter notre sélection d’experts du meilleur plugin d’adhésion WordPress pour protéger vos fichiers.

Si cet article vous a plu, abonnez-vous à notre [Chaîne Youtube](https://youtube.com/wpbeginner?sub_confirmation=1) pour les didacticiels vidéo WordPress. Vous pouvez également nous retrouver sur [Twitter](https://twitter.com/wpbeginner) et [Facebook](https://facebook.com/wpbeginner).
