---
title: "OBJ Box et texte bleu première moitié H1 d’un post WordPress"
permalink: "/obj-box-et-texte-bleu-premiere-moitie-h1-dun-post-wordpress/"
legacy_permalinks: []
type: "post"
date: "2022-02-09T08:03:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Thèmes","WordPress"]
tags: ["éditeur Wordpress","Erreur wordpress","H1","OBJ Box","post WordPress","texte bleu","URL ERREUR"]
description: "Erreur wordpress : J'écris généralement mes articles dans MS Word, puis je les coupe et les colle dans l'éditeur Wordpress. Dernièrement"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/02/FG.png"
source_url: "https://leconceptmarketing.com/obj-box-et-texte-bleu-premiere-moitie-h1-dun-post-wordpress/"
source_capture: "20220521215646"
---
**Erreur wordpress** : J’écris généralement mes articles dans MS Word, puis je les coupe et les colle dans l’éditeur WordPress. Dernièrement, lorsque je crée un nouvel article sur mon blog, le titre et l’URL se terminent par une boîte OBJ à la fin. Comment faire pour que cela ne se produise pas ?

![WordPress: what is it, how can you use it, and the main secrets](https://rockcontent.com/wp-content/uploads/2021/02/stage-en-wordpress.png)

Cela peut se produire en copiant le texte de MS Word. Les programmes de traitement de texte comme MS Word ont beaucoup plus de “code” en arrière-plan que les éditeurs d’un site Web (comme l’éditeur [WordPress.com)](https://wordpress.com/fr/). Ainsi, lorsque vous copiez du texte à partir de MS Word et que vous le collez, ce code indésirable est reporté, ce qui casse parfois la mise en forme.

Une solution de contournement consiste à vous assurer que vous le collez en texte brut. Si vous êtes sur Google Chrome, le raccourci “CMD + Maj + V” collera le texte source sans aucun type de formatage ou de code indésirable ajouté par MS Word. Je recommande de coller le texte de cette façon pour voir si cela se passe pour vous.

En ce qui concerne votre dernier message, je vois qu’il y a une balise dans le HTML qui est à l’origine du problème. Si vous ouvrez l’article dans l’éditeur → cliquez sur les trois points dans le coin supérieur droit → Cliquez sur Éditeur de code, vous verrez l’intégralité de l’article en HTML. Dans le HTML, vous remarquerez une balise et une balise dans le premier paragraphe. Veuillez les supprimer, cliquez sur “Modifier l’éditeur de code” en haut, puis cliquez sur “Mettre à jour”.

Cela supprimera la balise HTML indésirable du premier paragraphe et elle ne sera plus en bleu.

**À Lire Aussi :**
