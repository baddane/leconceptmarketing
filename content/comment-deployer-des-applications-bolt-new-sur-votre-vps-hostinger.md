---
title: "Comment déployer des applications Bolt.new sur votre VPS Hostinger"
permalink: "/comment-deployer-des-applications-bolt-new-sur-votre-vps-hostinger/"
legacy_permalinks: []
type: "post"
date: "2025-08-21T09:00:00+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Intelligence artificielle"]
tags: ["Bolt.new","VPS Hostinger"]
description: "Guide complet pour déployer une application Bolt.new sur un VPS Hostinger : création, téléversement du code, installation des dépendances, construction, mise en ligne et SSL"
cover: "https://leconceptmarketing.com/wp-content/uploads/2025/08/HOSTINGER.webp"
source_url: "https://leconceptmarketing.com/comment-deployer-des-applications-bolt-new-sur-votre-vps-hostinger/"
source_capture: "20250912074243"
---
Déployer votre application Bolt.new sur un VPS Hostinger est simple. Suivez ce guide étape par étape pour mettre votre site en ligne rapidement.

Nous avons également préparé un tutoriel vidéo pour le déploiement de votre application Bolt.new

## Étape 1 – Créez et téléchargez votre application dans Bolt.new

Pour ce guide, nous utiliserons leur suggestion de créer une application Vitepress, mais le processus est similaire pour tous les projets.

Une fois le code généré, vous pouvez télécharger le code source en un seul clic. Cliquez simplement sur le bouton **Download** en haut à droite, et un fichier ZIP sera téléchargé.

## Étape 2 – Installez Ubuntu 24.04 avec CloudPanel sur Hostinger

## Étape 3 – Accédez à votre compte CloudPanel

Rendez-vous sur :

https://votre\_ip\_vps:8443/

Remplacez `votre_ip_vps` par l’adresse IP de votre VPS.

Entrez les identifiants fournis lors de la configuration de CloudPanel.

Une fois connecté, allez dans l’onglet **Sites**.
Cliquez sur **Add Site** et sélectionnez **Node.js**.

Saisissez votre domaine (ex. : `domain.tld`) et complétez la configuration.

> Remarque : Vous pouvez utiliser le nom d’hôte de votre VPS comme nom de domaine pour ce guide.

## Étape 4 – Téléversez votre code source

Accédez à votre site nouvellement créé en cliquant sur **Manage**.

Ouvrez le **File Manager** dans CloudPanel.
Naviguez vers :

/htdocs/votre\_nom\_de\_domaine/

Téléversez votre fichier ZIP téléchargé et extrayez-le. Assurez-vous que tous les fichiers sont dans le dossier `votre_nom_de_domaine`.

## Étape 5 – Installez les dépendances

Connectez-vous à votre VPS via SSH :

```
ssh exemple@votre_ip_vps
```

## Allez dans le répertoire de votre projet :

```
cd /home/votre_nom_utilisateur/htdocs/votre_nom_de_domaine/
```

Installez les dépendances Node.js :

```
npm install
```

## Étape 6 – Construisez l’application

Exécutez la commande pour générer les fichiers statiques :

npm run build

Installez le package `serve` globalement :

```
npm install -g serve
```

Utilisez **PM2** pour maintenir le serveur actif :

```
npm install -g pm2
pm2 start "serve ./docs/.vitepress/dist" --name "vitepress"
pm2 save
pm2 startup
```

### Vérifiez votre application

Ouvrez votre domaine dans un navigateur (ex. : `http://domain.tld`) pour confirmer que l’application fonctionne.

## Étape 7 – Activer SSL (optionnel)

Dans CloudPanel, allez dans l’onglet **SSL/TLS**.
Cliquez sur **Actions → New Let’s Encrypt Certificate**.

Vérifiez que SSL est installé en visitant votre domaine via HTTPS (ex. : `https://domain.tld`).
