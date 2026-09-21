---
title: "Comment réparer l’erreur 404 des articles de WordPress ?"
permalink: "/comment-reparer-lerreur-404-des-articles-de-wordpress/"
legacy_permalinks: []
type: "post"
date: "2022-01-21T08:00:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Thèmes","WordPress"]
tags: ["articles de WordPress","erreurs WordPress","l'erreur 404","wordpress"]
description: "Les symptômes de cette erreur sont les suivants : lorsqu'un utilisateur visite un seul article sur son site, il obtient une erreur de type \"page 404 - not found\""
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/01/de.jpeg"
source_url: "https://leconceptmarketing.com/comment-reparer-lerreur-404-des-articles-de-wordpress/"
source_capture: "20220209090351"
---
WordPress est un [CMS ](https://leconceptmarketing.com/quest-ce-que-cest-systeme-de-gestion-de-contenu-cms/)puissant. Parfois, une légère modification peut rendre votre site Web inaccessible. Cependant, il est extrêmement facile de trouver une solution à tout problème lié à WordPress Dans le passé, nous avons couvert certains des problèmes les plus courants auxquels les utilisateurs de WordPress sont confrontés.

Un autre problème commun que la plupart des utilisateurs de WordPress rencontrent à un moment donné est le retour d’une erreur 404. Dans cet article, nous allons vous montrer comment réparer l’erreur 404 des articles WordPress.

Habituellement, dans ce scénario, un utilisateur peut accéder à la zone d’administration de WordPress, à la page principale de son blog, mais lorsqu’il accède à un seul article, il obtient une erreur 404 Not found. Tout d’abord, ne paniquez pas, la plupart du temps, vos articles sont toujours là et en sécurité.

Cela se produit généralement si votre fichier .htaccess a été supprimé ou si quelque chose s’est mal passé avec les règles de réécriture. Ce que vous devez faire, c’est corriger les paramètres de vos permaliens.

## Comment réparer l’erreur 404 ?

![](https://leconceptmarketing.com/wp-content/uploads/2022/01/Capture-décran-2022-01-20-à-03.45.49.png)

Cela mettra à jour les paramètres de vos permaliens et les règles de réécriture des flux. Dans la plupart des cas, cette solution corrige l’erreur 404 des articles WordPress. Cependant, si cela ne fonctionne pas pour vous, vous devez probablement mettre à jour votre fichier .htaccess manuellement.

Connectez-vous à votre serveur en utilisant le FTP, et modifiez le fichier .htaccess qui se trouve au même endroit que les dossiers /wp-content/ et /wp-includes/. La chose la plus simple que vous pouvez faire est de rendre temporairement le fichier accessible en écriture en changeant les permissions à 666. Ensuite, répétez la solution originale. N’oubliez pas de remettre les permissions à 660. Vous pouvez également ajouter manuellement ce code dans votre fichier .htaccess :

![](https://leconceptmarketing.com/wp-content/uploads/2022/01/Capture-décran-2022-01-20-à-03.49.50.png)

Correction pour les serveurs locaux
Souvent, les concepteurs et les développeurs installent WordPress sur leurs ordinateurs en utilisant un serveur local à des fins de test. Si vous souhaitez utiliser de jolis permaliens, vous devez activer le module rewrite\_module dans la configuration Apache de votre MAMP, WAMP ou XXAMP.

Nous espérons que cet article vous a aidé à résoudre l’erreur “posts returning 404” dans WordPress. Cette solution a-t-elle fonctionné pour vous ? Avez-vous une autre solution qui a fonctionné pour vous ? Veuillez la partager dans les commentaires ci-dessous. Nous aimerions faire de cet article une ressource complète pour les utilisateurs qui rencontrent ce problème.
