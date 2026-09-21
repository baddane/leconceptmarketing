---
title: "Comment résoudre l’erreur d’établissement d’une connexion à une base de données dans WordPress ?"
permalink: "/comment-resoudre-lerreur-detablissement-dune-connexion-a-une-base-de-donnees-dans-wordpress/"
legacy_permalinks: []
type: "post"
date: "2022-02-10T08:00:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Thèmes"]
tags: ["erreur base de données wordpress","erreur connexion base de données wordpress","erreur de connexion à la base de données","erreur de connexion à la base de données wordpress","erreur de la base de données wordpress","erreur lors de la connexion à la base de données","wordpress erreur de connexion à la base de données"]
description: "L'erreur \"Error establishing a database connection\" est probablement l'une des erreurs les plus courantes et les plus effrayantes que les utilisateurs de WordPress"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/02/vg.jpg"
source_url: "https://leconceptmarketing.com/comment-resoudre-lerreur-detablissement-dune-connexion-a-une-base-de-donnees-dans-wordpress/"
source_capture: "20220303085151"
---
L’erreur “Error establishing a database connection” est probablement l’une des [erreurs](https://leconceptmarketing.com/comment-reparer-lerreur-404-des-articles-de-wordpress/) les plus courantes et les plus effrayantes que les utilisateurs de WordPress peuvent rencontrer. Elle est certainement très proche de l’écran blanc de la mort (WSOD).

![Comment résoudre l'erreur d'établissement d'une connexion à une base de données dans WordPress ?](https://im0-tub-ru.yandex.net/i?id=883d13b2446e09b7d4818f105b3e9f08-l&n=13)

Cette erreur signifie que votre site Web ne communique plus ou n’a plus accès à votre base de données WordPress, et donc que votre site Web tout entier s’arrête. Ce n’est pas quelque chose à prendre à la légère et vous devriez essayer de le résoudre immédiatement car cela peut affecter directement vos ventes, votre trafic et vos analyses.

**👉🏼 Lecture complémentaire :** [**Le Top 4 des meilleurs outils de gestion des médias sociaux pour les entreprises de toutes tailles**](https://leconceptmarketing.com/le-top-4-des-meilleurs-outils-de-gestion-des-medias-sociaux-pour-les-entreprises-de-toutes-tailles/)

- 1 Qu’est-ce que l’erreur d’établissement d’une connexion à une base de données ?
- 2 Scénarios courants qui provoquent cette erreur :
- 3 Comment résoudre l’erreur d’établissement d’une connexion à une base de données ?
- 4 5 solutions faciles pour QuickErroring Establishing a Database Connection in WordPress :
  - 4.1 1. Vérifiez les identifiants de connexion à votre base de données :
  - 4.2 2.Réparation d’une base de données corrompue :
  - 4.3 3. Correction des fichiers corrompus :
  - 4.4 4. Problèmes avec votre serveur de base de données :
  - 4.5 5. Restaurer la dernière sauvegarde :
- 5 Résumé :

## Qu’est-ce que l’erreur d’établissement d’une connexion à une base de données ?

Toutes les informations de votre site WordPress, comme les données des articles, les données des pages, les méta-informations, les paramètres des plugins, les informations de connexion, etc. sont stockées dans votre base de données **[MySQL](https://www.mysql.com/fr/)**.

Les seules données qui n’y sont pas stockées sont les contenus multimédia tels que les images et les fichiers de votre thème/plugin/core tels que index.php, wp-login.php, etc. Lorsque quelqu’un visite votre site Web, [PHP](https://leconceptmarketing.com/php-blog-comment-creer-un-blog-en-php-et-base-de-donnees-mysql/) exécute le code de la page et interroge les informations de la base de données, qui les affiche ensuite dans le navigateur du visiteur.

Si, pour une raison quelconque, cela ne fonctionne pas correctement, vous vous retrouvez avec le message d’erreur établissant une connexion à la base de données, comme indiqué ci-dessous. La page entière est vide car aucune donnée ne peut être récupérée pour rendre la page, la connexion ne fonctionnant pas correctement.

Non seulement cela casse le front-end de votre site, mais cela vous empêchera également d’accéder à votre tableau de bord WordPress.

Cependant, les visiteurs ne verront peut-être pas tout de suite cette erreur sur le front-end. En effet, il est fort probable que votre site continue de fonctionner à partir du cache jusqu’à son expiration.

![Error establishing a database connection in Chrome](https://kinsta.com/wp-content/uploads/2017/07/error-establishing-a-database-connection-in-chrome.png)

## Scénarios courants qui provoquent cette erreur :

Pourquoi cela se produit-il exactement ? Eh bien, voici quelques raisons courantes. Et ne vous inquiétez pas, nous allons examiner chacune d’entre elles plus en profondeur afin que vous sachiez comment les résoudre. En général, vous pouvez résoudre cette erreur en moins de 15 minutes.

Le problème le plus courant est que vos identifiants de connexion à la base de données sont incorrects. Votre site WordPress utilise des informations de connexion distinctes pour se **[connecter à sa base de données MySQL](https://www.pierre-giraud.com/php-mysql-apprendre-coder-cours/connexion-base-donnee-mysqli-pdo/)**.
Votre base de données est corrompue. Les bases de données sont parfois corrompues en raison du grand nombre de pièces mobiles ([**thèmes**](https://leconceptmarketing.com/10-meilleurs-themes-wordpress-pour-les-cabinets-de-conseil-et-de-consulting/), plugins et utilisateurs qui les suppriment et les installent constamment). Cela peut être dû à une table manquante ou individuellement corrompue, ou peut-être que certaines informations ont été supprimées par accident.
Vous pouvez avoir des fichiers corrompus dans votre installation WordPress. Cela peut même arriver parfois à cause de pirates informatiques.
Des problèmes avec votre serveur de base de données. Un certain nombre de choses peuvent ne pas fonctionner du côté de l’hébergeur, comme une base de données surchargée par un pic de trafic ou ne répondant pas à un trop grand nombre de connexions simultanées. Cela est en fait assez courant avec les hôtes partagés, car ils utilisent les mêmes ressources pour un grand nombre d’utilisateurs sur les mêmes serveurs.

**👉🏼 Lecture complémentaire : [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)**

## Comment résoudre l’erreur d’établissement d’une connexion à une base de données ?

Avant de commencer à résoudre l’erreur, nous vous recommandons toujours de faire une sauvegarde de votre site WordPress. Un grand nombre des recommandations ci-dessous impliquent la manipulation d’informations dans votre base de données, vous ne voulez donc pas aggraver les choses.

Vous devriez toujours faire une sauvegarde avant d’essayer de réparer votre site WordPress, même si vous pensez être un expert en technologie.

Vous pouvez utiliser un plugin de sauvegarde WordPress populaire tel que [VaultPress](https://fr.jetpack.com/support/vaultpress/) ou WP Time Capsule pour sauvegarder à la fois vos fichiers et votre base de données.

## 5 solutions faciles pour QuickErroring Establishing a Database Connection in WordPress :

- **Vérifiez si vos identifiants de connexion à la base de données sont corrects (raison la plus courante du problème).**
- **Réparer une base de données corrompue avec le mode de réparation de base de données intégré à WordPress : define(‘WP\_ALLOW\_REPAIR’, true) ;**
- **Réparez les fichiers corrompus**
- **Vérifiez auprès de votre hébergeur les problèmes liés à votre serveur de base de données.**
- **Restaurez votre dernière sauvegarde**

### 1. Vérifiez les identifiants de connexion à votre base de données :

La toute première chose à faire est de vérifier que vos identifiants de connexion à la base de données sont corrects. C’est de loin la raison la plus fréquente pour laquelle le message d’erreur d’établissement d’une connexion à la base de données apparaît. Surtout juste après la migration vers un nouvel hébergeur. Les détails de connexion de votre site WordPress sont stockés dans le fichier wp-config.php qui est généralement situé à la racine de votre site WordPress.

Il contient quatre éléments d’information importants qui doivent tous être corrects pour que la connexion s’effectue avec succès.

**Nom de la base de données** :

```
// ** MySQL settings ** //
/** The name of the database for WordPress */
define('DB_NAME', 'xxxxxx');
```

**Nom d’utilisateur de la base de données MySQL** :

```
/** MySQL database username */
define('DB_USER', 'xxxxxx');
```

**Mot de passe de la base de données MySQL** :

```
/** MySQL database password */
define('DB_PASSWORD', 'xxxxxxxxx');
```

**Nom d’hôte MySQL (serveur)** :

```
/** MySQL hostname */
define('DB_HOST', 'localhost');
```

Pour accéder à votre fichier wp-config.php, vous pouvez vous connecter à votre site via SFTP et naviguer jusqu’à la racine de votre site. Ou si vous utilisez cPanel, vous pouvez cliquer sur “**Gestionnaire de fichiers**“, naviguer jusqu’à la racine de votre site et faire un clic droit pour modifier le fichier.

![Gestionnaire de fichiers Cpanel](https://kinsta.com/wp-content/uploads/2017/06/cpanel-file-manager.png)

**Voici un exemple ci-dessous de ce à quoi ressemble le fichier une fois ouvert.**

![wp-config.php credentials](https://kinsta.com/wp-content/uploads/2017/06/wp-config-file-credentials.png)

Vous devez maintenant vérifier vos valeurs actuelles par rapport à celles de votre serveur pour vous assurer qu’elles sont correctes.

**Vérifier les informations d’identification de la base de données dans cPanel :**

La première chose à vérifier est le nom de la base de données. Pour ce faire, vous devez vous connecter à phpMyAdmin dans cPanel sous la section Databases.

![cpanel phpmyadmin](https://kinsta.com/wp-content/uploads/2017/06/cpanel-phpmyadmin.png)

Sur le côté gauche, vous devriez voir le nom de votre base de données en bas. Vous pouvez ignorer la base de données “information\_schema” car elle est utilisée par l’hôte. Vous devez ensuite comparer ce nom avec la valeur DB\_NAME de votre fichier wp-config.php. S’ils correspondent, le problème n’est pas là. S’ils ne correspondent pas, vous devez mettre à jour votre fichier wp-config.php.

![cPanel database name](https://kinsta.com/wp-content/uploads/2017/06/cpanel-database-name.png)

Vous pouvez également vérifier qu’il s’agit de la bonne base de données en vous assurant qu’elle contient l’URL de votre site WordPress. Pour ce faire, cliquez simplement sur la base de données, puis sur la table wp\_options (qui peut être nommée différemment pour des raisons de sécurité, comme wpxx\_options). En haut de la table, vous verrez des valeurs pour l’URL et le nom de votre site. Si ces valeurs correspondent à votre site actuel, vous pouvez être sûr que vous êtes au bon endroit.

![pHp myadmin en Français](https://kinsta.com/wp-content/uploads/2017/06/check-site-url-in-phpmyadmin.png)

Si le nom de votre base de données était déjà correct et que vous obtenez toujours le message d’erreur d’établissement d’une connexion à la base de données, vous devrez également vérifier votre nom d’utilisateur et votre mot de passe. Pour ce faire, vous devrez créer un nouveau fichier PHP dans le répertoire racine de votre site WordPress, et saisir le code suivant. Vous pouvez le nommer comme vous le souhaitez, par exemple checkdb.php. Changez simplement les valeurs de db\_user et db\_password avec celles qui se trouvent dans votre fichier wp-config.php.

**👉🏼 Lecture complémentaire :** [**Le Top 4 des meilleurs outils de gestion des médias sociaux pour les entreprises de toutes tailles**](https://leconceptmarketing.com/le-top-4-des-meilleurs-outils-de-gestion-des-medias-sociaux-pour-les-entreprises-de-toutes-tailles/)

```
<?php
$test = mysqli_connect('localhost', 'db_user', 'db_password');
if (!$test) {
die('MySQL Error: ' . mysqli_error());
}
echo 'Database connection is working properly!';
mysqli_close($testConnection);
```

Ensuite, naviguez vers le fichier sur votre site WordPress : https://yourdomain.com/checkdb.php. Si vous obtenez une “Erreur MySQL : Access denied”, vous savez que votre nom d’utilisateur ou votre mot de passe est incorrect et vous devrez passer à l’étape suivante pour réinitialiser vos informations d’identification.

![Access denied mySQL](https://kinsta.com/wp-content/uploads/2017/06/access-denied-mySQL.png)

Voici le message que vous voulez voir, “La connexion à la base de données fonctionne correctement”. Mais bien sûr, si c’était le cas, vous ne seriez pas ici. Assurez-vous de supprimer/supprimer ce fichier lorsque vous aurez terminé vos tests.

![Database connection working properly](https://kinsta.com/wp-content/uploads/2017/06/database-connection-working-properly-e1498608809299.png)

Vous devez donc réinitialiser votre nom d’utilisateur et votre mot de passe. Dans cPanel, cliquez sur Bases de données MySQL dans la section Bases de données.

![cPanel MySQL databases](https://kinsta.com/wp-content/uploads/2017/06/cpanel-mysql-databases.png)

Faites défiler vers le bas et créez un nouvel utilisateur MySQL. Essayez de choisir un nom d’utilisateur et un mot de passe uniques afin qu’ils ne puissent pas être facilement devinés. L’outil de génération de mot de passe qu’ils fournissent fonctionne très bien.

Cliquez ensuite sur “Créer un utilisateur”. Vous pouvez également changer le mot de passe sur cet écran pour l’utilisateur actuel de la base de données qui existe déjà.

![Create new MySQL user](https://kinsta.com/wp-content/uploads/2017/06/create-new-mysql-user.png)

Ensuite, faites défiler vers le bas et ajoutez votre nouvel utilisateur à votre base de données. L’écran suivant vous demandera quels privilèges vous souhaitez attribuer, sélectionnez “Tous les privilèges”.

![Add user to database in cPanel](https://kinsta.com/wp-content/uploads/2017/06/cpanel-add-user-to-database.png)

Prenez ensuite ces nouvelles informations d’identification et mettez à jour votre fichier wp-config.php. Vous devrez mettre à jour les valeurs DB\_USER et DB\_PASSWORD. Vous pouvez également réexécuter le fichier de test de tout à l’heure. Cela devrait résoudre votre problème d’identifiants. Si ce n’est pas le cas, il se peut que vous ayez toujours le mauvais nom d’hôte (DB\_HOST).

Certains hôtes utilisent des valeurs différentes, voir la liste des valeurs d’hôte DB les plus courantes. En général, il s’agit simplement de localhost. Mais vous pouvez toujours contacter votre hébergeur ou consulter sa documentation si vous n’êtes pas sûr. Certains peuvent également utiliser 127.0.0.1 au lieu de localhost.

### 2.Réparation d’une base de données corrompue :

Dans certains cas, il se peut que votre base de données soit corrompue. Cela peut arriver occasionnellement (mais pas très souvent) car au fil du temps, des centaines de tables sont constamment ajoutées/supprimées par de nouveaux plugins et thèmes.

Si vous essayez de vous connecter au tableau de bord de votre site [WordPress ](https://fr.wordpress.org/download/)et que vous recevez l’erreur suivante, cela signifie que votre base de données est corrompue : ” Une ou plusieurs tables de la base de données sont indisponibles. La base de données peut avoir besoin d’être réparée”.

Il est important de noter que vous pouvez voir cette erreur uniquement sur le back-end, alors que vous voyez le message d’erreur d’établissement d’une connexion à la base de données sur le front-end.

```
define('WP_ALLOW_REPAIR', true);
```

![WordPress repair mode](https://kinsta.com/wp-content/uploads/2017/06/wordpress-repair-mode.png)

Ensuite, naviguez jusqu’à l’emplacement suivant sur votre site WordPress : https://yourdomain.com/wp-admin/maint/repair.php. Vous aurez alors la possibilité de réparer la base de données ou de réparer et optimiser la base de données. Étant donné que vous êtes probablement en train de résoudre une panne sur votre site en ce moment, nous vous recommandons de choisir l’option de réparation de la base de données, car elle est plus rapide.

![WordPress repair database](https://kinsta.com/wp-content/uploads/2017/06/wordpress-repair-database.png)

Après avoir exécuté la réparation de la base de données ci-dessus, assurez-vous de supprimer la ligne de code que vous avez ajoutée à votre fichier wp-config.php, sinon n’importe qui pourrait exécuter la réparation. Si vous utilisez cPanel, vous pouvez également exécuter une réparation à partir de l’écran des bases de données MySQL.

![cPanel repair database](https://kinsta.com/wp-content/uploads/2017/06/cpanel-repair-database.png)

Vous pouvez également effectuer une réparation à partir de phpMyAdmin. Connectez-vous simplement à phpMyAdmin, cliquez sur votre base de données et sélectionnez toutes les tables. Puis, dans la liste déroulante, cliquez sur “Réparer la table”. Il s’agit essentiellement d’exécuter la commande REPAIR TABLE.

![Repair tables in phpMyAdmin](https://kinsta.com/wp-content/uploads/2017/06/repair-tables-phpmyadmin.png)

Et enfin, votre autre option serait d’exécuter la réparation en utilisant WP-CLI avec la commande suivante

```
wp db repair
```

Vous trouverez plus de documentation sur l’utilisation dans les ressources du développeur WordPress.

Si vous souhaitez optimiser votre base de données, nous avons quelques excellents tutoriels sur la façon d’optimiser les révisions de WordPress pour les performances, ainsi que sur la façon de convertir vos tables MyISAM en InnoDB. Si vous rencontrez toujours des problèmes sur votre site, passez à l’étape de dépannage suivante.

**Lecture suggérée :** Comment réparer l’erreur “**MySQL Server Has Gone Away**” dans WordPress.

**👉🏼 Lecture complémentaire : [Le Top 22 Meilleurs Outils en Marketing Digital Indispensables en 2022](https://leconceptmarketing.com/les-22-meilleurs-outils-en-marketing-digital-indispensables-en-2022/)**

### 3. Correction des fichiers corrompus :

L’autre raison possible pour laquelle vous voyez le message d’erreur établissant une connexion à la base de données est que vos fichiers sont devenus corrompus. Qu’il s’agisse d’un problème de transfert de fichiers par FTP, d’un pirate accédant à votre site ou d’un problème avec votre [hébergeur](https://leconceptmarketing.com/avis-sur-lhebergeur-web-bluehost/), vous pouvez rapidement y remédier. Cependant, nous vous recommandons à nouveau de faire une sauvegarde de votre site avant d’essayer.

Vous allez essentiellement remplacer la version de base de WordPress sur votre site. Vous ne touchez pas à vos plugins, thèmes ou médias, juste à l’installation de WordPress elle-même. Pour ce faire, vous devrez télécharger une nouvelle copie de WordPress depuis [WordPress.org](https://fr.wordpress.org/).

![Download WordPress](https://kinsta.com/wp-content/uploads/2017/07/download-wordpress.png)

Décompressez ce fichier sur votre ordinateur. À l’intérieur, vous voudrez supprimer le dossier wp-content, ainsi que le fichier wp-config-sample.php.

![Delete wp-content folder](https://kinsta.com/wp-content/uploads/2017/07/delete-wp-content-folder.jpg)

Téléchargez ensuite les fichiers restants via SFTP sur votre site, en écrasant vos fichiers existants. Cela remplacera tous les fichiers problématiques et vous permettra de disposer de nouveaux fichiers propres et non corrompus. Il est recommandé de vider le cache de votre navigateur après avoir effectué cette opération. Vérifiez ensuite votre site WordPress pour voir si l’erreur existe toujours.

### 4. Problèmes avec votre serveur de base de données :

Si rien de ce qui précède ne vous a aidé à résoudre votre problème, nous vous recommandons vivement de vérifier auprès de votre fournisseur d’hébergement car il peut s’agir d’un problème avec votre serveur de base de données.

Par exemple, s’il y a trop de connexions simultanées à votre base de données, l’erreur peut être générée. Cela est dû au fait que beaucoup d’hébergeurs ont des limites sur leurs serveurs quant au nombre de connexions autorisées en même temps. L’utilisation d’un plugin de mise en cache peut aider à minimiser les interactions avec la base de données sur votre site.

Ce problème peut se produire souvent sur les hôtes partagés car quelqu’un d’autre pourrait théoriquement affecter votre site. Ceci est dû au fait que les hôtes partagés utilisent toutes les mêmes ressources sur les serveurs.

C’est une autre raison pour laquelle nous recommandons toujours d’opter pour un hébergement WordPress géré à haute performance, afin que les choses ne soient pas surchargées. Cela signifie également que l’environnement est généralement ajusté pour gérer de grandes quantités de trafic spécifiquement pour les sites WordPress.

### 5. Restaurer la dernière sauvegarde :

Enfin, vous pouvez toujours recourir à une sauvegarde si nécessaire. Dans certains cas, cela peut être un moyen plus rapide de résoudre le problème si vous ne craignez pas de perdre des données entre le moment où votre dernière sauvegarde a été effectuée. De nombreux hôtes ont leur propre processus de restauration des sauvegardes. N’oubliez pas que vous devrez peut-être restaurer à la fois votre base de données et vos fichiers.

Vous serez ensuite invité à confirmer la restauration. Il suffit d’entrer le nom de votre site et de cliquer sur “OK”. Il crée également une sauvegarde au moment de la restauration afin que vous puissiez annuler la restauration si nécessaire.

## Résumé :

Comme vous pouvez le constater, il existe plusieurs façons de corriger l’erreur d’établissement d’une connexion à une base de données dans WordPress. La plus courante étant les informations d’identification invalides dans le fichier wp-config.php. Le meilleur point de départ est de vérifier que ces informations sont correctes. La dernière chose que l’on souhaite pour un site Web est de subir un temps d’arrêt.

Nous espérons que l’une des étapes ci-dessus vous a aidé à remettre votre site en état de marche. N’oubliez pas que vous pouvez toujours restaurer votre site à partir d’une sauvegarde si nécessaire.

Avez-vous rencontré le message d’erreur d’établissement d’une connexion à la base de données sur votre site ? Si oui, avez-vous réussi à le résoudre ? Faites-le nous savoir ci-dessous dans les commentaires.

Économisez du temps et de l’argent et optimisez les performances de votre site avec :

- L’aide instantanée d’experts en hébergement WordPress, 24 heures sur 24 et 7 jours sur 7.
- Intégration de Cloudflare Enterprise.
- Une audience mondiale avec 29 centres de données dans le monde entier.
- Optimisation avec notre surveillance intégrée des performances des applications.

**Lectures complémentaires** :
