---
title: "Comment trouver et corriger les erreurs d&#039;indexation à l&#039;aide de la Console Google Search"
permalink: "/comment-trouver-et-corriger-les-erreurs-dindexation-a-laide-de-la-console-google-search/"
date: "2022-04-25T08:00:00+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "Qu&#039;est-ce que le rapport de couverture d&#039;index ?Le rapport de couverture d&#039;index est disponible dans la console de recherche Google et vous indique quelles"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/04/gg.jpg"
source_capture: "20220511124627"
method: "regex"
---
Accueil  Google  Comment trouver et corriger les erreurs d’indexation à l’aide de la Console...

- Google
- SEO

# Comment trouver et corriger les erreurs d’indexation à l’aide de la Console Google Search
Un tutoriel étape par étape sur la correction des erreurs d'indexation à l'aide du rapport de couverture d'index de Google Search Console et de l'outil d'inspection d'URL.

25 avril 202269
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

Table Des Mati&egrave;res
- 1 Qu’est-ce que le rapport de couverture d’index ?
- 2 Comment corriger les erreurs du rapport sur la couverture de l’indice
- 3 Comment corriger les erreurs &#8220;Submitted URL not found (404)&#8221; (URL non trouvée)
- 4 Comment corriger une erreur de serveur (5xx)
- 5 Comment corriger les erreurs de redirection
- 6 Comment corriger les erreurs &#8220;Submitted URL seems to be a soft 404&#8221; (L’URL soumise semble être une erreur 404)
- 7 Comment corriger l’erreur &#8220;URL soumise marquée &#8216;noindex'&#8221; ?
- 8 Comment corriger l’erreur &#8220;URL soumise bloquée par robots.txt&#8221; ?
- 9 Comment corriger l’erreur &#8220;L’URL soumise renvoie une requête non autorisée (401)
- 10 Comment utiliser l’outil d’inspection des URL
- 11 Comment soumettre à nouveau votre site Web à Google
- 12 Comment soumettre à nouveau une page Web à Google ?
- 13 Conclusion

## Qu’est-ce que le rapport de couverture d’index ?
Le rapport de couverture d’index est disponible dans la console de recherche Google et vous indique quelles sont les pages qui ont été indexées avec succès par Google et celles qui n’ont pas été indexées en raison d’une erreur.
Pour chacune des pages, vous pouvez obtenir plus de détails sur l’erreur et vous avez la possibilité de demander à Google de réindexer vos pages Web ou votre site Web dans son ensemble.
Comment trouver des erreurs dans le rapport sur la couverture de l’index ?
Connectez-vous à Google Search Console et sélectionnez votre domaine principal dans la liste déroulante (dans le coin supérieur gauche).
Cliquez sur COVERAGE sous Index pour afficher le rapport de couverture d’index.
Vous remarquerez que la partie supérieure du rapport comporte 4 onglets :
- Erreur
- Valable avec des réchauffements
- Valide
- Exclu
- Puisque notre objectif est d’examiner les éventuelles erreurs d’indexation, nous utiliserons l’onglet ERREUR.
Le processus de dépannage comporte deux parties :
- La première consiste à identifier les erreurs
- La seconde consiste à comprendre les erreurs et à les corriger.
Assurez-vous que seul l’onglet ERREUR est en surbrillance et faites défiler vers le bas jusqu’à la section DÉTAILS.
Vous remarquerez que les erreurs sont regroupées en catégories. Les valeurs possibles sont :
- &#8220;Erreur de serveur (5xx)&#8221;
- &#8220;Erreur de redirection&#8221;
- &#8220;L’URL soumise semble être un soft 404&#8221;
- &#8220;URL soumise marquée &#8216;noindex’ (en anglais)
- &#8220;L’URL soumise est bloquée par robots.txt&#8221;.
- &#8220;L’URL soumise renvoie une requête non autorisée (401)&#8221;
- &#8220;L’URL soumise a un problème de crawl&#8221;
- &#8220;L’URL soumise n’a pas été trouvée (404)&#8221;.
Pour chaque catégorie d’erreur, vous pouvez voir le statut de validation, la tendance et le nombre de pages affectées.
Vous pouvez cliquer sur n’importe quelle ligne pour voir plus de détails sur les pages concernées.

