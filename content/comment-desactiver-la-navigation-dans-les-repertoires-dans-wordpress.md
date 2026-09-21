---
title: "Comment désactiver la navigation dans les répertoires dans WordPress"
permalink: "/comment-desactiver-la-navigation-dans-les-repertoires-dans-wordpress/"
date: "2022-07-08T09:26:02+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "Voulez-vous désactiver la navigation dans les répertoires dans WordPress ?La navigation dans les répertoires peut mettre votre site en danger en montran"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/07/Comment-desactiver-la-navigation-dans-les-repertoires-dans-WordPress.png"
source_capture: "20220812185335"
method: "regex"
---
Accueil  Plugins  Comment désactiver la navigation dans les répertoires dans WordPress

- Plugins
- Thémes
- Wordpress

# Comment désactiver la navigation dans les répertoires dans WordPress

8 juillet 202252
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

Voulez-vous désactiver la navigation dans les répertoires dans WordPress ?
La navigation dans les répertoires peut mettre votre site en danger en montrant des informations importantes aux pirates qui peuvent être utilisées pour exploiter les vulnérabilités des plugins, des thèmes ou même de votre serveur d’hébergement de votre site.
Dans cet article, nous allons vous montrer comment vous pouvez désactiver la navigation dans les répertoires dans WordPress.
Table Des Mati&egrave;res
- 1 Que fait la désactivation de la navigation dans les répertoires dans WordPress ?
- 2 Comment vérifier si la navigation dans les répertoires est activée dans WordPress
- 3 Comment désactiver la navigation dans les répertoires dans WordPress

#### Que fait la désactivation de la navigation dans les répertoires dans WordPress ?
Chaque fois que quelqu’un visite votre site Web, votre serveur Web traitera cette demande.
Habituellement, le serveur fournit un fichier d’index au navigateur du visiteur, tel que index.html.  Cependant, si le serveur ne trouve pas de fichier d’index, il peut afficher à la place tous les fichiers et dossiers du répertoire demandé.
Il s’agit de la navigation dans les répertoires, et elle est souvent activée par défaut.
Si vous avez déjà visité un site et vu une liste de fichiers et de dossiers au lieu d’une page Web, vous avez vu la navigation dans les répertoires en action.
👉🏼 Lecture complémentaire :  Autoblogging : Comment publier automatiquement des articles wordpress

Le problème est que les pirates peuvent utiliser la navigation dans les répertoires pour voir les fichiers qui composent votre site Web, y compris tous les thèmes et plugins que vous utilisez.
Si l’un de ces thèmes ou plugins présente des vulnérabilités connues, les pirates peuvent utiliser ces connaissances pour prendre le contrôle de votre blog ou site Web WordPress, voler vos données ou effectuer d’autres actions.
Les attaquants peuvent également utiliser la navigation dans les répertoires pour consulter les informations confidentielles contenues dans vos fichiers et dossiers.  Ils peuvent même copier le contenu de votre site Web, y compris le contenu que vous factureriez habituellement, comme les téléchargements d’ebooks ou les cours en ligne.
C’est pourquoi il est considéré comme une bonne pratique de désactiver la navigation dans les répertoires dans WordPress.

#### Comment vérifier si la navigation dans les répertoires est activée dans WordPress
Le moyen le plus simple de vérifier si la navigation dans les répertoires est actuellement activée pour votre site Web WordPress consiste simplement à visiter le lien du dossier /wp-includes/ comme ceci : https://example.com/wp-includes/.
Vous voudrez remplacer www.example.com par l’URL de votre site Web.
Si vous recevez un message 403 Forbidden ou similaire, la navigation dans les répertoires est déjà désactivée sur votre site Web WordPress.
👉🏼 Lecture complémentaire :  Comment intégrer Google Maps sur votre site web Wordpress ?

Si vous voyez plutôt une liste de fichiers et de dossiers, cela signifie que la navigation dans les répertoires est activée pour votre site Web.
Étant donné que cela rend votre site Web plus vulnérable aux attaques, vous souhaiterez généralement bloquer la navigation dans les répertoires dans WordPress.

