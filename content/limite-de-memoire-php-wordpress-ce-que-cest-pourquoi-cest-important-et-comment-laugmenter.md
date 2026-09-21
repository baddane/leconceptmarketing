---
title: "Limite de mémoire PHP de WordPress : ce que c’est, pourquoi c’est important et comment l’augmenter"
permalink: "/limite-de-memoire-php-wordpress-ce-que-cest-pourquoi-cest-important-et-comment-laugmenter/"
legacy_permalinks: []
type: "post"
date: "2024-07-01T12:39:41+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["WordPress"]
tags: ["augmenter","PHP de WordPress","WordPress PHP Memory"]
description: "Les sites WordPress utilisent une limite de mémoire par défaut pour le code PHP qui peut être dépassée au fur et à mesure que vous ajoutez des éléments interactifs et riches en"
cover: "https://leconceptmarketing.com/wp-content/uploads/2024/06/image-1.png"
source_url: "https://leconceptmarketing.com/limite-de-memoire-php-wordpress-ce-que-cest-pourquoi-cest-important-et-comment-laugmenter/"
source_capture: "20250125164504"
---
Vous êtes en train d’ajouter du contenu ou des médias à votre site quand soudain un message s’affiche : “Erreur fatale : La taille de mémoire autorisée de xxxxxx octets est épuisée”.
Que s’est-il passé ? Pourquoi WordPress a-t-il manqué de mémoire ?

Pour faire simple, c’est le langage de programmation PHP qui est en cause. Les sites WordPress utilisent une limite de mémoire par défaut pour le code PHP qui peut être dépassée au fur et à mesure que vous ajoutez des éléments interactifs et riches en médias à votre site.

Dans cet article, nous allons expliquer ce qu’est la limite de mémoire PHP de WordPress, pourquoi elle est importante pour votre site et ce que vous pouvez faire pour l’augmenter.

## Qu’est-ce que PHP dans WordPress ?

PHP est un langage côté serveur utilisé par WordPress pour créer et gérer les pages HTML qui composent votre site. Il est appelé “côté serveur” parce qu’il fonctionne dans le backend de WordPress, et non sur votre ordinateur de bureau ou votre appareil mobile.

PHP est un langage léger, rapide et libre, idéal pour générer des éléments de site web. Les programmeurs expérimentés peuvent personnaliser ou modifier les frameworks PHP pour répondre aux besoins spécifiques d’un site web, et le code est régulièrement mis à jour pour rationaliser les fonctionnalités et renforcer la sécurité. C’est donc un langage de script polyvalent idéal pour WordPress.

## Quelle est la limite de mémoire de PHP dans WordPress ?

Par défaut, WordPress a une limite de mémoire PHP de 32MB. C’est une bonne chose pour les sites comportant peu de pages et une quantité limitée de contenu multimédia et de plugins, mais plus vous ajoutez de contenu à votre site, plus vous vous rapprochez de la limite maximale de mémoire.

