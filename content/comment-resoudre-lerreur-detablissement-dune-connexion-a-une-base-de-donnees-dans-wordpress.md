---
title: "Comment résoudre l&#039;erreur d&#039;établissement d&#039;une connexion à une base de données dans WordPress ?"
permalink: "/comment-resoudre-lerreur-detablissement-dune-connexion-a-une-base-de-donnees-dans-wordpress/"
date: "2022-02-10T07:00:00+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Actualité Web","Crypto-monnaies","Le Journal E-marketing","Meilleur du Web"]
description: "L&#039;erreur &quot;Error establishing a database connection&quot; est probablement l&#039;une des erreurs les plus courantes et les plus effrayantes que les utilisateurs de WordPr"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/02/vg.jpg"
source_capture: "20220303085151"
method: "regex"
---
Accueil  Thémes  Comment résoudre l’erreur d’établissement d’une connexion à une base de données dans...

- Thémes

# Comment résoudre l’erreur d’établissement d’une connexion à une base de données dans WordPress ?

10 février 202278
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

L’erreur &#8220;Error establishing a database connection&#8221; est probablement l’une des erreurs les plus courantes et les plus effrayantes que les utilisateurs de WordPress peuvent rencontrer. Elle est certainement très proche de l’écran blanc de la mort (WSOD).
Cette erreur signifie que votre site Web ne communique plus ou n’a plus accès à votre base de données WordPress, et donc que votre site Web tout entier s’arrête. Ce n’est pas quelque chose à prendre à la légère et vous devriez essayer de le résoudre immédiatement car cela peut affecter directement vos ventes, votre trafic et vos analyses.
 👉🏼 Lecture complémentaire : Le Top 4 des meilleurs outils de gestion des médias sociaux pour les entreprises de toutes tailles
Table Des Mati&egrave;res
- 1 Qu’est-ce que l’erreur d’établissement d’une connexion à une base de données ?
- 2 Scénarios courants qui provoquent cette erreur :
- 3 Comment résoudre l’erreur d’établissement d’une connexion à une base de données ?
- 4 5 solutions faciles pour QuickErroring Establishing a Database Connection in WordPress :- 4.1 1. Vérifiez les identifiants de connexion à votre base de données :
- 4.2 2.Réparation d’une base de données corrompue :
- 4.3 3. Correction des fichiers corrompus :
- 4.4 4. Problèmes avec votre serveur de base de données :
- 4.5 5. Restaurer la dernière sauvegarde :

- 5 Résumé :

## Qu’est-ce que l’erreur d’établissement d’une connexion à une base de données ?
Toutes les informations de votre site WordPress, comme les données des articles, les données des pages, les méta-informations, les paramètres des plugins, les informations de connexion, etc. sont stockées dans votre base de données MySQL.
Les seules données qui n’y sont pas stockées sont les contenus multimédia tels que les images et les fichiers de votre thème/plugin/core tels que index.php, wp-login.php, etc. Lorsque quelqu’un visite votre site Web, PHP exécute le code de la page et interroge les informations de la base de données, qui les affiche ensuite dans le navigateur du visiteur.
Si, pour une raison quelconque, cela ne fonctionne pas correctement, vous vous retrouvez avec le message d’erreur établissant une connexion à la base de données, comme indiqué ci-dessous. La page entière est vide car aucune donnée ne peut être récupérée pour rendre la page, la connexion ne fonctionnant pas correctement.
Non seulement cela casse le front-end de votre site, mais cela vous empêchera également d’accéder à votre tableau de bord WordPress.
Cependant, les visiteurs ne verront peut-être pas tout de suite cette erreur sur le front-end. En effet, il est fort probable que votre site continue de fonctionner à partir du cache jusqu’à son expiration.

## Scénarios courants qui provoquent cette erreur :
Pourquoi cela se produit-il exactement ? Eh bien, voici quelques raisons courantes. Et ne vous inquiétez pas, nous allons examiner chacune d’entre elles plus en profondeur afin que vous sachiez comment les résoudre. En général, vous pouvez résoudre cette erreur en moins de 15 minutes.
Le problème le plus courant est que vos identifiants de connexion à la base de données sont incorrects. Votre site WordPress utilise des informations de connexion distinctes pour se connecter à sa base de données MySQL.
Votre base de données est corrompue. Les bases de données sont parfois corrompues en raison du grand nombre de pièces mobiles (thèmes, plugins et utilisateurs qui les suppriment et les installent constamment). Cela peut être dû à une table manquante ou individuellement corrompue, ou peut-être que certaines informations ont été supprimées par accident.
Vous pouvez avoir des fichiers corrompus dans votre installation WordPress. Cela peut même arriver parfois à cause de pirates informatiques.
Des problèmes avec votre serveur de base de données. Un certain nombre de choses peuvent ne pas fonctionner du côté de l’hébergeur, comme une base de données surchargée par un pic de trafic ou ne répondant pas à un trop grand nombre de connexions simultanées. Cela est en fait assez courant avec les hôtes partagés, car ils utilisent les mêmes ressources pour un grand nombre d’utilisateurs sur les mêmes serveurs.
👉🏼  Lecture complémentaire : Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022

