---
title: "Comment débloquer Robots.txt et supprimer &quot; noindex &quot; sur WordPress ?"
permalink: "/comment-debloquer-robots-txt-et-supprimer-noindex-sur-wordpress-2/"
date: "2023-01-02T07:00:00+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Investissement","Crypto-monnaies","Le Journal E-marketing"]
description: "Vous avez du mal à faire en sorte que votre site Web WordPress soit exploré ou indexé dans les recherches ? Lorsque vous vous connectez à la Search Console"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/12/image-23.png"
source_capture: "20230203093815"
method: "regex"
---
Accueil  Thémes  Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?

- Thémes
- Wordpress

# Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?

2 janvier 202388
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

Vous avez du mal à faire en sorte que votre site Web WordPress soit exploré ou indexé dans les recherches ? Lorsque vous vous connectez à la Search Console de Google et demandez l’indexation, vous recevez toutes sortes de messages d’erreur concernant les balises robots.txt et/ou les balises méta &#8220;noindex&#8221; ? Si c’est le cas, vous êtes au bon endroit. Dans cet article de blog, je vais vous expliquer ces deux problèmes courants et comment les résoudre.
👉🏼  Lecture complémentaire :  Comment faire un SEO audit en 8 étapes ? La Checklist Ultime 2022
Table Des Mati&egrave;res
- 1 Dépannage des problèmes d’index et de crawl : Par où commencer :
- 2 Problème n°1 : Domaine ou URL bloqué par Robots.txt
- 3 Problème n° 2 : Supprimez la balise Meta &#8221; noindex &#8221; dans WordPress

## Dépannage des problèmes d’index et de crawl : Par où commencer :
Tout d’abord, essayons de circonscrire le problème. Pour ce faire, connectez-vous à Google Search Console. Ensuite, copiez et collez l’URL de la page d’accueil de votre site Web dans le testeur robots.txt et cliquez sur Envoyer. (Pour l’instant, cet outil n’existe que dans l’ancienne version de Google Search Console.) Si l’URL est &#8220;BLOQUÉE&#8221;, reportez-vous au problème n° 1, si elle est &#8220;AUTORISÉE&#8221;, reportez-vous au problème n° 2 ci-dessous.

## Problème n°1 : Domaine ou URL bloqué par Robots.txt

Si la ligne disallow s’allume en rouge et que vous voyez le mot &#8220;BLOCKED&#8221; apparaître dans la case en bas à droite comme dans la capture d’écran ci-dessous, le fichier robots.txt est le coupable. Pour remédier à ce problème, vous devez pouvoir accéder au fichier robots.txt de votre site Web et le modifier*.
*Si vous n’êtes pas une personne qui a l’habitude de jouer dans l’arrière-plan de votre site Web, je vous encourage vivement à contacter votre développeur de site Web, votre informaticien ou la personne chargée de la maintenance du site.
👉🏼 Lecture complémentaire :  ▷ 10 + Thèmes WordPress pour créer votre boutique en ligne

Dans l’exemple ci-dessus, il y a deux choses qui se passent, l’une bonne et l’autre mauvaise en fonction de notre situation actuelle. Cette URL, /wp-admin/, est volontairement interdite car nous ne souhaitons pas que la partie arrière de notre site Web soit explorée par les moteurs de recherche. Cela doit rester.
Cependant, la ligne Disallow : / est celle qui pose problème. Cette ligne, ou plutôt cette barre oblique, empêche tous les moteurs de recherche d’explorer votre site Web… en entier. Pour débloquer le fichier robots.txt, il faut donc supprimer cette partie du fichier robots.txt.
Il suffit littéralement d’un seul caractère pour mettre le feu aux poudres. Une fois que la modification nécessaire a été apportée au fichier, remettez l’URL de la page d’accueil dans le testeur de robots.txt pour vérifier si votre site accueille désormais les moteurs de recherche. Si tout va bien, la case en bas à droite indiquera &#8220;ALLOWED&#8221; en vert et les moteurs de recherche pourront commencer à explorer le site.

Cette correction devrait permettre de débloquer le fichier robots.txt pour l’ensemble du site (ou du moins pour toutes les pages qui ne sont pas spécifiquement désignées comme interdites, comme l’URL /wp-admin/ ci-dessus), mais n’hésitez pas à copier et coller quelques pages supplémentaires dans l’outil de test pour vous assurer que le problème n’est pas uniquement résolu pour votre page d’accueil.
👉🏼  Lecture complémentaire :  Comment identifier et éliminer la cannibalisation des mots-clés pour améliorer votre référencement
👉🏼 Lecture complémentaire :  ▷ Thèmes WordPress Arabe : les 10 meilleurs thèmes RTL gratuits !

