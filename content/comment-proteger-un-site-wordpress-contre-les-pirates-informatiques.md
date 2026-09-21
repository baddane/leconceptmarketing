---
title: "Comment protéger un site WordPress contre les pirates informatiques ?"
permalink: "/comment-proteger-un-site-wordpress-contre-les-pirates-informatiques/"
date: "2022-03-25T07:00:00+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "Pour de nombreux sites WordPress, le simple fait de prendre de petites mesures pour sécuriser un site Web suffit à empêcher les sites d&#039;être piratés. Pour"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/03/wordpress-security-bug.jpeg"
source_capture: "20220524003359"
method: "regex"
---
Accueil  Thémes  Comment protéger un site WordPress contre les pirates informatiques ?

- Thémes
- Wordpress

# Comment protéger un site WordPress contre les pirates informatiques ?

25 mars 2022141
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

Pour de nombreux sites WordPress, le simple fait de prendre de petites mesures pour sécuriser un site Web suffit à empêcher les sites d’être piratés. Pour en savoir plus, cliquez ici.
WordPress est une cible fréquente pour le piratage. Les pirates ciblent le thème, les fichiers de base de WordPress, les plugins, et même la page de connexion.

Voici les mesures à prendre pour réduire les risques de piratage et faciliter la récupération si cela devait
arriver.
Table Des Mati&egrave;res
- 1 Comment les pirates attaquent WordPress :
- 2 Sécurisez votre site WordPress avec un pare-feu :
- 3 À propos des agents utilisateur (UA) :
- 4 Défense de WordPress contre les exploits :
- 5 Renforcement de la sécurité des sites Web :
- 6 Limitez les connexions à votre site :
- 7 Sauvegarde de votre site WordPress :
- 8 Mettez à jour tous les thèmes et plugins :
- 9 Attention aux plugins abandonnés :
- 10 Protégez votre site WordPress contre les pirates informatiques :

## Comment les pirates attaquent WordPress :
Tous les sites sur le web sont constamment attaqués &#8211; qu’il s’agisse d’un forum phpBB ou d’un site WordPress &#8211; tous les sites sont sondés par les pirates. Il n’est pas rare qu’un pirate analyse des milliers de pages ou essaie de se connecter des centaines de fois par jour.
Et il ne s’agit là que d’un seul pirate. Les sites sont attaqués par plusieurs pirates en même temps.
En général, ce n’est pas une personne qui essaie de vous pirater. Les pirates utilisent des logiciels automatisés pour parcourir le Web et rechercher des faiblesses spécifiques dans le site.
Ces logiciels automatisés qui explorent le Web sont appelés &#8220;bots&#8221;. Je les appelle &#8220;bots&#8221; pour les distinguer des &#8220;scraper bots&#8221; (logiciels qui essaient de copier du contenu).

## Sécurisez votre site WordPress avec un pare-feu :
Un pare-feu est un logiciel qui bloque un intrus. À mon avis, le meilleur pare-feu WordPress est un plugin appelé Wordfence.
→ Découvrez maintenant : Les meilleurs plugins pour sécuriser un site WordPress
Wordfence vérifie si le comportement du visiteur d’un site Web correspond à celui d’un bot abusif. Si le robot enfreint certaines règles, comme demander trop de pages Web dans un court laps de temps, Wordfence le bloque automatiquement.
Wordfence est également programmé pour autoriser les robots légitimes comme Google et Bing sur le site.
Il existe des fonctions avancées qui permettent à l’éditeur de voir quels robots attaquent son site et d’en connaître la provenance, par exemple s’il s’agit d’un mauvais robot provenant d’Amazon Web Services ou de Bluehost. Wordfence offre à l’éditeur la possibilité de bloquer le robot par son adresse IP, par toute la plage d’adresses IP ou même par un faux agent utilisateur de navigateur utilisé par le robot.
👉🏼 Lecture complémentaire :  Comment partager automatiquement ses articles WordPress sur les réseaux sociaux

