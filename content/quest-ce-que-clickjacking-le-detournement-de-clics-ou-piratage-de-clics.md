---
title: "Qu’est-ce que Clickjacking ? le Détournement de clics ou piratage de clics"
permalink: "/quest-ce-que-clickjacking-le-detournement-de-clics-ou-piratage-de-clics/"
legacy_permalinks: []
type: "post"
date: "2021-11-23T12:36:36+00:00"
modified: ""
author: "Soléne Laupez Rédactrice de contenu réseaux sociaux"
categories: ["Meilleur du Web"]
tags: ["Clickjacking","Détournement de clics","piratage de clics","piratage informatique"]
description: "Le \"clickjacking\" est une attaque qui consiste à inciter l'utilisateur à cliquer sur un élément de la page web qui est invisible ou déguisé"
cover: "https://leconceptmarketing.com/wp-content/uploads/2021/11/dd-1.jpg"
source_url: "https://leconceptmarketing.com/quest-ce-que-clickjacking-le-detournement-de-clics-ou-piratage-de-clics/"
source_capture: "20211126134535"
---
Le “clickjacking” (Détournement de clics ou encore ou piratage de clics ) est une attaque qui consiste à inciter l’utilisateur à cliquer sur un élément de la page web qui est invisible ou déguisé en un autre élément.

Les utilisateurs peuvent ainsi télécharger involontairement des logiciels malveillants, visiter des pages Web malveillantes, fournir des informations d’identification ou des informations sensibles, transférer de l’argent ou acheter des produits en ligne.

![Qu'est-ce que Clickjacking ? le Détournement de clics ou piratage de clics](https://avatars.mds.yandex.net/i?id=ca167cb8142b756004d5f4dd34a9f28e-5220059-images-thumbs&n=13&exp=1)

[Le clickjacking](https://fr.wikipedia.org/wiki/D%C3%A9tournement_de_clic#:~:text=Le%20d%C3%A9tournement%20de%20clic%2C%20ou,sur%20des%20pages%20apparemment%20s%C3%BBres.) consiste généralement à afficher une page ou un élément HTML invisible, dans une iframe, au-dessus de la page que l’utilisateur voit. L’utilisateur croit qu’il clique sur la page visible, mais en fait, il clique sur un élément invisible de la page supplémentaire transposée au-dessus de celle-ci.

La page invisible peut être une page malveillante ou une page légitime que l’utilisateur n’avait pas l’intention de visiter – par exemple, une page du site bancaire de l’utilisateur qui autorise le transfert d’argent.

**Il existe plusieurs variantes de l’attaque par clickjacking, telles que :**

- **Likejacking** – une technique dans laquelle le bouton “Like” de Facebook est manipulé, amenant les utilisateurs à “aimer” une page qu’ils n’avaient en fait pas l’intention d’aimer.
- **Cursorjacking** – une technique de redressement de l’interface utilisateur qui change le curseur de la position perçue par l’utilisateur à une autre position. Le cursorjacking s’appuie sur des vulnérabilités dans Flash et le navigateur Firefox, qui ont maintenant été corrigées.

- 1 Exemple d’attaque de clickjacking :
- 2 Atténuation du clickjacking :
  - 2.1 Les méthodes côté client :
  - 2.2 Méthodes côté serveur :
- 3 Atténuation du clickjacking avec l’en-tête de réponse X-Frame-Options
- 4 Utilisation de l’option SAMEORIGIN pour se défendre contre le clickjacking
- 5 Limites de X-Frame-Options

## Exemple d’attaque de clickjacking :

1. L’attaquant crée une page attrayante qui promet à l’utilisateur un voyage gratuit à Tahiti.

2. En arrière-plan, l’attaquant vérifie si l’utilisateur est connecté à son site bancaire et, si c’est le cas, charge l’écran qui permet le transfert de fonds, en utilisant des paramètres de requête pour insérer les coordonnées bancaires de l’attaquant dans le formulaire.

3. La page de transfert bancaire est affichée dans une iframe invisible au-dessus de la page de cadeaux gratuits, le bouton “Confirmer le transfert” étant exactement aligné sur le bouton “Recevoir le cadeau” visible par l’utilisateur.
L’utilisateur visite la page et clique sur le bouton “Réserver mon voyage gratuit”.

4. En réalité, l’utilisateur clique sur la iframe invisible, et a cliqué sur le bouton “Confirmer le transfert”. Les fonds sont transférés à l’attaquant.

5. L’utilisateur est redirigé vers une page contenant des informations sur le cadeau gratuit (sans savoir ce qui s’est passé en arrière-plan).

## Atténuation du clickjacking :

Il existe deux façons générales de se défendre contre le clickjacking :

### **Les méthodes côté client** :

La plus courante est appelée Frame Busting. Les méthodes côté client peuvent être efficaces dans certains cas, mais ne sont pas considérées comme une bonne pratique, car elles peuvent être facilement contournées.

### **Méthodes côté serveur** :

La plus courante est X-Frame-Options. Les méthodes côté serveur sont recommandées par les experts en sécurité comme un moyen efficace de se défendre contre le [clickjacking](https://fr.wikipedia.org/wiki/D%C3%A9tournement_de_clic#:~:text=Le%20d%C3%A9tournement%20de%20clic%2C%20ou,sur%20des%20pages%20apparemment%20s%C3%BBres.).

## Atténuation du clickjacking avec l’en-tête de réponse X-Frame-Options

L’en-tête de réponse X-Frame-Options est transmis dans le cadre de la réponse HTTP d’une page Web, indiquant si le navigateur doit être autorisé ou non à rendre une page à l’intérieur d’une balise <FRAME> ou <IFRAME>.

Trois valeurs sont autorisées pour l’en-tête X-Frame-Options :

**DENY** – n’autorise aucun domaine à afficher cette page dans un cadre
**SAMEORIGIN** – permet d’afficher la page actuelle dans un cadre sur une autre page, mais uniquement dans le domaine actuel.
**ALLOW-FROM URI** – permet à la page actuelle d’être affichée dans un cadre, mais seulement dans un URI spécifique – par exemple www.example.com/frame-page.

## Utilisation de l’option SAMEORIGIN pour se défendre contre le clickjacking

L’option X-Frame-Options permet aux éditeurs de contenu d’empêcher que leur propre contenu soit utilisé dans un cadre invisible par des attaquants.

L’option DENY est la plus sûre, car elle empêche toute utilisation de la page actuelle dans un cadre. Plus souvent, l’option SAMEORIGIN est utilisée, car elle permet l’utilisation de cadres, mais les limite au domaine actuel.

## Limites de X-Frame-Options

-Pour activer l’option SAMEORIGIN sur un site Web, l’en-tête X-Frame-Options doit être renvoyé dans le cadre de la réponse HTTP pour chaque page individuelle (ne peut pas être appliqué entre sites).

-X-Frame-Options ne prend pas en charge une liste blanche des domaines autorisés, et ne fonctionne donc pas avec les sites multi-domaines qui doivent afficher du contenu encadré entre eux.

-Une seule option peut être utilisée sur une même page. Il n’est donc pas possible, par exemple, d’afficher la même page sous forme de cadre à la fois sur le site Web actuel et sur un site externe.

-L’option ALLOW-FROM n’est pas prise en charge par tous les navigateurs.

-X-Frame-Options est une option dépréciée dans la plupart des navigateurs.

Lire aussi :