#### Comment désactiver la navigation dans les répertoires dans WordPress
Pour désactiver la liste des répertoires, vous devrez ajouter du code au fichier .htaccess de votre site.
Pour accéder au fichier, vous aurez besoin d’un client FTP, ou vous pouvez utiliser l’application de gestion de fichiers dans votre panneau de contrôle d’hébergement WordPress.
Si c’est la première fois que vous utilisez FTP, vous pouvez consulter notre guide complet sur la façon de vous connecter à votre site en utilisant FTP.
Après vous être connecté à votre site, ouvrez simplement le dossier « public » de votre site Web et recherchez le fichier .htaccess.  Vous pouvez modifier le fichier .htaccess en le téléchargeant sur votre bureau, puis en l’ouvrant dans un éditeur de texte tel que le Bloc-notes.
Tout en bas du fichier, ajoutez simplement le code suivant :
Cela ressemblera à ceci :
Une fois que vous avez terminé, enregistrez votre fichier .htaccess et téléchargez-le sur votre serveur à l’aide d’un client FTP.
👉🏼 Lecture complémentaire :  Les 6 meilleurs créateurs de sites Web professionnels pour les petites entreprises

C’est ça.  Maintenant, si vous visitez la même URL http://example.com/wp-includes/, vous obtiendrez un message 403 Forbidden ou similaire.
Nous espérons que cet article vous a aidé à apprendre comment désactiver la navigation dans les répertoires dans WordPress.  Vous pouvez également consulter notre guide de sécurité WordPress ultime ou consulter notre sélection d’experts du meilleur plugin d’adhésion WordPress pour protéger vos fichiers.
Si cet article vous a plu, abonnez-vous à notre Chaîne Youtube pour les didacticiels vidéo WordPress.  Vous pouvez également nous retrouver sur Twitter et Facebook.

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- CMS
- créer un site wordpress
- désactiver l'index de répertoire dans wordpress
- désactiver la navigation dans les répertoires dans wordpress
- extensions
- Plugins
- sécurité wordpress
- site web
- thèmes
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

Article précédentSandbox (SAND) s’éclate avec un pic de 12 % en 24 heures

Article suivantTransformez-vous ou périssez !  Ninneko prétend avoir mis la main sur GameFi 2.0￼

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Comment créer facilement un formulaire de demande de bénévolat dans WordPress

### Comment utiliser le générateur de type de schéma personnalisé gratuit de SmartCrawl

### Comment changer les polices dans votre thème WordPress (5 façons simples)

### Le guide ultime pour sécuriser votre connexion WordPress (gratuitement !) avec l’authentification Web

### Sauvegardes d’hébergement horaires de niveau entreprise (seulement 5 $/mois !)

### Comment créer une carte d’image interactive dans WordPress

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

### Comment créer facilement un formulaire de demande de bénévolat dans WordPress

Sébastian Magni @ Responsable du contenu -                 1 août 20220

Vous souhaitez créer un formulaire de candidature bénévole dans WordPress ?En ajoutant un formulaire de candidature à votre site Web, vous pouvez recruter plus...

### Comment utiliser le générateur de type de schéma personnalisé gratuit de...

30 juillet 2022

### Comment changer les polices dans votre thème WordPress (5 façons simples)

26 juillet 2022

### Le guide ultime pour sécuriser votre connexion WordPress (gratuitement !) avec...

24 juillet 2022

### Sauvegardes d’hébergement horaires de niveau entreprise (seulement 5 $/mois !)

18 juillet 2022

#### Articles récents
-
La nouvelle série NFT de Dan Harmon donne aux fans le contrôle du &#8220;Krap&#8221;
-
Comment choisir le meilleur fournisseur de gaz
-
Comment obtenir des NFT gratuits
-
Est-ce la meilleure nouvelle pièce Meme à 10x?  Tamadoge s’apprête à dépasser Dogecoin
-
La Major League Soccer signe Bored Ape NFT en tant qu’athlète
-
Qu’est-ce que l’IPTV ? Tout ce que vous devez savoir sur l’IPTV (Internet Protocol Television)
-
Maggoo Land arrive sur Polygon pour créer un métaverse de jeu