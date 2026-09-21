---
title: "Comment débloquer Robots.txt et supprimer &quot; noindex &quot; sur WordPress ?"
permalink: "/comment-debloquer-robots-txt-et-supprimer-noindex-sur-wordpress/"
date: "2022-01-02T07:01:00+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "Vous avez du mal à faire en sorte que votre site Web WordPress soit crawlé ou indexé dans les recherches ? Lorsque vous vous connectez à la Search Console d"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/01/rt.jpg"
source_capture: "20220129002935"
method: "regex"
---
Accueil  Thémes  Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?

- Thémes
- Wordpress

# Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ?

2 janvier 2022285
1

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Vous avez du mal à faire en sorte que votre site Web WordPress soit crawlé ou indexé dans les recherches ? Lorsque vous vous connectez à la Search Console de Google et demandez l’indexation, vous recevez toutes sortes de messages d’erreur concernant les balises robots.txt et/ou les balises méta &#8220;noindex&#8221; ? Si c’est le cas, vous êtes au bon endroit. Dans cet article de blog, je vais vous expliquer ces deux problèmes courants et comment les résoudre.

Table Des Mati&egrave;res
- 1 Dépannage des problèmes d’index et de crawl : Par où commencer ?
- 2 Problème n°1 : Domaine ou URL bloqué par Robots.txt
- 3 Problème n° 2 : Supprimez la balise Meta &#8221; noindex &#8221; dans WordPress

## Dépannage des problèmes d’index et de crawl : Par où commencer ?
Tout d’abord, essayons de circonscrire le problème. Pour ce faire, connectez-vous à Google Search Console. Ensuite, copiez et collez l’URL de la page d’accueil de votre site Web dans le testeur robots.txt et cliquez sur Envoyer. (Pour l’instant, cet outil n’existe que dans l’ancienne version de Google Search Console).
Si l’URL est &#8220;BLOQUÉE&#8221;, reportez-vous au problème n° 1, si elle est &#8220;AUTORISÉE&#8221;, reportez-vous au problème n° 2 ci-dessous.

## Problème n°1 : Domaine ou URL bloqué par Robots.txt
Si la ligne disallow s’allume en rouge et que vous voyez le mot &#8220;BLOCKED&#8221; apparaître dans la case en bas à droite comme dans la capture d’écran ci-dessous, le fichier robots.txt est le coupable. Pour remédier à ce problème, vous devez pouvoir accéder au fichier robots.txt de votre site Web et le modifier*.
*Si vous n’êtes pas une personne qui joue habituellement dans l’arrière-plan de votre site Web, je vous encourage vivement à contacter votre développeur de site Web, votre informaticien ou la personne chargée de la maintenance du site.
Dans l’exemple ci-dessus, il y a deux choses qui se passent, l’une bonne et l’autre mauvaise en fonction de notre situation actuelle.
Cette URL, /wp-admin/, est volontairement interdite car nous ne souhaitons pas que la partie arrière de notre site soit explorée par les moteurs de recherche. Cela doit rester.
Cependant, la ligne Disallow : / est celle qui pose problème. Cette ligne, ou plutôt cette barre oblique, empêche tous les moteurs de recherche d’explorer votre site Web… en entier. Pour débloquer le fichier robots.txt, il faut donc supprimer cette partie du fichier robots.txt.
Il suffit littéralement d’un seul caractère pour mettre le feu aux poudres.
Une fois que la modification nécessaire a été apportée au fichier, remettez l’URL de la page d’accueil dans le testeur de robots.txt pour vérifier si votre site accueille désormais les moteurs de recherche.
Si tout va bien, la case en bas à droite indiquera &#8220;ALLOWED&#8221; en vert et les moteurs de recherche pourront désormais commencer à explorer le site.
Cette correction, devrait permettre de débloquer le fichier robots.txt pour l’ensemble du site (ou du moins pour toutes les pages qui ne sont pas spécifiquement désignées comme interdites, comme l’URL /wp-admin/ ci-dessus).
Mais n’hésitez pas à copier et coller quelques pages, supplémentaires, dans l’outil de test pour vous assurer que le problème n’est pas uniquement résolu pour votre page d’accueil.

## Problème n° 2 : Supprimez la balise Meta &#8221; noindex &#8221; dans WordPress

