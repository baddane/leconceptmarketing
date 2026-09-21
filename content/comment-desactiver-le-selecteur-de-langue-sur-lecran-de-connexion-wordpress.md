---
title: "Comment désactiver le sélecteur de langue sur l&#039;écran de connexion WordPress"
permalink: "/comment-desactiver-le-selecteur-de-langue-sur-lecran-de-connexion-wordpress/"
date: "2022-02-17T08:38:23+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "Voulez-vous désactiver le sélecteur de langue sur l&#039;écran de connexion WordPress ?La désactivation du sélecteur de langue fait de votre langue par dé"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/02/www.jpg"
source_capture: "20220521225821"
method: "regex"
---
Accueil  Meilleur du Web  Comment désactiver le sélecteur de langue sur l’écran de connexion WordPress

- Meilleur du Web
- Wordpress

# Comment désactiver le sélecteur de langue sur l’écran de connexion WordPress

17 février 2022295
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

Voulez-vous désactiver le sélecteur de langue sur l’écran de connexion WordPress ?
La désactivation du sélecteur de langue fait de votre langue par défaut la seule option sur la page de connexion, mais les utilisateurs pourront toujours changer la langue dans leurs paramètres de profil.
Dans cet article, nous allons vous montrer comment désactiver le menu déroulant du sélecteur de langue sur l’écran de connexion WordPress.
Table Des Mati&egrave;res
- 1 Pourquoi désactiver le sélecteur de langue sur l’écran de connexion WordPress ?
- 2 Méthode 1. Désactiver le sélecteur de langue sur l’écran de connexion WordPress avec un plugin WordPress
- 3 Méthode 2. Désactiver le sélecteur de langue de connexion WordPress sans plugin

## Pourquoi désactiver le sélecteur de langue sur l’écran de connexion WordPress ?
La version de WordPress 5.9 a introduit une nouvelle option de connexion déroulante qui permet aux utilisateurs de sélectionner une nouvelle langue lors de la connexion au site Web.
S’il y a plus d’une langue active sur le site, cette option apparaîtra.
Cela fonctionne bien pour les sites Web multilingues et les équipes avec différents utilisateurs qui pourraient vouloir accéder au tableau de bord WordPress dans une langue différente.
Mais si vous souhaitez que votre page de connexion reste simple et que vos utilisateurs n’aient pas besoin de changer fréquemment de langue, sa suppression peut aider à désencombrer la page de connexion. Cela peut également vous aider à garder le contrôle sur la conception de votre page de connexion personnalisée.
👉🏼 Lecture complémentaire :  Comment accepter Bitcoin sur WordPress - Votre guide étape par étape

Noter: Le sélecteur de langue ne rend pas votre site Web WordPress multilingue, il traduit simplement les pages de connexion et de réinitialisation du mot de passe WordPress et le tableau de bord WordPress.
Cela dit, montrons comment désactiver le sélecteur de langue sur votre site WordPress. Utilisez simplement les liens rapides ci-dessous pour accéder directement à la méthode que vous souhaitez utiliser.
👉🏼  Lecture complémentaire : Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022

## Méthode 1. Désactiver le sélecteur de langue sur l’écran de connexion WordPress avec un plugin WordPress
Le moyen le plus convivial pour les débutants de supprimer le sélecteur de langue WordPress sur l’écran de connexion WordPress consiste à utiliser le Désactiver le sélecteur de langue de connexion brancher.
La première chose que vous devez faire est d’installer et d’activer le plugin. Pour plus de détails, consultez notre guide étape par étape sur la façon d’installer un plugin WordPress.
Lors de l’activation, l’option de changement de langue sera automatiquement supprimée. Vous n’avez aucun paramètre supplémentaire à configurer.
Maintenant, lorsque vous accédez à votre écran de connexion, vous verrez l’écran de connexion standard sans l’option de changement de langue.

## Méthode 2. Désactiver le sélecteur de langue de connexion WordPress sans plugin
Une autre façon de désactiver le sélecteur de langue consiste à ajouter du code à WordPress. Si vous ne l’avez pas encore fait, consultez notre guide sur la façon de copier et coller du code dans WordPress.
👉🏼 Lecture complémentaire :  Comment réduire le coût de vos publicités Facebook | Conseil d'Experts