## Problème n° 2 : Supprimez la balise Meta &#8221; noindex &#8221; dans WordPress
Si le problème ci-dessus n’est pas celui de votre site Web, c’est-à-dire que tout est &#8220;AUTORISÉ&#8221; (comme il se doit), il existe une autre raison courante pour laquelle votre site Web WordPress n’apparaît pas dans les résultats de recherche : la balise &#8220;noindex&#8221;.
Pour voir si c’est le cas, revenez à la nouvelle version de Search Console et collez n’importe quelle URL dans le champ de recherche &#8220;Inspecter n’importe quelle URL dans…&#8221; en haut de la page et appuyez sur la touche Entrée.
Si le rapport d’inspection d’URL affiche le message suivant : No : &#8216;noindex’ detected in &#8216;robots’ meta tag, c’est un simple paramètre de case à cocher dans l’arrière-plan de WordPress qui est à l’origine de toute cette agitation.
Pour empêcher les moteurs de recherche d’indexer votre site Web, procédez comme suit :
- Connectez-vous à WordPress
- Allez dans Réglages → Lecture
- Faites défiler la page jusqu’à l’endroit où il est indiqué &#8211; Visibilité des moteurs de recherche
- Décochez la case à côté de &#8220;Décourager les moteurs de recherche d’indexer ce site&#8221;.
- Cliquez sur le bouton &#8220;Enregistrer les modifications&#8221; ci-dessous
Si vous utilisez le plugin Yoast SEO &#8211; WordPress, vérifiez également les paramètres des articles de blog pour vous assurer qu’ils sont également configurés pour permettre l’indexation.
👉🏼  Lecture complémentaire :  Google EAT : Comment améliorer votre référencement On-Page SEO
Une fois cette opération terminée, retournez dans Search Console et soumettez à nouveau l’URL que vous avez essayée précédemment. Si vos paramètres sont correctement configurés, tout devrait changer. Désormais, lorsque vous soumettez une URL, le rapport d’inspection de l’URL devrait être dépourvu de tous les avertissements et messages d’erreur, du moins ceux liés à l’indexation et à la facilité d’exploration, et vous serez en mesure de &#8220;demander l’indexation&#8221;, ce qui, j’imagine, était votre objectif depuis le début.
👉🏼 Lecture complémentaire :  ▷ Les 10+ Meilleurs Thèmes OnePage Pour Les Agences Marketing

J’espère que cela vous aidera, mais si les étapes ci-dessus n’ont pas apporté de solution à votre problème actuel, je vous recommande de consulter cet article du service d’assistance aux webmasters de Google sur la fonction &#8220;noindex&#8221; pour en savoir plus.
Une partie évidente, mais cruciale, du référencement consiste à faire apparaître votre site dans les résultats de recherche. Pour ce faire, vous devez vous assurer que votre site Web peut être exploré et indexé, ce qui signifie supprimer la balise &#8220;noindex&#8221; et débloquer le fichier robots.txt des parties publiques de votre site. Ces paramètres sont essentiels pour réussir, alors faites-vous une faveur et n’ignorez pas les avertissements de la Search Console ou les comportements bizarres, résolvez ces problèmes à l’aide des conseils et des ressources fournis ci-dessus.
👉🏼  Lecture complémentaire :  Comment faire un SEO audit en 8 étapes ? La Checklist Ultime 2022
👉🏼  Ressources :
- Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?
- Avis du thème Avada 💥 | Le produit le plus puissant de tous les temps
- Comment créer facilement un formulaire de demande de bénévolat dans WordPress
- Comment utiliser le générateur de type de schéma personnalisé gratuit de SmartCrawl
- Comment changer les polices dans votre thème WordPress (5 façons simples)

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- débloquer Robots.txt
- index
- noindex
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

Article précédentSushiswap Vs. Uniswap : Quelles sont les différences ?

Article suivantQu’est-ce que le GPT-3 ? Tout ce que vous devez savoir

Sébastian Magni @ Responsable du contenu

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Avis du thème Avada 💥 | Le produit le plus puissant de tous les temps

### Comment créer facilement un formulaire de demande de bénévolat dans WordPress

### Comment utiliser le générateur de type de schéma personnalisé gratuit de SmartCrawl

### Comment changer les polices dans votre thème WordPress (5 façons simples)

### Le guide ultime pour sécuriser votre connexion WordPress (gratuitement !) avec l’authentification Web

### Sauvegardes d’hébergement horaires de niveau entreprise (seulement 5 $/mois !)

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

### Avis du thème Avada 💥 | Le produit le plus puissant...

Sébastian Magni @ Responsable du contenu -                 15 septembre 2022                0

Avis du thème Avada | Le produit le plus puissant de tous les tempsAujourd'hui, dans cet examen du thème Avada pour , nous allons...

### Comment créer facilement un formulaire de demande de bénévolat dans WordPress

1 août 2022

### Comment utiliser le générateur de type de schéma personnalisé gratuit de...

30 juillet 2022

### Comment changer les polices dans votre thème WordPress (5 façons simples)

26 juillet 2022

### Le guide ultime pour sécuriser votre connexion WordPress (gratuitement !) avec...

24 juillet 2022

#### Articles récents
-
Application Mspy &#8211; L’application de Localisation la plus dominante pour les parents
-
Les 5 meilleurs raccourcisseurs d’URL pour le marketing des médias sociaux
-
Marketing de contenu : Comment créer et diffuser un contenu de qualité
-
Qu’est-ce qu’ActiveCampaign ? Avis des logiciels d’automatisation du marketing [2023]
-
Comment Obtenir un Emploi Grâce à Linkedin : Le Guide Complet
-
Quel casino offre un bonus de bienvenue ?
-
Casino en ligne : Comment en choisir un fiable ?