Si le problème ci-dessus n’est pas celui de votre site Web, c’est-à-dire que tout est &#8220;AUTORISÉ&#8221; (comme il se doit), il existe une autre raison courante pour laquelle votre site Web WordPress n’apparaît pas dans les résultats de recherche : la balise &#8220;noindex&#8221;.
Pour voir si c’est le cas, revenez à la nouvelle version de Search Console et collez n’importe quelle URL dans le champ de recherche &#8220;Inspecter n’importe quelle URL dans…&#8221; en haut de la page et appuyez sur la touche Entrée.
Si le rapport d’inspection d’URL affiche le message suivant : No : &#8216;noindex’ detected in &#8216;robots’ meta tag, c’est un simple paramètre de case à cocher dans l’arrière-plan de WordPress qui est à l’origine de toute cette agitation.
Pour empêcher les moteurs de recherche d’indexer votre site Web, procédez comme suit :
- Connectez-vous à WordPress
- Allez dans Réglages → Lecture
- Faites défiler la page jusqu’à l’endroit où il est indiqué &#8220;Visibilité des moteurs de recherche&#8221;.
- Décochez la case à côté de &#8220;Décourager les moteurs de recherche d’indexer ce site&#8221;.
- Appuyez sur le bouton &#8220;Enregistrer les modifications&#8221; ci-dessous
Si vous utilisez le plugin Yoast SEO &#8211; WordPress, vérifiez également les paramètres des articles de blog pour vous assurer qu’ils sont réglés de manière similaire pour permettre l’indexation.
Une fois cette opération terminée, retournez dans Search Console et soumettez à nouveau l’URL que vous avez essayée précédemment. Si vos paramètres sont configurés correctement, tout devrait être différent.
Désormais, lorsque vous soumettez une URL, le rapport d’inspection de l’URL devrait être dépourvu de tous les avertissements et messages d’erreur, du moins ceux liés à l’indexation et à la facilité d’exploration, et vous serez en mesure de &#8220;demander l’indexation&#8221;, ce qui, j’imagine, était votre objectif depuis le début.
J’espère que cela vous aidera, mais si les étapes ci-dessus n’ont pas apporté de solution à votre dilemme actuel, je vous recommande de consulter cet article du service d’assistance aux webmasters de Google sur la fonction &#8220;noindex&#8221; pour en savoir plus.
Une partie évidente, mais cruciale, du référencement consiste à faire apparaître votre site dans les résultats de recherche.
Pour ce faire, vous devez vous assurer que votre site Web peut être exploré et indexé, ce qui signifie supprimer la balise &#8220;noindex&#8221; et débloquer le fichier robots.txt des parties publiques de votre site. Ces paramètres sont essentiels pour réussir, alors faites-vous une faveur et n’ignorez pas les avertissements de la Search Console ou les comportements bizarres, résolvez ces problèmes à l’aide des conseils et des ressources fournis ci-dessus.
Si vous cherchez à vous introduire dans (La création des supports numériques et des ressources pour votre nouveau site web) . Nous vous suggérons d’utiliser : ▷ EnvatoElements
Si vous cherchez à vous introduire dans (Le référencement naturel et SEO) . Nous vous suggérons de consulter : ▷ SEO : Référencement Naturel pour les Débutants (Guide complet de A à Z)
Si vous cherchez à vous introduire dans (Le référencement et SEO) . Nous vous suggérons de consulter :  ▷  Comment rédiger un contenu adapté au référencement (du débutant au SEO avancé)
À lire aussi :
- Que sont les SERP et pourquoi sont-elles importantes pour le référencement SEO
- Qu’est-ce qu’un flux RSS ? Comment fonctionnent un fil RSS ?
- Comment faire un SEO audit en 8 étapes ? La Checklist Ultime 2022
- 6 conseils d’experts pour la stratégie SEO des petites entreprises en 2022
- Quelle plateforme de netlinking pour acheter des liens en 2022 ?

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- index follow
- meta no index
- meta robots
- noindex
- robot txt no index
- robots txt
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

Article précédentQu’est-ce que le contenu léger ? Comprendre la pénalité pour contenu léger et le référencement de Google

Article suivantComment créer une cryptomonnaie [Guide  complet ] | LCM.com

#### ARTICLES CONNEXESDU MÊME AUTEUR

### 4 étapes incontournables pour créer un site web WordPress performant  en 2022

### Comment réparer l’erreur 404 des articles de WordPress ?

### Comment utiliser l’application WordPress sur votre Smartphone

### Comment intégrer Google Maps sur votre site web WordPress ?

### 10 conseils WordPress pour sécuriser votre site web

### Placeit : créez des logos, des vidéos et des designs en quelques secondes

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

1 Commentaire

Le plus ancien

Le plus récent
Le plus populaire

 Commentaires en ligne
Afficher tous les commentaires

10 conseils WordPress pour sécuriser votre site web - Le Concept Marketing

17 jours il y a

[…] Comment débloquer Robots.txt et supprimer &#8221; noindex &#8221; sur WordPress ? […]

0

Répondre

Rejoignez l'élite des experts d'internet

Bénéficiez de conseils, des documents exclusifs et  des informations non divulguées...

Nous respectons votre vie privée.

#### Ne Manquez Pas

### Comment savoir si votre Site Web à été piraté ? 7...

Sébastian Magni @ Responsable du contenu -                 28 janvier 20220

Voici des signes simples indiquant qu'un site Web a été piraté. Vous n'avez pas besoin d'engager un expert en sécurité pour les...

### Qu’est-ce que le data marketing  ? Pourquoi c’est important et...

27 janvier 2022

### Binance vs eToro, Qui est le meilleur courtier en ligne ?

27 janvier 2022

### Qu’est-ce qu’eToro ? Comment fonctionne le trading en ligne Etoro ?

26 janvier 2022

### 3 types de CRM et comment choisir le meilleur pour votre...

26 janvier 2022

#### Articles récents
-
Comment savoir si votre Site Web à été piraté ? 7 signes
-
Qu’est-ce que le data marketing  ? Pourquoi c’est important et comment le faire correctement
-
Binance vs eToro, Qui est le meilleur courtier en ligne ?
-
Qu’est-ce qu’eToro ? Comment fonctionne le trading en ligne Etoro ?
-
3 types de CRM et comment choisir le meilleur pour votre entreprise
-
18 meilleurs logiciels d’édition vidéo gratuits pour les spécialistes du marketing
-
Top 5 des meilleurs logiciels de facturation les plus populaires