## À propos des agents utilisateur (UA) :
Un agent utilisateur est une information d’identification que le navigateur envoie et qui indique au site Web de quel navigateur il s’agit (Chrome, Firefox, Vivaldi) et sur quel système d’exploitation il fonctionne (Windows 10, Mac OS X).
Par exemple, voici une chaîne d’agent utilisateur pour un navigateur Safari 11 sur un ordinateur Mac OS X :
Mozilla/5.0 (Macintosh ; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15
Les robots utilisent de nombreux agents utilisateurs différents pour tromper les sites Web et s’infiltrer. Par exemple, certains bots se font passer pour un navigateur sous Windows XP.
Le nombre réel d’utilisateurs de Windows XP est proche de zéro, je peux créer une règle avec Wordfence pour bloquer tous les agents utilisateurs avec Windows XP comme système d’exploitation et avec cette seule règle, je peux bloquer des milliers de mauvais bots, quel que soit le pays d’où ils viennent ou l’adresse IP.
Les mauvais robots réagissent parfois en changeant d’agent utilisateur. En combinant ces règles, un éditeur a donc une chance de bloquer un large éventail de mauvais robots pirates.
Et cela avec la version gratuite de Wordfence.
La version payante permet de bloquer des pays entiers. Ainsi, si les visiteurs légitimes de votre site ne proviennent pas de certains pays, vous pouvez bloquer tous les visiteurs qui viennent de ces pays.

## Défense de WordPress contre les exploits :
En outre, la version payante de Wordfence vous protège à l’avance contre de nombreux thèmes et plugins compromis avant que ceux-ci ne soient corrigés.
Dès que les chercheurs de Wordfence ont connaissance d’un exploit, ils mettent à jour la version premium du pare-feu afin de protéger les abonnés contre ces exploits, parfois des semaines avant que l’exploit ne soit corrigé par le développeur du thème ou du plugin compromis.
→ Découvrez maintenant : Les meilleurs plugins pour sécuriser un site WordPress

## Renforcement de la sécurité des sites Web :
Un autre plugin gratuit qui fournit une couche supplémentaire de protection s’appelle Sucuri Security. Sucuri (propriété de GoDaddy) aide à renforcer la sécurité de WordPress pour empêcher les mauvais robots de profiter de certains types d’attaques. Il dispose également d’une fonction de recherche de logiciels malveillants qui vérifie tous les fichiers pour voir s’ils ont été modifiés.
Sucuri vous alerte chaque fois que quelqu’un se connecte à votre site, ce qui aide les éditeurs à identifier si un pirate se connecte. Sucuri peut également alerter un éditeur si un fichier a été modifié, ce que font les pirates.
Voici les caractéristiques de la version gratuite de Sucuri :
- Audit des activités de sécurité.
- Surveillance de l’intégrité des fichiers.
- Analyse à distance des logiciels malveillants.
- Surveillance des listes noires.
- Renforcement efficace de la sécurité.
- Actions de sécurité post-hacking.
- Notifications de sécurité.
👉🏼 Lecture complémentaire :  Comment utiliser l'application WordPress sur votre iPhone, iPad et Android (Guide)

La version payante de Sucuri comprend un pare-feu pour les sites web.
👉🏼  Lecture complémentaire :  Comment élaborer votre stratégie de marketing des médias sociaux pour 2022

## Limitez les connexions à votre site :
WordFence est capable de bloquer les robots qui remplissent de manière répétée les noms d’utilisateur et les mots de passe sur la page de connexion de WordPress.
Mais si vous voulez vous concentrer sur la limitation de ces connexions, il existe un plugin appelé Limit Login Attempts Reloaded qui permet aux éditeurs de bloquer automatiquement tous les pirates qui entrent un nombre défini de combinaisons de noms et de mots de passe ayant échoué.
Par exemple, vous pouvez le configurer de manière à bloquer les pirates après trois tentatives pour deviner le mot de passe.
→ Découvrez maintenant : Les meilleurs plugins pour sécuriser un site WordPress
Voici les caractéristiques du bloqueur de connexion :
- Limiter le nombre de tentatives de réessai lors de la connexion (par chaque IP). Ceci est entièrement personnalisable.
- Informe l’utilisateur des tentatives restantes ou du temps de blocage sur la page de connexion.
- Journalisation facultative et notification par courriel facultative.
- Il est possible de mettre en liste blanche/blanche les IP et les noms d’utilisateur.
- Compatibilité avec le pare-feu de Sucuri Website.
- Protection de la passerelle XMLRPC.
- Protection de la page de connexion de Woocommerce.
- Compatibilité multisite avec des paramètres MU supplémentaires.
- Conforme au GDPR. Lorsque cette fonctionnalité est activée, toutes les IP enregistrées sont obscurcies (hachées en md5).
- Prise en charge des origines IP personnalisées (Cloudflare, Sucuri, etc.).
Le plugin Limit Login Reloaded offre un moyen rapide d’arrêter les robots de piratage qui tentent de deviner un mot de passe.
→ Découvrez maintenant : Les meilleurs plugins pour sécuriser un site WordPress

## Sauvegarde de votre site WordPress :

Il est important de créer automatiquement une sauvegarde quotidienne de votre site web. Tout événement catastrophique qui fait tomber le site peut être récupéré avec une sauvegarde.
Il existe de nombreuses solutions de sauvegarde, mais celle que j’ai trouvée immensément utile s’appelle UpdraftPlus WordPress Backup Plugin. UpdraftPlus a la confiance de plus de deux millions d’utilisateurs, c’est un choix très apprécié.
Il peut être configuré pour envoyer les sauvegardes par courriel tous les jours ou les envoyer vers un emplacement de stockage en nuage comme Dropbox.
Une fois, j’ai accidentellement supprimé tous les fichiers de mise en page du thème d’un site, ce qui a complètement supprimé l’aspect du site. Mais j’ai pu restaurer le site exactement comme il était avant en utilisant une sauvegarde UpdraftPlus. C’était facile à faire et j’en ai été très reconnaissant.
👉🏼 Lecture complémentaire :  Comment accepter les paiements via votre site Web WordPress

→ Découvrez maintenant : Les meilleurs plugins pour sécuriser un site WordPress

## Mettez à jour tous les thèmes et plugins :
Il est important de toujours mettre à jour tous les thèmes et plugins. WordPress offre un moyen de mettre à jour tous les plugins automatiquement, ce qui est pratique pour les éditeurs ou les entreprises qui ne se connectent pas et ne font pas de mises à jour souvent.
En activant la fonction de mise à jour automatique, un éditeur peut être assuré d’avoir le logiciel le plus à jour. Un plugin obsolète est l’une des principales causes de piratage.
Il existe des raisons de ne pas activer la fonction de mise à jour automatique, mais les aspects négatifs ont tendance à être rares. Par exemple, un plugin mis à jour peut être incompatible avec d’autres plugins.
Mais pour les sites qui ne changent pas fréquemment, la fonction de mise à jour automatique est probablement une bonne chose à activer.
👉🏼  Lecture complémentaire : Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022

## Attention aux plugins abandonnés :
Un dernier avertissement concernant les plugins abandonnés. Certains plugins peuvent continuer à fonctionner des années après avoir été abandonnés par leur développeur. Ce qui peut se passer, c’est que ces anciens plugins peuvent contenir une vulnérabilité. Mais comme ils sont abandonnés, ils ne seront jamais corrigés.
Un autre problème est que les pirates achètent parfois de vieux plugins et les mettent à jour avec des logiciels malveillants et des virus.
Vérifiez tous vos plugins WordPress pour vous assurer qu’ils n’ont pas été abandonnés et qu’ils semblent être mis à jour assez fréquemment.

## Protégez votre site WordPress contre les pirates informatiques :
Pour de nombreux sites, le simple fait de prendre ces petites mesures pour sécuriser un site Web suffit à empêcher les sites d’être piratés. Les versions gratuites de ces plugins offrent une protection extraordinaire et les versions premium offrent encore plus de protection.
Il existe de nombreux plugins de type sécurité et certains d’entre eux contenaient eux-mêmes des vulnérabilités. Wordfence et Sucuri sont à mon avis les meilleurs choix pour la sécurité de WordPress.
À Lire Aussi  :
- Comment protéger un site WordPress contre les pirates informatiques ?
- Qu’est-ce qu’un blog personnel ? Comment créer votre premier blog ?
- Divi d’Elegant Themes &#8211; Qu’est-ce que Divi et combien coûte-t-il ?
- Qu’est-ce que GitHub ? Introduction à GitHub pour les débutants
- Comment résoudre l’erreur d’établissement d’une connexion à une base de données dans WordPress ?

Sylvere Gelien Responsable Webmarketing & Acquisitions // Marchés : France, Uk, USA, CA
Sylvere Gelien est un Consultant en Marketing Digital & Stratégie eCommerce chez @Search Engine Spot

- TAGS
- pirates informatiques
- proteger site wordpress
- protéger son site wordpress
- sécuriser son site wordpress
- securiser son site wordpress
- securiser son wordpress
- wordpress sécuriser son site

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Article précédentQu’est-ce que le Brand Marketing ? Définition &#038; Exemple &#038; Stratégie

Article suivantQu’est-ce que le Growth Hacking ? Une Définition simple et Exemples

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Comment accepter Bitcoin sur WordPress &#8211; Votre guide étape par étape

### Comment Ajouter Correctement Google AdSense à votre site WordPress

### Qu’est-ce qu’un blog personnel ? Comment créer votre premier blog ?

### Qu’est-ce qu’une Landing Page et Comment Fonctionne-t-elle ?

### Divi d’Elegant Themes &#8211; Qu’est-ce que Divi et combien coûte-t-il ?

### Comment désactiver le sélecteur de langue sur l’écran de connexion WordPress

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
Bitcoin récupère un territoire de 30 000 $ après la lutte des dernières semaines
-
5 étapes pour obtenir votre chèque bleu
-
111 raccourcis clavier permettant de gagner du temps pour les gestionnaires de médias sociaux (PC et Mac)
-
Que se passe-t-il lorsque vous dépensez 100 $ pour promouvoir une publication Instagram (expérience)
-
Tout ce que tu as besoin de savoir
-
10 tactiques qui fonctionnent réellement
-
L’adresse Bitcoin transfère 2 457 BTC de Coinbase