## Comment corriger les erreurs du rapport sur la couverture de l’indice
Maintenant que vous avez appris comment trouver les erreurs, voyons comment les corriger.
Comme mentionné ci-dessus, les erreurs sont regroupées en 8 catégories et selon le type d’erreur, nous pouvons suivre un chemin différent pour la corriger.
Comment corriger les erreurs &#8220;Submitted URL has crawl issue&#8221; (l’URL soumise a un problème d’exploration)
Un problème d’indexation signifie qu’une page a des problèmes et que Google ne peut pas l’indexer. Vous devez déterminer la nature exacte du problème, le résoudre et soumettre à nouveau la page à Google.
- La première étape consiste à cliquer sur le bouton INSPECT URL.
- Cliquez ensuite sur VIEW CRAWLED PAGE et sur MORE INFO dans le menu de droite.

L’une des raisons les plus courantes pour lesquelles une page peut présenter des problèmes d’indexation est que certaines des ressources de la page (images, CSS, JavaScript) n’ont pas pu être chargées lorsque Google a essayé d’indexer la page.
👉🏼 Lecture complémentaire :  Google EAT : Comment améliorer votre référencement On-Page SEO

Avant d’approfondir la question, vous devez :
- Ouvrir une nouvelle fenêtre de navigateur et visiter la page. Si elle se charge correctement, il est fort probable que les erreurs étaient temporaires.
- Cliquez sur le bouton TEST LIVE URL pour forcer Google à rafraîchir le rapport d’erreur.
- Vérifiez à nouveau les détails dans la section PLUS D’INFO.
- Cliquez sur le bouton REQUEST INDEXING pour soumettre à nouveau la page à Google.
Retournez au rapport de couverture d’index et à la page qui présente des problèmes et cliquez sur le bouton VALIDER LA CORRECTION.
Google vous informera par courrier électronique des résultats de votre demande d’indexation.
Si vous obtenez toujours des erreurs ou des ressources non trouvées après avoir cliqué sur le bouton TEST LIVE URL, vous devez d’abord corriger les erreurs en modifiant votre code HTML, puis demander l’indexation et valider la correction.
👉🏼  Lecture complémentaire :  Comment identifier et éliminer la cannibalisation des mots-clés pour améliorer votre référencement

## Comment corriger les erreurs &#8220;Submitted URL not found (404)&#8221; (URL non trouvée)
Ce type d’erreur est facile à corriger. Cela signifie qu’une page n’a pas pu être trouvée par le robot Google au moment de l’indexation.
Dans la plupart des cas, il peut s’agir d’une fausse alerte. La première chose à faire est donc de vérifier que la page est bien introuvable.
Cliquez sur une page de la liste, puis sur le bouton INSPECT URL.
En attendant de recevoir les données de Google Index, ouvrez une nouvelle fenêtre du navigateur et tapez l’URL.
Si la page est trouvée sur votre site web et que vous voulez l’ajouter à l’index Google, alors :
- Cliquez sur le bouton TEST LIVE URL.
- Cliquez sur le bouton DEMANDER L’INDEXATION.
- Retournez au rapport et cliquez sur VALIDER LA FIXATION.
S’il s’agit d’une page qui renvoie effectivement un code 404 et que vous ne voulez pas que Google l’indexe, vous avez deux possibilités :
Premièrement, la laisser telle quelle. Google va progressivement retirer la page de l’index. Ce phénomène est normal et attendu pour les pages qui ne sont plus valables ou qui sont supprimées pour une raison valable.
👉🏼  Lecture complémentaire :  Qu’est-ce que le contenu léger ? Comprendre la pénalité pour contenu léger et le référencement de Google

## Comment corriger une erreur de serveur (5xx)
Les pages répertoriées ici n’ont pas pu être consultées par le robot Google, soit parce que le serveur était en panne, soit parce qu’il n’était pas disponible pour le moment.
Normalement, aucune erreur de serveur ne devrait être signalée. Si vous avez BEAUCOUP d’erreurs, cela signifie que votre serveur a des problèmes et que vous devez chercher à en savoir plus.
Si vous avez quelques erreurs, il est fort probable que la page ne soit pas accessible temporairement, ce qui signifie que vous pouvez demander à Google de réindexer la page.
Suivez cette procédure :
Cliquez sur l’une des pages concernées et vous obtiendrez un menu avec des options sur la droite.

Tout d’abord, cliquez sur INSPECT URL. Google vous donnera plus de détails sur les erreurs de l’index Google.
L’URL n’est pas sur Google : erreurs d’indexation
Si vous obtenez le message &#8220;L’URL n’est pas sur Google : erreurs d’indexation&#8221;, cela signifie que Google a soit supprimé l’URL de son index parce qu’il n’a pas pu y accéder, soit qu’elle n’est pas dans son index parce qu’elle n’était pas disponible lors de la première tentative d’exploration.
👉🏼 Lecture complémentaire :  ▷ Comment choisir une bonne agence de référencement experte et fiable

