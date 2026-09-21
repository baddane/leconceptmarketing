---
title: "Qu'est-ce que Localhost ? Comment se connecte-t-il à WordPress ?"
permalink: "/quest-ce-que-localhost-comment-se-connecte-t-il-a-wordpress/"
legacy_permalinks: []
type: "post"
date: "2021-10-30T13:54:40+00:00"
modified: "2021-11-22T23:09:32+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: []
tags: []
description: "Dans les termes les plus simples et les plus conviviaux, \"localhost\" signifie \"cet ordinateur\". si vous parlez du navigateur Web que vous"
cover: "https://leconceptmarketing.com/wp-content/uploads/2021/10/image-10.png"
source_url: "https://leconceptmarketing.com/quest-ce-que-localhost-comment-se-connecte-t-il-a-wordpress/?amp=1"
source_capture: "20240221161949"
---
Dans les termes les plus simples et les plus conviviaux, “localhost” signifie “cet ordinateur”.

Plus précisément, cela signifie “l’ordinateur sur lequel un programme est exécuté”. Selon le programme dont vous parlez, cela peut signifier votre propre ordinateur ou votre serveur web.

Par exemple, si vous parlez du navigateur Web que vous utilisez pour afficher cette page, “localhost” signifie “votre ordinateur”. Mais si vous travaillez dans un plugin WordPress sur votre site Web, “localhost” signifie votre serveur Web, car le logiciel WordPress se trouve sur votre serveur Web (et non sur votre propre ordinateur).

En fait, il s’agit de “cet ordinateur” du point de vue du programme que vous utilisez, et pas nécessairement du vôtre.

## Quelques détails techniques supplémentaires sur le fonctionnement de Localhost :

### Adresse IP de Localhost :

Par défaut, localhost se résout en 127.0.0.1 lorsqu’il utilise IPv4 et en ::1 lorsqu’il utilise IPv6.

Localhost utilise l’interface réseau loopback, ce qui signifie que toute donnée envoyée à localhost est automatiquement réacheminée sans aucune modification.

## Vous ne pouvez pas enregistrer un nom de domaine .localhost :

Depuis 1999, localhost est officiellement un nom DNS de premier niveau réservé. Cela signifie que vous ne pouvez pas enregistrer un nom de domaine avec l’extension “.localhost”. La raison en est que les développeurs peuvent tester en toute sécurité les sites Web utilisant l’extension .localhost (que vous verrez dans une seconde).

## Comment l’hôte local se connecte-t-il à WordPress ?

Bien que localhost soit un terme général de réseau, vous le verrez souvent référencé lorsque vous travaillerez avec WordPress.

Il peut apparaître à de nombreux endroits différents, mais voici quelques-uns des endroits les plus courants où vous verrez la référence à localhost avec [WordPress](https://fr.wordpress.org/download/).

## 1. Développement WordPress en local :

Lorsque les développeurs créent des sites WordPress, ils ne les installent généralement pas tout de suite sur un serveur web ou un site de test.

Au lieu de cela, ils installent WordPress “localement” sur leur “localhost”. Si vous vous souvenez de la définition donnée au début de cet article, cela signifie que WordPress fonctionne sur leur propre ordinateur, plutôt que sur un serveur web.

Cela permet aux développeurs de travailler facilement dans un bac à sable sécurisé pendant la création du site. Une fois que le site WordPress est prêt à être mis en ligne, les développeurs le feront migrer de leur serveur local vers un serveur web en ligne.

Il existe plusieurs outils populaires que vous pouvez utiliser pour mettre en place votre propre environnement de développement WordPress en hôte local. Voici quelques bonnes options :

- XAMPP
- MAMP
- WAMP

DesktopServer – une solution spécifique à WordPress.
Par exemple, si vous utilisez le logiciel XAMPP, vous pourrez alors accéder à vos sites de développement locaux en utilisant “localhost/folder\_name” :

Et comme “localhost” est une adresse de bouclage, vous pouvez également saisir l’adresse IP de localhost pour accéder au même site de développement local :

En d’autres termes, “localhost” et “127.0.0.1” vous amènent exactement au même endroit.

## 2. Le fichier wp-config.php de votre site :

WordPress est le fichier de configuration de base pour les différents paramètres de WordPress. L’une des choses dont wp-config.php est responsable est le contrôle de la base de données de votre site WordPress, y compris son emplacement.

Dans la plupart des cas, la base de données de votre site WordPress est hébergée sur le même serveur que le logiciel WordPress.

Comme le logiciel de la base de données est exécuté sur le même serveur que le logiciel WordPress, votre fichier wp-config.php définit généralement l’emplacement de la base de données comme “localhost” :

Bien qu’il soit peu probable que vous travailliez quotidiennement avec votre fichier wp-config.php, vous rencontrerez ce même principe si vous utilisez un jour un plugin de migration WordPress. En parlant de ça…

## 3. Tout plugin qui implique votre base de données :

Pour la même raison que ci-dessus, vous rencontrerez souvent localhost lorsque vous travaillez avec un plugin qui implique la base de données de votre site WordPress.

Par exemple, lorsque vous utilisez le plugin de migration Duplicator, vous avez la possibilité de spécifier le “Host” de la base de données MySQL de destination :

Dans la plupart des cas, vous entrerez localhost dans cette case. Encore une fois, c’est parce que la base de données MySQL fonctionne sur le même serveur que le logiciel WordPress.

Et c’est tout ce que la plupart des utilisateurs de WordPress ont besoin de savoir sur localhost !

Rappelez-vous, un raccourci facile est de penser à localhost comme étant “cet ordinateur”. Rappelez-vous simplement que vous devez y penser du point de vue du programme avec lequel vous travaillez !

**À lire aussi :**