![](https://leconceptmarketing.com/wp-content/uploads/2024/06/image-1.png)

Lorsque cette limite est atteinte – disons que vous téléchargez une nouvelle vidéo ou un élément web interactif – WordPress augmente automatiquement la mémoire disponible à 40 Mo. Si vous atteignez toujours la limite, vous obtiendrez le message d’erreur décrit ci-dessus et ne pourrez pas ajouter de nouveau contenu tant que vous n’aurez pas résolu le problème.

## Quelle est la cause du problème de mémoire de PHP ?

Bien qu’il soit possible d’augmenter la mémoire PHP disponible dans WordPress au-delà de 40 Mo, il est utile de déterminer la cause des dépassements de mémoire avant de prendre des mesures pour augmenter votre limite. Voici pourquoi : Si la cause première de votre problème de mémoire n’est pas simplement l’espace disponible, mais quelque chose lié à l’utilisation de l’espace disponible, il est préférable de ne pas l’augmenter.

1. **Plugins de mauvaise qualité**Tous les plugins ne sont pas égaux. Certains sont conçus pour être rapides et de qualité, tandis que d’autres sont conçus pour remplir une fonction spécifique mais ne font aucun effort pour améliorer l’efficacité. L’utilisation de plusieurs plugins nécessitant beaucoup de mémoire peut épuiser la mémoire disponible de PHP et provoquer une erreur fatale sur votre page.
2. **Versions PHP obsolètes**Comme le note le Search Engine Journal, 61,6 % des sites WordPress utilisent des versions obsolètes de PHP. Cela présente non seulement un risque pour la sécurité des sites, mais aussi un impact sur leurs performances. Les nouvelles versions de PHP sont capables de gérer plus de tâches, plus rapidement, ce qui réduit la quantité de mémoire utilisée à tout moment.
3. **Des médias gourmands en mémoire**Ce que vous mettez sur votre site a une incidence sur la mémoire. Par exemple, si votre site WordPress est essentiellement composé de texte, avec quelques images et liens occasionnels, vous n’atteindrez probablement pas la limite de mémoire. Si vous téléchargez régulièrement des vidéos et d’autres contenus interactifs, vous risquez de manquer d’espace.

Et si vous n’êtes pas sûr de la cause du problème ? Procurez-vous un plugin tel que Server IP and Memory Usage Display qui suit l’utilisation de la mémoire et la mémoire totale disponible de votre installation [WordPress ](https://leconceptmarketing.com/5-meilleurs-outils-wordpress-de-generation-de-code-qr-pour-2023/)et indique la version de PHP que vous utilisez actuellement. Des indices visuels mettent en évidence l’augmentation de l’utilisation de la mémoire : lorsque l’utilisation de la mémoire augmente, la valeur en pourcentage passe lentement au rouge, ce qui vous indique que vous atteignez la limite. Le plugin indique également la quantité de mémoire utilisée par d’autres plugins pour vous aider à repérer les voleurs de mémoire.

Mais devez-vous maximiser votre bande passante mémoire et pousser WordPress jusqu’à sa limite ? Ou vaut-il mieux rester en dessous de la limite de mémoire pour améliorer les performances du site ? Nous en discuterons dans la section ci-dessous.

## Quelle est la limite de mémoire PHP recommandée pour WordPress ?

WordPress a une limite de mémoire de 32MB par défaut, mais certains hébergeurs augmentent cette limite à 64MB pour tous les clients. Il est également possible d’aller encore plus loin, jusqu’à 256 Mo.

Bien que la mise à l’échelle permette de disposer de plus d’espace pour le contenu et les médias, elle présente l’inconvénient potentiel de ralentir la vitesse du site si vous mettez en œuvre un grand nombre d’éléments gourmands en données. La meilleure solution ? Essayez de vous situer entre les deux pour équilibrer le débit de la mémoire et les performances.

Comment augmenter la limite de mémoire de PHP dans WordPress
Si vous avez mis à jour votre PHP, supprimé les plugins de mauvaise qualité, nettoyé votre contenu, et que vous obtenez toujours des erreurs de mémoire, il se peut que vous deviez augmenter la limite de mémoire.

**Il existe plusieurs façons d’atteindre cet objectif :**

- Modifiez votre fichier wp-config.php.
- Modifiez votre fichier PHP.ini.
- Modifiez votre fichier .htaccess.
- Utiliser un plugin d’augmentation de la mémoire.
- Contactez votre hébergeur.

## 1.Modifiez votre fichier wp-config.php.

Si vous êtes raisonnablement confiant dans vos compétences techniques, vous pouvez essayer de modifier votre fichier wp-config.php.

Première chose à faire ? L’accès au fichier. Utilisez un protocole de transfert de fichiers ([FTP](https://wpmarmite.com/ftp-wordpress/#:~:text=Un%20client%20FTP%20est%20un,WordPress%20distante%20vers%20votre%20ordinateur.)) ou un protocole de transfert de fichiers SSH (SFTP) pour vous connecter à vos fichiers WordPress et y accéder. Votre kilométrage variera en fonction de la solution que vous utilisez, mais vous devriez voir quelque chose comme ceci :

![](https://leconceptmarketing.com/wp-content/uploads/2024/06/image-2.png)

Ouvrez le fichier wp-config.php et recherchez cette chaîne de texte : define(‘WP\_MEMORY\_LIMIT’, ’32M’) ;

Ensuite, modifiez-la comme suit define(‘WP\_MEMORY\_LIMIT’, ‘128M’) ; Vous pouvez aller jusqu’à 256MB, mais dans la plupart des cas, vous n’aurez pas besoin d’une telle quantité de mémoire.

## 2. Editez votre fichier PHP.ini.

Si l’édition de votre fichier de configuration ne résout pas le problème, vous pouvez également essayer de modifier votre fichier PHP.ini. Cela vaut la peine d’être noté. Comme ce fichier régit les paramètres du serveur, vous ne pourrez pas le modifier si vous utilisez un hébergeur mutualisé.

Recherchez la ligne memory\_limit = 32M et modifiez-la à nouveau pour lire 128M. Il est également conseillé de modifier la ligne max\_execution\_time. Cette ligne indique le temps en secondes alloué à l’exécution d’un script PHP. Si la limite de temps est dépassée, PHP renvoie une erreur. En augmentant cette valeur, vos scripts auront plus de temps pour s’exécuter, ce qui est une bonne idée si vous prévoyez d’utiliser des services et des plugins plus gourmands en mémoire.

## 3. Modifiez votre fichier .htaccess.

Votre dernier recours en matière d’édition de fichiers est le fichier .htaccess. Bien qu’il soit accessible via la liste des répertoires et des fichiers renvoyée par les connexions FTP, le “.” qui le précède signifie qu’il s’agit d’un fichier caché. Si vous ne le voyez pas, vérifiez que votre solution FTP ou SFTP est configurée pour afficher tous les fichiers et répertoires cachés.

Une fois que vous avez accédé au fichier, trouvez cette ligne : php\_value memory\_limit Ajoutez ensuite la valeur que vous souhaitez – 64M, 128M ou 256M – et enregistrez le fichier.

Quelle que soit la méthode d’édition de fichier choisie, veillez à vider votre cache avant de vérifier si le problème est résolu.

## 4.Utiliser un plugin d’augmentation de la mémoire.

Une autre option pour augmenter votre mémoire PHP disponible est l’utilisation d’un plugin, comme le plugin WordPress WP Memory Limit, Memory Usage, Server Memory, and Health. Ce plugin fonctionne avec la version 5.2 ou supérieure de WordPress et vous permet de modifier la mémoire PHP disponible sans avoir besoin d’accéder à des fichiers ou de les modifier.

## 5.Contactez votre hébergeur

Dernier point, mais non des moindres ? Contactez votre hébergeur et demandez-lui d’augmenter la limite de mémoire PHP de WordPress. Selon le type d’hébergement que vous avez – partagé, dédié ou serveur privé virtuel – il peut s’agir d’une solution rapide ou d’un service qui n’est pas offert.

## Merci pour les souvenirs :

Les erreurs de mémoire PHP dans WordPress sont frustrantes, mais elles ne sont pas permanentes. En modifiant vos fichiers WordPress, en utilisant un plugin ou en contactant votre hébergeur, il est possible d’augmenter significativement votre mémoire disponible et d’éviter les problèmes PHP.

→  **D’autres articles qui pourraient vous intéresser** :