Suivez les étapes suivantes :
Ouvrez une nouvelle fenêtre de navigateur et accédez à l’URL. Si le chargement est correct, retournez au SGC et cliquez sur le bouton TEST LIVE URL.
Google récupérera à nouveau la page et vous donnera plus de détails. S’il s’agit d’une erreur temporaire, vous pouvez cliquer sur le bouton REQUEST INDEXING pour soumettre à nouveau la page à Google.
Si la page ne se charge pas dans le navigateur, vous devez trouver la cause du problème, puis retourner au SGC, cliquer sur le bouton TEST LIVE ULR, puis sur REQUEST INDEXING.
Si vous ne parvenez pas à résoudre le problème, pensez à ajouter une balise d’en-tête &#8220;noindex&#8221; à la page et à la supprimer de votre sitemap. Cela permettra à Google de ne plus accéder à la page et de ne plus signaler d’erreurs liées à cette page.

## Comment corriger les erreurs de redirection
Lorsque vous obtenez une &#8220;erreur de redirection&#8221;, cela signifie que le robot Google n’a pas pu accéder à la page parce qu’elle redirige vers une page qui n’existe pas ou qui ne fonctionne pas.
La procédure pour corriger les erreurs de redirection est la même que précédemment.
- Cliquez sur l’URL d’INSPECTION
- Obtenez plus de détails sur les erreurs
- Cliquez sur l’URL TEST LIVE
- Corrigez l’erreur et DEMANDEZ L’INDEXATION
- Revenez en arrière et cliquez sur VALIDER LA CORRECTION
Si tout est correct et que l’erreur est corrigée, vous verrez un message PASSÉ dans la colonne de validation.

## Comment corriger les erreurs &#8220;Submitted URL seems to be a soft 404&#8221; (L’URL soumise semble être une erreur 404)
Lorsque vous obtenez une erreur &#8220;soft 404&#8221;, cela signifie que la page n’a pas été trouvée (parce qu’elle n’existe pas) mais qu’au lieu d’indiquer aux moteurs de recherche qu’elle doit être ignorée, elle a renvoyé un code valide.
Vous pouvez avoir des pages sur votre site Web qui ne sont pas accessibles directement, mais seulement après qu’un utilisateur ait effectué une action spécifique.
Par exemple, disons que votre page de paiement n’est affichée aux utilisateurs qu’APRÈS qu’ils aient ajouté un article à leur panier.
Si la page figure toujours dans votre sitemap, Google essaiera de l’explorer, mais il ne la trouvera pas, car aucun article n’a été ajouté au panier.
Que faire en cas d’erreurs 404 molles ?
- Vous devez soit renvoyer un code 404 pour les pages qui ne sont pas valides.
- les supprimer de votre sitemap afin que Google ne puisse pas y accéder
- les rediriger vers une page valide
- Ne rien faire. Parfois, les erreurs &#8221; soft 404 &#8221; sont normales et attendues.
👉🏼  Lecture complémentaire :  Qu’est-ce qu’un Featured Snippet ? [Définition + Exemples]

## Comment corriger l’erreur &#8220;URL soumise marquée &#8216;noindex'&#8221; ?
Il ne s’agit pas vraiment d’une erreur. Cela signifie qu’une page a été soumise à l’indexation (par le biais de votre sitemap), mais qu’elle comporte la directive &#8220;noindex&#8221;, qui indique aux moteurs de recherche de ne pas l’ajouter à leur index.
Il convient de vérifier la liste des pages dotées de la balise &#8220;noindex&#8221; et de s’assurer qu’elles ne doivent pas figurer dans l’index de Google.
Si une page a été étiquetée à tort comme &#8220;noindex&#8221;, supprimez la directive de page de l’en-tête et DEMANDEZ L’INDEXATION.

## Comment corriger l’erreur &#8220;URL soumise bloquée par robots.txt&#8221; ?
Une page a été soumise pour être indexée (par le biais de votre sitemap) mais une règle dans votre fichier robots.txt indique aux moteurs de recherche de ne pas l’indexer.
👉🏼 Lecture complémentaire :  5 conseils pour faire vivre votre agence de référencement et obtenir plus de clients en SEO

Vous devez suivre la même procédure que ci-dessus, c’est-à-dire vérifier si les pages sont censées être bloquées dans l’index de Google.

