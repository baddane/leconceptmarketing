---
title: "Comment débloquer Robots.txt et supprimer ” noindex ” sur WordPress ?"
permalink: "/comment-debloquer-robots-txt-et-supprimer-noindex-sur-wordpress/"
legacy_permalinks: []
type: "post"
date: "2022-01-02T08:01:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Thèmes","WordPress"]
tags: ["index follow","meta no index","meta robots","noindex","robot txt no index","robots txt","wordpress"]
description: "Connectez-vous à Google Search Console. Ensuite, copiez et collez l'URL de la page d'accueil de votre site Web dans le testeur robots.txt et cliquez sur Envoyer"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/01/rt.jpg"
source_url: "https://leconceptmarketing.com/comment-debloquer-robots-txt-et-supprimer-noindex-sur-wordpress/"
source_capture: "20220129002935"
---
Vous avez du mal à faire en sorte que votre site Web WordPress soit crawlé ou indexé dans les recherches ? Lorsque vous vous connectez à la Search Console de Google et demandez **l’indexation**, vous recevez toutes sortes de messages d’erreur concernant les balises robots.txt et/ou les balises méta “noindex” ? Si c’est le cas, vous êtes au bon endroit. Dans cet article de [blog](https://leconceptmarketing.com/comment-creer-un-blog-et-vivre-de-son-blog-a-partir-de-zero-guide-ultime/), je vais vous expliquer ces deux problèmes courants et comment les résoudre.

![Comment débloquer Robots.txt et supprimer " noindex " sur WordPress ?](https://www.iquanti.com/wp-content/uploads/2019/07/Google-open-source-robots.txt-parsing-changes-iQuanti-Digital-Marketing-Company.jpg)

- 1 Dépannage des problèmes d’index et de crawl : Par où commencer ?
- 2 Problème n°1 : Domaine ou URL bloqué par Robots.txt
- 3 Problème n° 2 : Supprimez la balise Meta ” noindex ” dans WordPress

## Dépannage des problèmes d’index et de crawl : Par où commencer ?

Tout d’abord, essayons de circonscrire le problème. Pour ce faire, connectez-vous à **[Google Search Console](https://search.google.com/search-console?hl=fr)**. Ensuite, copiez et collez l’URL de la page d’accueil de votre site Web dans **[le testeur robots.txt](https://www.google.com/webmasters/tools/robots-testing-tool)** et cliquez sur Envoyer. (Pour l’instant, cet outil n’existe que dans l’ancienne version de Google Search Console).

Si l’URL est “BLOQUÉE”, reportez-vous au problème n° 1, si elle est “AUTORISÉE”, reportez-vous au problème n° 2 ci-dessous.

## Problème n°1 : Domaine ou URL bloqué par Robots.txt

Si la ligne disallow s’allume en rouge et que vous voyez le mot “BLOCKED” apparaître dans la case en bas à droite comme dans la capture d’écran ci-dessous, le fichier robots.txt est le coupable. Pour remédier à ce problème, vous devez pouvoir accéder au fichier robots.txt de votre site Web et le modifier\*.

\*Si vous n’êtes pas une personne qui joue habituellement dans l’arrière-plan de votre site Web, je vous encourage vivement à contacter votre développeur de site Web, votre informaticien ou la personne chargée de la maintenance du site.

Dans l’exemple ci-dessus, il y a deux choses qui se passent, l’une bonne et l’autre mauvaise en fonction de notre situation actuelle.

**Cette URL, /wp-admin/, est volontairement interdite car nous ne souhaitons pas que la partie arrière de notre site soit explorée par les moteurs de recherche. Cela doit rester.**

Cependant, la ligne Disallow : / est celle qui pose problème. Cette ligne, ou plutôt cette barre oblique, empêche tous les moteurs de recherche d’explorer votre site Web… en entier. Pour débloquer le fichier robots.txt, il faut donc supprimer cette partie du fichier robots.txt.

Il suffit littéralement d’un seul caractère pour mettre le feu aux poudres.

Une fois que la modification nécessaire a été apportée au fichier, remettez l’URL de la page d’accueil dans le testeur de robots.txt pour vérifier si votre site accueille désormais les moteurs de recherche.

Si tout va bien, la case en bas à droite indiquera “ALLOWED” en vert et les moteurs de recherche pourront désormais commencer à explorer le site.

![](https://leconceptmarketing.com/wp-content/uploads/2021/12/ca.png)

Cette correction, devrait permettre de débloquer le fichier robots.txt pour l’ensemble du site (ou du moins pour toutes les pages qui ne sont pas spécifiquement désignées comme interdites, comme l’URL /wp-admin/ ci-dessus).

Mais n’hésitez pas à copier et coller quelques pages, supplémentaires, dans l’outil de test pour vous assurer que le problème n’est pas uniquement résolu pour votre page d’accueil.

## Problème n° 2 : Supprimez la balise Meta ” noindex ” dans WordPress

Si le problème ci-dessus n’est pas celui de votre site Web, c’est-à-dire que tout est “AUTORISÉ” (comme il se doit), il existe une autre raison courante pour laquelle votre site Web [WordPress](https://leconceptmarketing.com/divi-wordpress-est-il-un-des-meilleurs-themes-test-et-verdict/) n’apparaît pas dans les résultats de recherche : la balise “noindex”.

Pour voir si c’est le cas, revenez à la nouvelle version de Search Console et collez n’importe quelle URL dans le champ de recherche “Inspecter n’importe quelle URL dans…” en haut de la page et appuyez sur la touche Entrée.

Si le rapport d’inspection d’URL affiche le message suivant : No : ‘noindex’ detected in ‘robots’ meta tag, c’est un simple paramètre de case à cocher dans l’arrière-plan de WordPress qui est à l’origine de toute cette agitation.

**Pour empêcher les moteurs de recherche d’indexer votre site Web, procédez comme suit :**

![](https://leconceptmarketing.com/wp-content/uploads/2021/12/tyyy.png)

- **Connectez-vous à WordPress**
- **Allez dans Réglages → Lecture**
- **Faites défiler la page jusqu’à l’endroit où il est indiqué “Visibilité des moteurs de recherche”.**
- **Décochez la case à côté de “Décourager les moteurs de recherche d’indexer ce site”.**
- **Appuyez sur le bouton “Enregistrer les modifications” ci-dessous**

Si vous utilisez le plugin**[ Yoast SEO](https://fr.wordpress.org/plugins/wordpress-seo/)** – WordPress, vérifiez également les paramètres des articles de blog pour vous assurer qu’ils sont réglés de manière similaire pour permettre l’indexation.

Une fois cette opération terminée, retournez dans Search Console et soumettez à nouveau l’URL que vous avez essayée précédemment. Si vos paramètres sont configurés correctement, tout devrait être différent.

Désormais, lorsque vous soumettez une URL, le rapport d’inspection de l’URL devrait être dépourvu de tous les avertissements et messages d’erreur, du moins ceux liés à l’indexation et à la facilité d’exploration, et vous serez en mesure de “demander l’indexation”, ce qui, j’imagine, était votre objectif depuis le début.

**J’espère que cela vous aidera, mais si les étapes ci-dessus n’ont pas apporté de solution à votre dilemme actuel, je vous recommande de consulter cet article du service d’assistance aux webmasters de Google sur la fonction “noindex” pour en savoir plus.**

Une partie évidente, mais cruciale, du[ référencement ](https://leconceptmarketing.com/seo-referencement-naturel-pour-les-debutants-guide-complet-de-a-a-z/)consiste à faire apparaître votre site dans les résultats de recherche.

Pour ce faire, vous devez vous assurer que votre site Web peut être exploré et indexé, ce qui signifie supprimer la balise “noindex” et débloquer le fichier robots.txt des parties publiques de votre site. Ces paramètres sont essentiels pour réussir, alors faites-vous une faveur et n’ignorez pas les avertissements de la Search Console ou les comportements bizarres, résolvez ces problèmes à l’aide des conseils et des ressources fournis ci-dessus.

**Si vous cherchez à vous introduire dans (La création des supports numériques et des ressources pour votre nouveau site web) . Nous vous suggérons d’utiliser : ▷** [EnvatoElements](http://1.envato.market/29mkA)

**Si vous cherchez à vous introduire dans (Le référencement naturel et SEO) . Nous vous suggérons de consulter : ▷** [SEO : Référencement Naturel pour les Débutants (Guide complet de A à Z)](https://leconceptmarketing.com/seo-referencement-naturel-pour-les-debutants-guide-complet-de-a-a-z/)

**Si vous cherchez à vous introduire dans (Le référencement et SEO) . Nous vous suggérons de consulter :**  **▷** [Comment rédiger un contenu adapté au référencement (du débutant au SEO avancé)](https://leconceptmarketing.com/comment-rediger-un-contenu-adapte-au-referencement-du-debutant-au-seo-avance/)

***À lire aussi* :**
