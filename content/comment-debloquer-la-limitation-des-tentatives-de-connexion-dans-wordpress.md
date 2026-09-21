---
title: "Comment débloquer la limitation des tentatives de connexion dans WordPress"
permalink: "/comment-debloquer-la-limitation-des-tentatives-de-connexion-dans-wordpress/"
legacy_permalinks: []
type: "post"
date: "2023-04-10T14:23:27+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["WordPress"]
tags: ["connexion","Limit Login Attempts","tentatives de connexion"]
description: "Lorsque vous créez un site web WordPress, il est conseillé de suivre les meilleures pratiques en matière de sécurité afin de réduire le risque de piratage"
cover: "https://leconceptmarketing.com/wp-content/uploads/2023/04/image-1.png"
source_url: "https://leconceptmarketing.com/comment-debloquer-la-limitation-des-tentatives-de-connexion-dans-wordpress/?noamp=mobile"
source_capture: "20231201105014"
---
Vous n’arrivez pas à vous connecter à votre site web parce que vous avez atteint le nombre maximum de tentatives de connexion infructueuses ?

Si vous avez tapé le mauvais mot de passe trop souvent, vos propres mesures de sécurité peuvent vous empêcher d’accéder à votre tableau de bord WordPress.

![](https://leconceptmarketing.com/wp-content/uploads/2023/04/image.png)

Dans cet article, nous allons vous montrer comment débloquer le plugin Limit Login Attempts dans WordPress.

**👉🏼 Lecture complémentaire :**  [**Logiciel Montage Video InVideo, Avis, Caractéristiques, prix et outils 2023**](https://leconceptmarketing.com/logiciel-montage-video-invideo-avis-caracteristiques-prix-et-outils-2022/)

## Pourquoi êtes-vous bloqué sur votre propre site WordPress ?

Lorsque vous créez un site web WordPress, il est conseillé de suivre les meilleures pratiques en matière de sécurité afin de réduire le risque de piratage.

Nous vous recommandons d’installer **[le plugin Limit Login Attempts Reloaded](https://wordpress.org/plugins/limit-login-attempts-reloaded/)** pour limiter le nombre de tentatives de connexion à votre site web. Cela réduit considérablement les chances d’un pirate d’essayer de deviner votre mot de passe à l’aide d’une attaque par force brute.

![](https://leconceptmarketing.com/wp-content/uploads/2023/04/image-1.png)

Mais si vous passez une mauvaise journée, il se peut que vous tapiez votre propre mot de passe de manière incorrecte. Peut-être avez-vous récemment changé de mot de passe ou n’avez-vous pas réalisé que le verrouillage des majuscules était activé.

Si vous vous trompez trop souvent, vous risquez de vous retrouver bloqué dans votre propre zone d’administration WordPress.

Vous devrez temporairement débloquer les tentatives de connexion dans WordPress pour retrouver l’accès. Nous allons vous montrer deux méthodes :

- Débloquer la limite des tentatives de connexion en utilisant FTP
- Débloquer la limite des tentatives de connexion en utilisant MySQL

👉🏼 **Lecture complémentaire :**  **[HubSpot CRM Avis : Pourquoi utiliser cet outil digital pour piloter votre entreprise ](https://leconceptmarketing.com/hubspot-avis-pourquoi-utiliser-cet-outil-digital-pour-piloter-votre-entreprise/)**

## Méthode 1 : Débloquer Limit Login Attempts en utilisant le FTP

La solution la plus simple pour les débutants est de supprimer le dossier Limit Login Attempts Reloaded, puis de réinstaller le plugin plus tard, une fois que vous pourrez vous connecter.

Pour cette méthode, vous devrez utiliser un client FTP ou l’option de gestion de fichiers dans votre panneau de contrôle d’hébergement WordPress.

Si vous n’avez jamais utilisé le FTP, vous pouvez consulter notre guide sur l’utilisation du FTP pour télécharger des fichiers sur WordPress.

Vous devez accéder à votre site en utilisant votre client FTP ou votre gestionnaire de fichiers, puis vous rendre dans le dossier /wp-content/plugins/. Une fois que vous y êtes, vous pouvez simplement supprimer le dossier du plugin limit-login-attempts-reloaded.

![](https://leconceptmarketing.com/wp-content/uploads/2023/04/image-2.png)

Vous pouvez maintenant vous connecter à votre zone d’administration WordPress.

Lorsque vous êtes prêt, n’oubliez pas de réinstaller et d’activer[ le plugin Limit Login Attempts Reloaded](https://wordpress.org/plugins/limit-login-attempts-reloaded/). Pour plus de détails, consultez notre guide étape par étape sur l’installation d’un plugin WordPress.

## Méthode 2 : Débloquer la limite des tentatives de connexion à l’aide de MySQL

Bien que la méthode 1 soit plus simple, les utilisateurs avancés qui sont familiers avec MySQL et phpMyAdmin peuvent souhaiter supprimer le blocage Limit Login Attempts Unloaded à l’aide d’une requête SQL.

![](https://leconceptmarketing.com/wp-content/uploads/2023/04/image-3.png)

Tout d’abord, vous devez vous connecter à votre tableau de bord d’hébergement web et cliquer sur l’icône ‘phpMyAdmin’ dans la section Bases de données.

Ceci lancera phpMyAdmin dans une nouvelle fenêtre du navigateur. Vous devrez sélectionner votre base de données WordPress si elle ne l’est pas déjà. Ensuite, vous devez cliquer sur l’onglet “SQL” et coller la requête suivante :

|  |
| --- |
| `UPDATE``wp_options` `SET``option_value =` `''``WHERE``option_name =` `'limit_login_lockouts'``LIMIT 1;` |

![](https://leconceptmarketing.com/wp-content/uploads/2023/04/image-4.png)

Cette requête suppose que vous utilisez le préfixe de base de données par défaut “wp\_”. Si vous avez changé le préfixe de votre base de données, vous devrez mettre à jour la requête avec le préfixe correct.

Une fois cela fait, vous devez cliquer sur le bouton “Go” en bas à droite de l’écran pour exécuter la requête. Un message vous confirme que la requête a été exécutée avec succès.

Le nombre de tentatives infructueuses a été réinitialisé, et vous pouvez maintenant vous connecter à votre zone d’administration WordPress.

👉🏼 **Lecture complémentaire** : [**HostGator Vs Bluehost ? Lequel est le meilleur hébergeurs web et pourquoi ?**](https://leconceptmarketing.com/hostgator-vs-bluehost-lequel-est-le-meilleur-hebergeurs-web-et-pourquoi/)

Si vous préférez débloquer votre propre adresse IP au lieu de celle de tout le monde, exécutez une requête comme celle-ci :

UPDATE wp\_options SET option\_value = REPLACE(option\_value, ‘111.222.111.222’, ”) WHERE option\_name = ‘limit\_login\_lockouts’ LIMIT 1 ;
Veillez à mettre à jour la requête avec votre adresse IP réelle au lieu de “111.222.111.222”. Vous pouvez la trouver en vous rendant sur [WhatIsMyIP.com](https://www.whatismyip.com/) dans votre navigateur Web.

Nous espérons que ce tutoriel vous a aidé à apprendre comment débloquer les tentatives de connexion sur WordPress. Vous voudrez peut-être aussi apprendre comment augmenter le trafic de votre blog ou consulter notre liste des 50 erreurs WordPress les plus courantes et comment les résoudre.

**Si vous avez aimé cet article, abonnez-vous à notre chaîne YouTube pour des tutoriels vidéo. Vous pouvez également nous trouver sur Twitter et Facebook.**

**👉🏼 Ressources :**