## Comment résoudre l’erreur d’établissement d’une connexion à une base de données ?
Avant de commencer à résoudre l’erreur, nous vous recommandons toujours de faire une sauvegarde de votre site WordPress. Un grand nombre des recommandations ci-dessous impliquent la manipulation d’informations dans votre base de données, vous ne voulez donc pas aggraver les choses.
Vous devriez toujours faire une sauvegarde avant d’essayer de réparer votre site WordPress, même si vous pensez être un expert en technologie.
Vous pouvez utiliser un plugin de sauvegarde WordPress populaire tel que VaultPress ou WP Time Capsule pour sauvegarder à la fois vos fichiers et votre base de données.

## 5 solutions faciles pour QuickErroring Establishing a Database Connection in WordPress :
- Vérifiez si vos identifiants de connexion à la base de données sont corrects (raison la plus courante du problème).
- Réparer une base de données corrompue avec le mode de réparation de base de données intégré à WordPress : define(&#8216;WP_ALLOW_REPAIR’, true) ;
- Réparez les fichiers corrompus
- Vérifiez auprès de votre hébergeur les problèmes liés à votre serveur de base de données.
- Restaurez votre dernière sauvegarde

### 1. Vérifiez les identifiants de connexion à votre base de données :
La toute première chose à faire est de vérifier que vos identifiants de connexion à la base de données sont corrects. C’est de loin la raison la plus fréquente pour laquelle le message d’erreur d’établissement d’une connexion à la base de données apparaît. Surtout juste après la migration vers un nouvel hébergeur. Les détails de connexion de votre site WordPress sont stockés dans le fichier wp-config.php qui est généralement situé à la racine de votre site WordPress.
Il contient quatre éléments d’information importants qui doivent tous être corrects pour que la connexion s’effectue avec succès.
Nom de la base de données :
// ** MySQL settings ** //
/** The name of the database for WordPress */
define('DB_NAME', 'xxxxxx');Nom d’utilisateur de la base de données MySQL :
/** MySQL database username */
define('DB_USER', 'xxxxxx');Mot de passe de la base de données MySQL :
/** MySQL database password */
define('DB_PASSWORD', 'xxxxxxxxx');Nom d’hôte MySQL (serveur) :
/** MySQL hostname */
define('DB_HOST', 'localhost');Pour accéder à votre fichier wp-config.php, vous pouvez vous connecter à votre site via SFTP et naviguer jusqu’à la racine de votre site. Ou si vous utilisez cPanel, vous pouvez cliquer sur &#8220;Gestionnaire de fichiers&#8220;, naviguer jusqu’à la racine de votre site et faire un clic droit pour modifier le fichier.
Voici un exemple ci-dessous de ce à quoi ressemble le fichier une fois ouvert.Vous devez maintenant vérifier vos valeurs actuelles par rapport à celles de votre serveur pour vous assurer qu’elles sont correctes.
Vérifier les informations d’identification de la base de données dans cPanel :
La première chose à vérifier est le nom de la base de données. Pour ce faire, vous devez vous connecter à phpMyAdmin dans cPanel sous la section Databases.
Sur le côté gauche, vous devriez voir le nom de votre base de données en bas. Vous pouvez ignorer la base de données &#8220;information_schema&#8221; car elle est utilisée par l’hôte. Vous devez ensuite comparer ce nom avec la valeur DB_NAME de votre fichier wp-config.php. S’ils correspondent, le problème n’est pas là. S’ils ne correspondent pas, vous devez mettre à jour votre fichier wp-config.php.
Vous pouvez également vérifier qu’il s’agit de la bonne base de données en vous assurant qu’elle contient l’URL de votre site WordPress. Pour ce faire, cliquez simplement sur la base de données, puis sur la table wp_options (qui peut être nommée différemment pour des raisons de sécurité, comme wpxx_options). En haut de la table, vous verrez des valeurs pour l’URL et le nom de votre site. Si ces valeurs correspondent à votre site actuel, vous pouvez être sûr que vous êtes au bon endroit.
Si le nom de votre base de données était déjà correct et que vous obtenez toujours le message d’erreur d’établissement d’une connexion à la base de données, vous devrez également vérifier votre nom d’utilisateur et votre mot de passe. Pour ce faire, vous devrez créer un nouveau fichier PHP dans le répertoire racine de votre site WordPress, et saisir le code suivant. Vous pouvez le nommer comme vous le souhaitez, par exemple checkdb.php. Changez simplement les valeurs de db_user et db_password avec celles qui se trouvent dans votre fichier wp-config.php.
 👉🏼 Lecture complémentaire : Le Top 4 des meilleurs outils de gestion des médias sociaux pour les entreprises de toutes tailles
&lt;?php
$test = mysqli_connect('localhost', 'db_user', 'db_password');
if (!$test) {
die('MySQL Error: ' . mysqli_error());
}
echo 'Database connection is working properly!';
mysqli_close($testConnection);Ensuite, naviguez vers le fichier sur votre site WordPress : https://yourdomain.com/checkdb.php. Si vous obtenez une &#8220;Erreur MySQL : Access denied&#8221;, vous savez que votre nom d’utilisateur ou votre mot de passe est incorrect et vous devrez passer à l’étape suivante pour réinitialiser vos informations d’identification.
Voici le message que vous voulez voir, &#8220;La connexion à la base de données fonctionne correctement&#8221;. Mais bien sûr, si c’était le cas, vous ne seriez pas ici. Assurez-vous de supprimer/supprimer ce fichier lorsque vous aurez terminé vos tests.Vous devez donc réinitialiser votre nom d’utilisateur et votre mot de passe. Dans cPanel, cliquez sur Bases de données MySQL dans la section Bases de données.Faites défiler vers le bas et créez un nouvel utilisateur MySQL. Essayez de choisir un nom d’utilisateur et un mot de passe uniques afin qu’ils ne puissent pas être facilement devinés. L’outil de génération de mot de passe qu’ils fournissent fonctionne très bien.
Cliquez ensuite sur &#8220;Créer un utilisateur&#8221;. Vous pouvez également changer le mot de passe sur cet écran pour l’utilisateur actuel de la base de données qui existe déjà.
Ensuite, faites défiler vers le bas et ajoutez votre nouvel utilisateur à votre base de données. L’écran suivant vous demandera quels privilèges vous souhaitez attribuer, sélectionnez &#8220;Tous les privilèges&#8221;.
Prenez ensuite ces nouvelles informations d’identification et mettez à jour votre fichier wp-config.php. Vous devrez mettre à jour les valeurs DB_USER et DB_PASSWORD. Vous pouvez également réexécuter le fichier de test de tout à l’heure. Cela devrait résoudre votre problème d’identifiants. Si ce n’est pas le cas, il se peut que vous ayez toujours le mauvais nom d’hôte (DB_HOST).
Certains hôtes utilisent des valeurs différentes, voir la liste des valeurs d’hôte DB les plus courantes. En général, il s’agit simplement de localhost. Mais vous pouvez toujours contacter votre hébergeur ou consulter sa documentation si vous n’êtes pas sûr. Certains peuvent également utiliser 127.0.0.1 au lieu de localhost.

### 2.Réparation d’une base de données corrompue :
Dans certains cas, il se peut que votre base de données soit corrompue. Cela peut arriver occasionnellement (mais pas très souvent) car au fil du temps, des centaines de tables sont constamment ajoutées/supprimées par de nouveaux plugins et thèmes.
Si vous essayez de vous connecter au tableau de bord de votre site WordPress et que vous recevez l’erreur suivante, cela signifie que votre base de données est corrompue : &#8221; Une ou plusieurs tables de la base de données sont indisponibles. La base de données peut avoir besoin d’être réparée&#8221;.
Il est important de noter que vous pouvez voir cette erreur uniquement sur le back-end, alors que vous voyez le message d’erreur d’établissement d’une connexion à la base de données sur le front-end.
define('WP_ALLOW_REPAIR', true);Ensuite, naviguez jusqu’à l’emplacement suivant sur votre site WordPress : https://yourdomain.com/wp-admin/maint/repair.php. Vous aurez alors la possibilité de réparer la base de données ou de réparer et optimiser la base de données. Étant donné que vous êtes probablement en train de résoudre une panne sur votre site en ce moment, nous vous recommandons de choisir l’option de réparation de la base de données, car elle est plus rapide.

Après avoir exécuté la réparation de la base de données ci-dessus, assurez-vous de supprimer la ligne de code que vous avez ajoutée à votre fichier wp-config.php, sinon n’importe qui pourrait exécuter la réparation. Si vous utilisez cPanel, vous pouvez également exécuter une réparation à partir de l’écran des bases de données MySQL.
Vous pouvez également effectuer une réparation à partir de phpMyAdmin. Connectez-vous simplement à phpMyAdmin, cliquez sur votre base de données et sélectionnez toutes les tables. Puis, dans la liste déroulante, cliquez sur &#8220;Réparer la table&#8221;. Il s’agit essentiellement d’exécuter la commande REPAIR TABLE.
Et enfin, votre autre option serait d’exécuter la réparation en utilisant WP-CLI avec la commande suivante
wp db repairVous trouverez plus de documentation sur l’utilisation dans les ressources du développeur WordPress.
Si vous souhaitez optimiser votre base de données, nous avons quelques excellents tutoriels sur la façon d’optimiser les révisions de WordPress pour les performances, ainsi que sur la façon de convertir vos tables MyISAM en InnoDB. Si vous rencontrez toujours des problèmes sur votre site, passez à l’étape de dépannage suivante.
Lecture suggérée : Comment réparer l’erreur &#8220;MySQL Server Has Gone Away&#8221; dans WordPress.
👉🏼  Lecture complémentaire : Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022

### 3. Correction des fichiers corrompus :
L’autre raison possible pour laquelle vous voyez le message d’erreur établissant une connexion à la base de données est que vos fichiers sont devenus corrompus. Qu’il s’agisse d’un problème de transfert de fichiers par FTP, d’un pirate accédant à votre site ou d’un problème avec votre hébergeur, vous pouvez rapidement y remédier. Cependant, nous vous recommandons à nouveau de faire une sauvegarde de votre site avant d’essayer.
Vous allez essentiellement remplacer la version de base de WordPress sur votre site. Vous ne touchez pas à vos plugins, thèmes ou médias, juste à l’installation de WordPress elle-même. Pour ce faire, vous devrez télécharger une nouvelle copie de WordPress depuis WordPress.org.

Décompressez ce fichier sur votre ordinateur. À l’intérieur, vous voudrez supprimer le dossier wp-content, ainsi que le fichier wp-config-sample.php.
Téléchargez ensuite les fichiers restants via SFTP sur votre site, en écrasant vos fichiers existants. Cela remplacera tous les fichiers problématiques et vous permettra de disposer de nouveaux fichiers propres et non corrompus. Il est recommandé de vider le cache de votre navigateur après avoir effectué cette opération. Vérifiez ensuite votre site WordPress pour voir si l’erreur existe toujours.

### 4. Problèmes avec votre serveur de base de données :
Si rien de ce qui précède ne vous a aidé à résoudre votre problème, nous vous recommandons vivement de vérifier auprès de votre fournisseur d’hébergement car il peut s’agir d’un problème avec votre serveur de base de données.
Par exemple, s’il y a trop de connexions simultanées à votre base de données, l’erreur peut être générée. Cela est dû au fait que beaucoup d’hébergeurs ont des limites sur leurs serveurs quant au nombre de connexions autorisées en même temps. L’utilisation d’un plugin de mise en cache peut aider à minimiser les interactions avec la base de données sur votre site.
Ce problème peut se produire souvent sur les hôtes partagés car quelqu’un d’autre pourrait théoriquement affecter votre site. Ceci est dû au fait que les hôtes partagés utilisent toutes les mêmes ressources sur les serveurs.
C’est une autre raison pour laquelle nous recommandons toujours d’opter pour un hébergement WordPress géré à haute performance, afin que les choses ne soient pas surchargées. Cela signifie également que l’environnement est généralement ajusté pour gérer de grandes quantités de trafic spécifiquement pour les sites WordPress.

### 5. Restaurer la dernière sauvegarde :
Enfin, vous pouvez toujours recourir à une sauvegarde si nécessaire. Dans certains cas, cela peut être un moyen plus rapide de résoudre le problème si vous ne craignez pas de perdre des données entre le moment où votre dernière sauvegarde a été effectuée. De nombreux hôtes ont leur propre processus de restauration des sauvegardes. N’oubliez pas que vous devrez peut-être restaurer à la fois votre base de données et vos fichiers.
Vous serez ensuite invité à confirmer la restauration. Il suffit d’entrer le nom de votre site et de cliquer sur &#8220;OK&#8221;. Il crée également une sauvegarde au moment de la restauration afin que vous puissiez annuler la restauration si nécessaire.

## Résumé :
Comme vous pouvez le constater, il existe plusieurs façons de corriger l’erreur d’établissement d’une connexion à une base de données dans WordPress. La plus courante étant les informations d’identification invalides dans le fichier wp-config.php. Le meilleur point de départ est de vérifier que ces informations sont correctes. La dernière chose que l’on souhaite pour un site Web est de subir un temps d’arrêt.
Nous espérons que l’une des étapes ci-dessus vous a aidé à remettre votre site en état de marche. N’oubliez pas que vous pouvez toujours restaurer votre site à partir d’une sauvegarde si nécessaire.
Avez-vous rencontré le message d’erreur d’établissement d’une connexion à la base de données sur votre site ? Si oui, avez-vous réussi à le résoudre ? Faites-le nous savoir ci-dessous dans les commentaires.
Économisez du temps et de l’argent et optimisez les performances de votre site avec :
- L’aide instantanée d’experts en hébergement WordPress, 24 heures sur 24 et 7 jours sur 7.
- Intégration de Cloudflare Enterprise.
- Une audience mondiale avec 29 centres de données dans le monde entier.
- Optimisation avec notre surveillance intégrée des performances des applications.
 Lectures complémentaires :
- Que sont les CPM, CPC, CPA, CTR ?
- Logiciel Montage Video InVideo, Avis, Caractéristiques, prix et outils 2022
- Next Earth Avis : Immobilier virtuel, Metaverse et plus encore
- Qu’est-ce qu’un blog personnel ? Comment créer votre premier blog ?
- 15 façons de gagner de l’argent avec le programme de marketing d’affiliation d’Amazon

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM

- TAGS
- erreur base de données wordpress
- erreur connexion base de données wordpress
- erreur de connexion à la base de données
- erreur de connexion à la base de données wordpress
- erreur de la base de données wordpress
- erreur lors de la connexion à la base de données
- wordpress erreur de connexion à la base de données

Partager

Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram

Article précédentOBJ Box et texte bleu première moitié H1 d’un post WordPress

Article suivantQu’est-ce que GitHub ? Introduction à GitHub pour les débutants

#### ARTICLES CONNEXESDU MÊME AUTEUR

### Qu’est-ce qu’un blog personnel ? Comment créer votre premier blog ?

### Divi d’Elegant Themes &#8211; Qu’est-ce que Divi et combien coûte-t-il ?

### Qu’est-ce que GitHub ? Introduction à GitHub pour les débutants

### OBJ Box et texte bleu première moitié H1 d’un post WordPress

### 4 étapes incontournables pour créer un site web WordPress performant  en 2022

### Comment réparer l’erreur 404 des articles de WordPress ?

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

Divi d'Elegant Themes - Qu'est-ce que Divi et combien coûte-t-il ?

8 jours il y a

[…] Comment résoudre l’erreur d’établissement d’une connexion à une base de donnée… […]

0

Répondre

Rejoignez l'élite des experts d'internet

Bénéficiez de conseils, des documents exclusifs et  des informations non divulguées...

Nous respectons votre vie privée.

#### Ne Manquez Pas

### Qu’est-ce qu’une Landing Page et Comment Fonctionne-t-elle ?

Sébastian Magni @ Responsable du contenu -                 23 février 20220

Savez-vous ce qu'est une "landing page" et en avez-vous déjà mis une en place ?Si ce n'est pas...

### Divi d’Elegant Themes &#8211; Qu’est-ce que Divi et combien coûte-t-il ?

22 février 2022

### Comment désactiver le sélecteur de langue sur l’écran de connexion WordPress

17 février 2022

### Qu’est-ce que GitHub ? Introduction à GitHub pour les débutants

11 février 2022

### OBJ Box et texte bleu première moitié H1 d’un post WordPress

9 février 2022

#### Articles récents
-
Que sont les CPM, CPC, CPA, CTR ?
-
Logiciel Montage Video InVideo, Avis, Caractéristiques, prix et outils 2022
-
Next Earth Avis : Immobilier virtuel, Metaverse et plus encore
-
Qu’est-ce qu’un blog personnel ? Comment créer votre premier blog ?
-
15 façons de gagner de l’argent avec le programme de marketing d’affiliation d’Amazon
-
Comment Google crawls les pages avec le défilement infini
-
10 Stratégies de trading de crypto-monnaies que vous devez connaître