---
title: "Comment débloquer la limitation des tentatives de connexion dans WordPress"
permalink: "/comment-debloquer-la-limitation-des-tentatives-de-connexion-dans-wordpress/"
date: "2023-04-10T14:23:27+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Digital Marketing","Le Journal E-marketing","SEO","Réseaux Sociaux"]
description: "Vous n&#039;arrivez pas à vous connecter à votre site web parce que vous avez atteint le nombre maximum de tentatives de connexion infructueuses ?Si vous avez"
cover: "https://leconceptmarketing.com/wp-content/uploads/2023/04/image-1.png"
source_capture: "20231201105014"
method: "regex"
---
Accueil  Wordpress  Comment débloquer la limitation des tentatives de connexion dans WordPress

- Wordpress

# Comment débloquer la limitation des tentatives de connexion dans WordPress

10 avril 2023648
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

Vous n’arrivez pas à vous connecter à votre site web parce que vous avez atteint le nombre maximum de tentatives de connexion infructueuses ?
Si vous avez tapé le mauvais mot de passe trop souvent, vos propres mesures de sécurité peuvent vous empêcher d’accéder à votre tableau de bord WordPress.
Dans cet article, nous allons vous montrer comment débloquer le plugin Limit Login Attempts dans WordPress.
👉🏼  Lecture complémentaire :  Logiciel Montage Video InVideo, Avis, Caractéristiques, prix et outils 2023

## Pourquoi êtes-vous bloqué sur votre propre site WordPress ?
Lorsque vous créez un site web WordPress, il est conseillé de suivre les meilleures pratiques en matière de sécurité afin de réduire le risque de piratage.
Nous vous recommandons d’installer le plugin Limit Login Attempts Reloaded pour limiter le nombre de tentatives de connexion à votre site web. Cela réduit considérablement les chances d’un pirate d’essayer de deviner votre mot de passe à l’aide d’une attaque par force brute.

Mais si vous passez une mauvaise journée, il se peut que vous tapiez votre propre mot de passe de manière incorrecte. Peut-être avez-vous récemment changé de mot de passe ou n’avez-vous pas réalisé que le verrouillage des majuscules était activé.
Si vous vous trompez trop souvent, vous risquez de vous retrouver bloqué dans votre propre zone d’administration WordPress.
👉🏼 Lecture complémentaire :  Comment protéger un site WordPress contre les pirates informatiques ?

Vous devrez temporairement débloquer les tentatives de connexion dans WordPress pour retrouver l’accès. Nous allons vous montrer deux méthodes :
- Débloquer la limite des tentatives de connexion en utilisant FTP
- Débloquer la limite des tentatives de connexion en utilisant MySQL
👉🏼  Lecture complémentaire :  HubSpot CRM Avis : Pourquoi utiliser cet outil digital pour piloter votre entreprise

## Méthode 1 : Débloquer Limit Login Attempts en utilisant le FTP

La solution la plus simple pour les débutants est de supprimer le dossier Limit Login Attempts Reloaded, puis de réinstaller le plugin plus tard, une fois que vous pourrez vous connecter.
Pour cette méthode, vous devrez utiliser un client FTP ou l’option de gestion de fichiers dans votre panneau de contrôle d’hébergement WordPress.
Si vous n’avez jamais utilisé le FTP, vous pouvez consulter notre guide sur l’utilisation du FTP pour télécharger des fichiers sur WordPress.
Vous devez accéder à votre site en utilisant votre client FTP ou votre gestionnaire de fichiers, puis vous rendre dans le dossier /wp-content/plugins/. Une fois que vous y êtes, vous pouvez simplement supprimer le dossier du plugin limit-login-attempts-reloaded.
Vous pouvez maintenant vous connecter à votre zone d’administration WordPress.
Lorsque vous êtes prêt, n’oubliez pas de réinstaller et d’activer le plugin Limit Login Attempts Reloaded. Pour plus de détails, consultez notre guide étape par étape sur l’installation d’un plugin WordPress.
👉🏼 Lecture complémentaire :  OBJ Box et texte bleu première moitié H1 d'un post WordPress

