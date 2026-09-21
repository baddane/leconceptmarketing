---
title: "Php Blog : Comment créer un blog en PHP et base de données MySQL"
permalink: "/php-blog-comment-creer-un-blog-en-php-et-base-de-donnees-mysql/"
legacy_permalinks: []
type: "post"
date: "2022-02-02T07:22:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Ressources"]
tags: ["blog php mysql","code source blog php","create blog php","Php Blog","script blog php gratis","simple blog php"]
description: "php blog : - Vous pouvez créer, visualiser, mettre à jour, publier/dépublier et supprimer N'IMPORTE QUEL message. - Il peut également créer"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/02/php.png"
source_url: "https://leconceptmarketing.com/php-blog-comment-creer-un-blog-en-php-et-base-de-donnees-mysql/"
source_capture: "20220929025649"
---
Nous sommes impatient de vous présenter ce tutoriel tant attendu, enfin. Je vais vous montrer comment construire une application de [blog](https://leconceptmarketing.com/comment-creer-un-blog-et-vivre-de-son-blog-a-partir-de-zero-guide-ultime/) complète à partir de zéro en utilisant PHP et la base de données MySQL. Un blog comme vous le savez est une application où certains utilisateurs (utilisateurs Admin) peuvent créer, éditer, mettre à jour et publier des articles pour les rendre disponibles au public afin qu’il puisse les lire et peut-être les commenter. Les utilisateurs et le public peuvent parcourir un catalogue de ces articles et cliquer sur n’importe quel article pour en lire plus et le commenter.

- 1 Caractéristiques
- 2 Créer un blog en PHP et base de données MySQL
  - 2.1 Mise en œuvre :

## Caractéristiques

- Un système d’enregistrement des utilisateurs qui gère deux types d’utilisateurs : Admin et utilisateurs normaux
- Le blog aura une zone d’administration et une zone publique séparées l’une de l’autre.
- La zone d’administration ne sera accessible qu’aux utilisateurs admin connectés et la zone publique aux utilisateurs normaux et au grand public.
- Dans la section admin, il existe **deux types d’admins :**

**Admin :**

- Peut créer, visualiser, mettre à jour, publier/dépublier et supprimer TOUT article.
- Il peut également créer, afficher, mettre à jour et supprimer des sujets.
- Un utilisateur Admin (et seulement un utilisateur Admin) peut créer un autre utilisateur Admin ou un auteur.
- Peut voir, mettre à jour et supprimer d’autres utilisateurs admin

**Auteur :**

- Peut créer, afficher, mettre à jour et supprimer uniquement les messages qu’il a lui-même créés.
- Ils ne peuvent pas publier un article. Toute publication de messages est effectuée par l’utilisateur Admin.

- Seuls les messages publiés sont affichés dans la zone publique pour être consultés.
- Chaque message est créé sous un thème particulier
- Il existe une relation de plusieurs à plusieurs entre les messages et les sujets.
- La page publique liste les messages ; chaque message est affiché avec une image, un auteur et une date de création.
- L’utilisateur peut parcourir toutes les listes de messages d’un sujet particulier en cliquant sur ce sujet.
- Lorsqu’un utilisateur clique sur un message, il peut l’afficher dans son intégralité et le commenter au bas de la page.
- [Un système de commentaires Disqus ](https://www.e-monsite.com/blog/nouveaute/disqus-un-nouveau-systeme-de-gestion-des-commentaires.html)est mis en œuvre, ce qui permet aux utilisateurs de commenter en utilisant des comptes de médias sociaux avec des plateformes comme Facebook, GooglePlus, Twitter.

## Créer un blog en PHP et base de données MySQL

![](https://bizzapps.ru/wp-content/uploads/sites/24/2021/06/1546605744_kJJn8X.png)

### Mise en œuvre :

Ok, tout de suite, commençons à coder.

Nous appellerons le projet complete-blog-php. Dans le répertoire de votre serveur (htdocs ou www), créez un dossier nommé complete-blog-php. Ouvrez ce dossier dans un éditeur de texte de votre choix, par exemple, Sublime Text. Créez les sous-dossiers suivants à l’intérieur : admin, includes et static.

![Php Blog : Comment créer un blog en PHP et base de données MySQL](http://codewithawa.com/assets/post_images/how-to-create-a-complete-blog-application-php-and-mysql-database-1.png.2018-04-15.1523777612.png)

**Les 3 dossiers contiendront les contenus suivants :**

- **admin :** Contient les fichiers de l’interface d’administration. Les fichiers concernant la création, l’affichage, la mise à jour et la suppression des messages, des sujets et des utilisateurs.
- **includes** : Contiendra les fichiers contenant des morceaux de code qui seront inclus dans une ou plusieurs autres pages. Par exemple, les fichiers pour l’affichage des erreurs.
- **static** : contient des fichiers statiques tels que des images, des feuilles de style **CSS, Javascript**.

**Dans le dossier racine de l’application, créez un fichier nommé index.php :**

![Le dossier racine de l'application, créez un fichier nommé index.php :](http://codewithawa.com/assets/post_images/how-to-create-a-complete-blog-application-php-and-mysql-database-2.png.2018-04-15.1523777806.png)

**Ouvrez-le et collez-y ce code :**

```
<!DOCTYPE html>
<html>
<head>
	<!-- Google Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Averia+Serif+Libre|Noto+Serif|Tangerine" rel="stylesheet">
	<!-- Styling for public area -->
	<link rel="stylesheet" href="static/css/public_styling.css">
	<meta charset="UTF-8">
	<title>LifeBlog | Home </title>
</head>
<body>
	<!-- container - wraps whole page -->
	
		<!-- navbar -->
		
			
				<h1>LifeBlog</h1></a>
			</div>
			<ul>
			  <li>Home</a></li>
			  <li>News</a></li>
			  <li>Contact</a></li>
			  <li>About</a></li>
			</ul>
		</div>
		<!-- // navbar -->

		<!-- Page content -->
		
			<h2 class="content-title">Recent Articles</h2>
			<hr>
			<!-- more content still to come here ... -->
		</div>
		<!-- // Page content -->

		<!-- footer -->
		
			MyViewers &copy; <?php echo date('Y'); ?></p>
		</div>
		<!-- // footer -->

	</div>
	<!-- // container -->
</body>
</html>

```

Entre les balises **<head></head>**, nous avons inclus des liens vers certaines polices Google. Il y a aussi un lien vers notre fichier de style public\_styling.css, que nous allons créer dans une minute. Remarquez également l’élément <div> avec une classe définie sur conteneur qui enveloppe toute notre application, y compris la barre de navigation, le contenu de la page et les sections de pied de page de la page.

Pour l’afficher dans votre navigateur, accédez à http://localhost/complete-blog-php/index.php. Ça n’a pas l’air aussi cool que vous l’auriez aimé, n’est-ce pas ? Le dossier statique, comme indiqué précédemment, contiendra, entre autres, le style du site.

Créez 3 sous-dossiers dans le dossier statique : css, images, js. Dans le sous-dossier css que vous venez de créer, créez un fichier nommé public\_styling.css.

![](http://codewithawa.com/assets/post_images/how-to-create-a-complete-blog-application-php-and-mysql-database-3.png.2018-04-15.1523778138.png)

**Ouvrez public\_styling.css et ajoutez-y ce code de style :**

```
/****************
*** DEFAULTS
*****************/
* { margin: 0px; padding: 0px; }

html { height: 100%; box-sizing: border-box; }
body {
  position: relative;
  margin: 0;
  padding-bottom: 6rem;
  min-height: 100%;
}
/* HEADINGS DEFAULT */
h1, h2, h3, h4, h5, h6 { color: #444; font-family: 'Averia Serif Libre', cursive; }
a { text-decoration: none; }
ul, ol { margin-left: 40px; }
hr { margin: 10px 0px; opacity: .25; }

/* FORM DEFAULTS */
form h2 {
	margin: 25px auto;
	text-align: center;
	font-family: 'Averia Serif Libre', cursive;
}
form input {
	width: 100%;
	display: block;
	padding: 13px 13px;
	font-size: 1em;
	margin: 5px auto 10px;
	border-radius: 3px;
	box-sizing : border-box;
	background: transparent;
	border: 1px solid #3E606F;
}
form input:focus {
	outline: none;
}
/* BUTTON DEFAULT */
.btn {
	color: white;
	background: #4E6166;
	text-align: center;
	border: none;
	border-radius: 5px;
	display: block;
	letter-spacing: .1em;
	margin: 10px 0px;
	padding: 13px 20px;
	text-decoration: none;
}
.container {
	width: 80%;
	margin: 0px auto;
}
/* NAVBAR */
.navbar {
	margin: 0 auto;
    overflow: hidden;
	background-color: #3E606F;
    border-radius: 0px 0px 6px 6px;
}
.navbar ul {
    list-style-type: none;
    float: right;
}
.navbar ul li {
    float: left;
    font-family: 'Noto Serif', serif;
}
.navbar ul li a {
    display: block;
    color: white;
    text-align: center;
    padding: 20px 28px;
    text-decoration: none;
}
.navbar ul li a:hover {
	color: #B9E6F2;
    background-color: #334F5C;
}

/* LOGO */
.navbar .logo_div {
	float: left;
	padding-top: 5px;
	padding-left: 40px;
}
.navbar .logo_div h1 {
	color: #B9E6F2;
	font-size: 3em;
	letter-spacing: 5px;
	font-weight: 100;
	font-family: 'Tangerine', cursive;
}

/* FOOTER */
.footer {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  color: white;
  background-color: #73707D;
  text-align: center;
  width: 80%;
  margin: 20px auto 0px;
  padding: 20px 0px;
}
```

Ce code commence par le style par défaut du site, suivi du style de la barre de navigation et de celui du pied de page.

Rechargez la page dans le navigateur. Notre page simple a maintenant une jolie barre de navigation avec un logo, de belles polices de caractères et, si vous faites défiler la page, notre pied de page est caché quelque part en bas. Excellent !

Notre page comporte toutefois quelques segments de code qui seront répétés sur de nombreuses autres pages du site. Par exemple, la plupart des pages auront besoin d’une barre de navigation et d’un pied de page, ainsi que des liens vers le style et les polices qui se trouvent dans la section d’en-tête. En PHP, nous pouvons écrire un morceau de code dans un fichier et l’inclure à une position particulière dans plusieurs autres fichiers. Cela revient à écrire le même code à ces endroits, mais avec l’avantage d’éviter la répétition du code. Pour ce faire, nous utilisons les mots-clés include ou require.

Comme vous l’avez peut-être déjà deviné, il est temps d’utiliser le dossier includes que nous avons créé au début. Les sections qui se répètent sont l’en-tête, la barre de navigation et le pied de page. Donc, dans votre dossier includes, créez 3 fichiers, à savoir head\_section.php, navbar.php et footer.php.

![](https://codewithawa.com/assets/post_images/how-to-create-a-blog-in-php-and-mysql-database%20---%20(1).png.2018-02-18.1518947179.png)

Allez dans le fichier index.php, sélectionnez la partie du code de la première ligne jusqu’à la balise
incluse directement au-dessus de vos balises et coupez-la. Maintenant, allez dans le fichier nouvellement créé complete-blog-php/includes/head\_section.php et collez le code dedans.

**Le fichier head\_section.php contient donc le code suivant :**

```
<!DOCTYPE html>
<html>
<head>
	<!-- Google Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Averia+Serif+Libre|Noto+Serif|Tangerine" rel="stylesheet">
	<!-- Styling for public area -->
	<link rel="stylesheet" href="static/css/public_styling.css">
	<meta charset="UTF-8">
```

De retour dans votre fichier index.php, remplacez le code que vous venez de couper par la ligne suivante :

```
<?php require_once('includes/head_section.php') ?>
```

Notez que la ligne qui suit immédiatement cette ligne include est la balise . Nous n’avons pas inclus la balise <title> dans le fichier head\_section.php car le titre de chaque page pourrait devoir être différent des autres à des fins d’optimisation pour les moteurs de recherche.

**Faisons maintenant la même chose avec la section navbar et le pied de page.**

Dans votre fichier index.php, sélectionnez et coupez le code de la barre de navigation à l’endroit indiqué par un commentaire et collez-le dans navbar.php dans le dossier includes. Voici le fichier navbar.php après collage :

```

	
		<h1>LifeBlog</h1></a>
	</div>
	<ul>
	  <li>Home</a></li>
	  <li>News</a></li>
	  <li>Contact</a></li>
	  <li>About</a></li>
	</ul>
</div>
```

Ensuite, à la place de la barre de navigation dans votre index.php, ajoutez cette ligne :

```
<!-- navbar -->
<?php include('includes/navbar.php') ?>
```

Pour ce qui est du pied de page, sélectionnez et coupez le code de la balise d’ouverture du pied de page
jusqu’à la dernière ligne de la page, et collez-le dans le fichier footer.php nouvellement créé. Voici le fichier footer.php après le collage :

```

			MyViewers &copy; <?php echo date('Y'); ?></p>
		</div>
	</div>
	<!-- // container -->
</body>
</html>
```

Remplacez ensuite cette section dans la page index.php par l’include pour footer.php

```
<!-- footer -->
<?php include('includes/footer.php') ?>
```

Après cette réorganisation, notre fichier index.php ressemble à ceci :

```
<?php require_once('includes/head_section.php') ?>
	<title>LifeBlog | Home </title>
</head>
<body>
	<!-- container - wraps whole page -->
	
		<!-- navbar -->
		<?php include('includes/navbar.php') ?>

		<!-- Page content -->
		
			<h2 class="content-title">Recent Articles</h2>
			<hr>
			<!-- more content still to come here ... -->
		</div>
		<!-- // Page content -->

		<!-- footer -->
		<?php include('includes/footer.php') ?>
```

Si vous rechargez la page, aucun changement ne sera observé.

Ajoutons maintenant une bannière sur la page d’accueil, juste en dessous de la barre de navigation. Créez un nouveau fichier nommé banner.php dans votre dossier complete-blog-php/includes et collez-y ce code :

```

	
		<h1>Today's Inspiration</h1>
		<p>
		    One day your life <br>
		    will flash before your eyes. <br>
		    Make sure it's worth watching. <br>
			<span>~ Gerard Way
		</p>
		Join us!</a>
	</div>
	
		<form action="index.php" method="post" >
			<h2>Login</h2>
			<input type="text" name="username" placeholder="Username">
			<input type="password" name="password"  placeholder="Password">
			<button class="btn" type="submit" name="login_btn">Sign in</button>
		</form>
	</div>
</div>
```

Incluez-le dans votre index.php, juste en dessous de l’include de la barre de navigation :

```
<!-- navbar is up here... -->

<!-- banner -->
<?php include('includes/banner.php') ?>
```

TÉLÉCHARGER une image, renommer la en banner.jpg placer la dans votre dossier complete-blog-php/static/images/.

Une fois que vous avez fait cela, ajoutez ce code CSS dans votre fichier public\_styling.css ; c’est le style de la bannière :

```
/* BANNER: Welcome message; */
.banner {
	margin: 5px auto;
	min-height: 400px;
	color: white;
	border-radius: 5px;
	background-image: url('../images/banner.jpg');
	background-size: 100% 100%;
}
.banner .welcome_msg {
	width: 45%;
	float: left;
	padding: 20px;
}
.banner .welcome_msg h1 {
	color: #B9E6F2;
	margin: 25px 0px;
	font-size: 2.4em;
	font-family: 'Averia Serif Libre', cursive;
}
.banner .welcome_msg p {
	color: white;
	font-size: 1.5em;
	line-height: 1.8em;
    font-family: 'Noto Serif', serif;
}
.banner .welcome_msg p span {
	font-size: .81em;
	color: #3E606F;
}
.banner .welcome_msg a {
	width: 30%;
	margin: 20px 0px;
	padding: 12px 15px;
	font-size: 1.2em;
	text-decoration: none;
}
.banner .welcome_msg a:hover {
	background: #374447;
}

/* BANNER: Login Form; */
.banner .login_div {
	width: 50%;
	float: left;
}
.banner .login_div form {
	margin-top: 40px;
}
.banner .login_div form h2 {
	color: white;
	margin-bottom: 20px;
    font-family: 'Noto Serif', serif;
}
.banner .login_div form input {
	width: 60%;
	color: white;
	border: 1px solid white;
	margin: 10px auto;
	letter-spacing: 1.3px;
    font-family: 'Noto Serif', serif;
}
.banner .login_div form button {
	display: block;
	background: #006384;
	margin-left: 20%;
}
```

Rechargez la page maintenant.

Si vous avez tout fait correctement, vous aurez une belle bannière avec l’image banner.jpg en arrière-plan, un formulaire de connexion à droite et une citation inspirante accompagnée d’un bouton “Rejoignez-nous” à gauche. Cool !

Créons un fichier pour initialiser les variables globales de notre application. Dans le dossier racine (complete-blog-php) de votre application, créez un fichier nommé config.php et collez-y ce code :

```
<?php
	session_start();

	// connect to database
       // coming soon...

	define ('ROOT_PATH', realpath(dirname(__FILE__)));
	define('BASE_URL', 'http://localhost/complete-blog-php/');
?>
```

**ROOT\_PATH** est défini comme l’adresse physique, par rapport au système d’exploitation, du répertoire courant dans lequel réside ce fichier (config.php). Sur ma machine par exemple, ROOT\_PATH a la valeur /opt/lampp/htdocs/complete-blog-php/. Il est utilisé pour inclure des fichiers physiques comme les fichiers de code source PHP (comme ceux que nous venons d’inclure), des fichiers physiques téléchargeables comme des images, des fichiers vidéo, des fichiers audio, etc. Mais dans ce tutoriel, nous l’utiliserons uniquement pour inclure des fichiers sources PHP.

**BASE\_URL** est simplement une adresse Web qui définit une URL pointant vers la racine de notre site Web. Dans notre cas, sa valeur est http://localhost/complete-blog-php. Elle est utilisée pour former des liens vers des CSS, des images, du javascript.

J’espère avoir suffisamment bien expliqué ces deux variables. Si vous n’avez pas compris, restez dans le coin, vous le découvrirez peut-être au fur et à mesure que nous utiliserons les variables.

Maintenant, incluons le fichier config.php nouvellement créé comme toute première ligne dans index.php. Après l’avoir inclus, nous allons modifier les quatre endroits de notre code où nous avons inclus d’autres segments de code afin qu’ils utilisent désormais la variable ROOT\_PATH pour pointer vers ces fichiers inclus. Après toutes ces modifications, notre index.php ressemblera à ceci :

```
<!-- The first include should be config.php -->
<?php require_once('config.php') ?>
<?php require_once( ROOT_PATH . '/includes/head_section.php') ?>
	<title>LifeBlog | Home </title>
</head>
<body>
	<!-- container - wraps whole page -->
	
		<!-- navbar -->
		<?php include( ROOT_PATH . '/includes/navbar.php') ?>
		<!-- // navbar -->

		<!-- banner -->
		<?php include( ROOT_PATH . '/includes/banner.php') ?>
		<!-- // banner -->

		<!-- Page content -->
		
			<h2 class="content-title">Recent Articles</h2>
			<hr>
			<!-- more content still to come here ... -->
		</div>
		<!-- // Page content -->

		<!-- footer -->
		<?php include( ROOT_PATH . '/includes/footer.php') ?>
		<!-- // footer -->
```

Cette façon d’inclure les fichiers présente l’avantage que, si plus tard certains fichiers sont déplacés vers d’autres répertoires, nous n’aurons peut-être pas besoin de mettre à jour les includes. De même, si nous décidons de modifier le chemin d’accès au répertoire racine, nous ne le ferons qu’à un seul endroit, c’est-à-dire dans le fichier config.php.

Nous en avons terminé avec la configuration de base de la zone publique. Jusqu’à présent, l’application n’est pas dynamique. Nous n’avons pas encore créé de base de données et si vous cliquez sur le bouton “join us”, vous obtiendrez une erreur du type “file not found”. La connexion de l’utilisateur n’a pas encore été implémentée non plus. Tous ces points seront traités dans les prochaines parties de ce tutoriel.

J’espère que vous l’avez apprécié. Si vous avez aimé cet article et en voulez plus, n’oubliez pas de le partager avec vos amis en utilisant l’un des liens de médias sociaux ci-dessous. Merci

**À Lire Aussi :**