Ensuite, vous pouvez ajouter l’extrait de code suivant à votre fichier functions.php, dans un plugin spécifique au site ou en utilisant un plugin d’extraits de code.
add_filter( 'login_display_language_dropdown', '__return_false' );
Cet extrait désactivera automatiquement le sélecteur de langue sur votre site Web WordPress. Maintenant, lorsque vous visitez la page de connexion, l’option de changer de langue disparaîtra.
Si vous devez activer le changement de langue à l’avenir, supprimez simplement la ligne de code que vous avez ajoutée.
Nous espérons que cet article vous a aidé à apprendre comment désactiver le sélecteur de langue sur l’écran de connexion WordPress. Vous pouvez également consulter notre guide sur la façon d’obtenir un certificat SSL gratuit pour votre site Web WordPress, et nos sélections d’experts des meilleurs logiciels de paie RH pour les petites entreprises.
Si cet article vous a plu, abonnez-vous à notre Chaîne Youtube pour les didacticiels vidéo WordPress. Vous pouvez également nous retrouver sur Twitter et Facebook.
👉🏼  Lecture complémentaire : Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022
À Lire Aussi  :
- Les 14 meilleurs modèles de présentation marketing pour votre entreprise 2022
- Qu’est-ce qu’une Agence d’Inbound Marketing ?
- Guide de Marketing Numérique : Définition, Stratégie et Exemples
- 3 types de CRM et comment choisir le meilleur pour votre entreprise
- Le Top 22 Meilleurs Outils en Marketing Digital  Indispensables en 2022
👉🏼 Lecture complémentaire :  ▷ Le merchandising vers une ère de digitalisation

Sylvere Gelien Responsable Webmarketing & Acquisitions // Marchés : France, Uk, USA, CA
Sylvere Gelien est un Consultant en Marketing Digital & Stratégie eCommerce chez @Search Engine Spot

- TAGS
- désactiver le sélecteur de langue
- wordpress

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Article précédent61% des acteurs financiers luxembourgeois se lanceront dans l’aventure crypto en 2022

Article suivantComment créer une page de destination Facebook Ads dans WordPress

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Qu’est-ce qu’une société SaaS ? | Exemples et signification

### Comment accepter Bitcoin sur WordPress &#8211; Votre guide étape par étape

### Comment Ajouter Correctement Google AdSense à votre site WordPress

### Comment protéger un site WordPress contre les pirates informatiques ?

### 4 stratégies de veille tarifaire : Une formidable opportunité de se démarquer

### Conseils de montage vidéo pour le marketing dans 10 industries énormes Le

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

Label

{}
[+]

Nom*

E-mail*

Site web

0 Commentaires

 Commentaires en ligne
Afficher tous les commentaires

Rejoignez l'élite des experts d'internet

Bénéficiez de conseils, des documents exclusifs et  des informations non divulguées...

Nous respectons votre vie privée.

#### Ne Manquez Pas

### Comment accepter Bitcoin sur WordPress &#8211; Votre guide étape par étape

Sébastian Magni @ Responsable du contenu -                 20 avril 20222

Bien que le bitcoin soit imprévisible, sa valeur et son utilisation grand public n'ont cessé d'augmenter, à la grande satisfaction de ceux...

### Comment Ajouter Correctement Google AdSense à votre site WordPress

7 avril 2022

### Comment protéger un site WordPress contre les pirates informatiques ?

25 mars 2022

### Qu’est-ce qu’une Landing Page et Comment Fonctionne-t-elle ?

23 février 2022

### Divi d’Elegant Themes &#8211; Qu’est-ce que Divi et combien coûte-t-il ?

22 février 2022

#### Articles récents
-
Tout ce que tu as besoin de savoir
-
10 tactiques qui fonctionnent réellement
-
L’adresse Bitcoin transfère 2 457 BTC de Coinbase
-
TikTok lance une fonctionnalité de crédit de créateur
-
Les nouveaux NFT compensent les émissions du marché.  Le prix est de 17 millions de dollars.
-
Les liens les plus consultés de Facebook dominés par le spam
-
TikTok lance Branded Mission, une nouvelle façon de crowdsourcer la création