## Méthode 2 : Débloquer la limite des tentatives de connexion à l’aide de MySQL
Bien que la méthode 1 soit plus simple, les utilisateurs avancés qui sont familiers avec MySQL et phpMyAdmin peuvent souhaiter supprimer le blocage Limit Login Attempts Unloaded à l’aide d’une requête SQL.
Tout d’abord, vous devez vous connecter à votre tableau de bord d’hébergement web et cliquer sur l’icône &#8216;phpMyAdmin’ dans la section Bases de données.
Ceci lancera phpMyAdmin dans une nouvelle fenêtre du navigateur. Vous devrez sélectionner votre base de données WordPress si elle ne l’est pas déjà. Ensuite, vous devez cliquer sur l’onglet &#8220;SQL&#8221; et coller la requête suivante :
UPDATEwp_options SEToption_value = ''WHEREoption_name = 'limit_login_lockouts'LIMIT 1;Cette requête suppose que vous utilisez le préfixe de base de données par défaut &#8220;wp_&#8221;. Si vous avez changé le préfixe de votre base de données, vous devrez mettre à jour la requête avec le préfixe correct.
Une fois cela fait, vous devez cliquer sur le bouton &#8220;Go&#8221; en bas à droite de l’écran pour exécuter la requête. Un message vous confirme que la requête a été exécutée avec succès.
Le nombre de tentatives infructueuses a été réinitialisé, et vous pouvez maintenant vous connecter à votre zone d’administration WordPress.
👉🏼  Lecture complémentaire :  HostGator Vs Bluehost ? Lequel est le meilleur hébergeurs web et pourquoi ?
👉🏼 Lecture complémentaire :  ▷ Les Meilleurs Plugins Gratuits Pour l'optimisation de Votre Référencement

Si vous préférez débloquer votre propre adresse IP au lieu de celle de tout le monde, exécutez une requête comme celle-ci :
UPDATE wp_options SET option_value = REPLACE(option_value, &#8216;111.222.111.222’, &#8221;) WHERE option_name = &#8216;limit_login_lockouts’ LIMIT 1 ;
Veillez à mettre à jour la requête avec votre adresse IP réelle au lieu de &#8220;111.222.111.222&#8221;. Vous pouvez la trouver en vous rendant sur WhatIsMyIP.com dans votre navigateur Web.
Nous espérons que ce tutoriel vous a aidé à apprendre comment débloquer les tentatives de connexion sur WordPress. Vous voudrez peut-être aussi apprendre comment augmenter le trafic de votre blog ou consulter notre liste des 50 erreurs WordPress les plus courantes et comment les résoudre.
Si vous avez aimé cet article, abonnez-vous à notre chaîne YouTube pour des tutoriels vidéo. Vous pouvez également nous trouver sur Twitter et Facebook.
👉🏼  Ressources :
- Super Mario Bros. Wonder Avis
- Les 10 jeux en ligne les plus populaires en 2023 aux États-Unis
- 10 astuces pour améliorer son ordinateur portable pour le jeu
- Top 7 des meilleurs supports de caméra abordables
- Avis sur Manette Hori D-Pad Joy-Con pour Nintendo Switch

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- connexion
- Limit Login Attempts
- tentatives de connexion

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Article précédentComment gagner de l’argent grâce au marketing d’affiliation

Article suivant5 façons dont ChatGPT peut vous aider avec le Crypto Trading

Sébastian Magni @ Responsable du contenu

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Comment Empêcher la Sélection de Texte et le Copier/Coller dans WordPress (Rapidement)

### 5 meilleurs outils WordPress de génération de code QR pour 2023

### 5 Plugins ChatGPT pour WordPress que vous devriez découvrir

### Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?

### Avis du thème Avada | Le produit le plus puissant de tous les temps

### Comment créer facilement un formulaire de demande de bénévolat dans WordPress

0
0
votes
Évaluation de l'article

 S’abonner

 Connexion

Notification pour

nouveaux commentaires de suivinouvelles réponses à mes commentaires

Label

{}
[+]

Nom*

E-mail*

Site web

&#916;

Label

{}
[+]

Nom*

E-mail*

Site web

&#916;

0 Commentaires

 Commentaires en ligne
Afficher tous les commentaires

Rejoignez l'élite des experts d'internet

Bénéficiez de conseils, des documents exclusifs et  des informations non divulguées...

Nous respectons votre vie privée.

#### Ne Manquez Pas

### Comment Empêcher la Sélection de Texte et le Copier/Coller dans WordPress...

Sébastian Magni @ Responsable du contenu -                 27 septembre 2023                0

Récemment, un de nos lecteurs nous a demandé comment empêcher la sélection de texte et le copier/coller dans WordPress ?Beaucoup d'éditeurs qui veulent empêcher...

### 5 meilleurs outils WordPress de génération de code QR pour 2023

17 mars 2023

### 5 Plugins ChatGPT pour WordPress que vous devriez découvrir

14 mars 2023

### Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?

2 janvier 2023

### Avis du thème Avada | Le produit le plus puissant de...

15 septembre 2022

#### Articles récents
-
Super Mario Bros. Wonder Avis
-
Les 10 jeux en ligne les plus populaires en 2023 aux États-Unis
-
10 astuces pour améliorer son ordinateur portable pour le jeu
-
Top 7 des meilleurs supports de caméra abordables
-
Avis sur Manette Hori D-Pad Joy-Con pour Nintendo Switch
-
Les Clés de la Prospérité Numérique : Décryptage de la Formation en Marketing Digital
-
Qu’est-ce que le fichier test EICAR et comment fonctionne-t-il ?