## Comment corriger l’erreur &#8220;L’URL soumise renvoie une requête non autorisée (401)
Une page est incluse dans votre sitemap, mais Google ne peut y accéder car elle est protégée par un mot de passe.
Comme ces pages ne sont pas accessibles au public, vous devez :
- les supprimer de votre sitemap
- Ajouter une directive &#8220;noindex&#8221; dans l’en-tête de la page.
- bloquer le répertoire (ou les zones protégées) dans votre fichier robots.txt.

## Comment utiliser l’outil d’inspection des URL
L’outil d’inspection des URL vous permet de vérifier le statut d’indexation de n’importe quelle page de votre site Web, de résoudre les erreurs ou de demander à Google de réindexer votre site Web ou une page particulière.
Pour utiliser l’outil d’inspection des URL, il suffit de taper n’importe quelle URL dans le menu déroulant INSPECT ANY URL situé en haut de la page.
Vous pouvez saisir le domaine de votre site Web ou une URL spécifique.
L’OUTIL D’INSPECTION D’URL peut être utilisé pour résoudre les erreurs signalées dans le RAPPORT DE COUVERTURE D’INDEX (comme expliqué ci-dessus) ou pour :
- Soumettre à nouveau votre site Web à Google.
- Soumettre à nouveau une page particulière à Google.

## Comment soumettre à nouveau votre site Web à Google
Lorsque vous apportez un certain nombre de modifications à votre site Web et que vous souhaitez accélérer le processus d’indexation, vous pouvez demander à Google de réindexer votre site Web.
Saisissez votre domaine dans l’OUTIL D’INSPECTION D’URL.
Cliquez sur REQUEST INDEXING.

## Comment soumettre à nouveau une page Web à Google ?
Si le contenu d’une page a considérablement changé et que vous souhaitez informer Google de ces modifications, vous pouvez utiliser l’outil INSPECTION D’URL et le bouton DEMANDER L’INDEXATION pour accélérer le processus.
Le processus est le même que celui qui consiste à soumettre à nouveau votre site Web (expliqué ci-dessus).
Quand utiliser la fonction REQUEST INDEXING ?
Google détecte très bien les modifications apportées à un site ou à une page Web. Dans la majorité des cas, il n’est donc pas nécessaire d’utiliser la fonction &#8220;Demander l’indexation&#8221;.
Voici quelques utilisations valables :
- Lorsque vous migrez des domaines
- Lorsque vous passez de http à https
- lors de la refonte d’un site Web
- Lorsque vous publiez des informations urgentes et que vous souhaitez en informer Google

## Conclusion
Ne paniquez pas lorsque vous voyez des erreurs dans votre compte Google Search Console. Dans de nombreux cas, les erreurs sont valides et attendues.
Votre priorité est de résoudre les erreurs CRAW ISSUES ou NOT FOUND (404) car ce sont les erreurs directement liées à vos classements.
À Lire Aussi  :
- Mercury In Retrograde apportera-t-il un changement d’humeur dans Bitcoin?
- Twitter clarifie la politique de contenu dupliqué
- Azuki Creator in Hot Water Amidst Rug Pull Allégations : voici les faits
- Les détenteurs de Bitcoin à long terme commencent à capituler au milieu de la panique
- KuCoin obtient un financement de 150 millions de dollars et dépasse les 10 milliards de dollars d’évaluation

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- Console Google Search
- corriger les erreurs d'indexation
- erreurs d'indexation
- indexation

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Article précédentQu’est-ce que le Spam Score et à quoi sert-il ?

Article suivant▷ 6 Présentation PowerPoint Metaverse  &#8211;   Metaverse Powerpoint

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Qu’est-ce que le Spam Score et à quoi sert-il ?

### Qu’est-ce que le black hat SEO et pourquoi l’éviter ?

### Qu’est-ce que le Off-Page SEO ? Un guide complet

### 20 façons d’obtenir du trafic et de promouvoir votre blogue

### Les meilleurs outils de référencement qui aident à améliorer le classement des moteurs de recherché

### Qu’est-ce que le On-Page SEO ? (et comment le faire)

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
Mercury In Retrograde apportera-t-il un changement d’humeur dans Bitcoin?
-
Twitter clarifie la politique de contenu dupliqué
-
Azuki Creator in Hot Water Amidst Rug Pull Allégations : voici les faits
-
Les détenteurs de Bitcoin à long terme commencent à capituler au milieu de la panique
-
KuCoin obtient un financement de 150 millions de dollars et dépasse les 10 milliards de dollars d’évaluation
-
La 16ème machine à sous Parachain de Polkadot est sécurisée lors d’un tour Crowdloan
-
Les crashs de crypto nettoient l’air pour les NFT