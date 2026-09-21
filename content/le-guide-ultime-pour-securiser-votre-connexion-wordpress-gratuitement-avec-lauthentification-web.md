---
title: "Le guide ultime pour sécuriser votre connexion WordPress (gratuitement !) avec l’authentification Web"
permalink: "/le-guide-ultime-pour-securiser-votre-connexion-wordpress-gratuitement-avec-lauthentification-web/"
legacy_permalinks: []
type: "post"
date: "2022-07-24T10:35:07+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Plugins","Thèmes","WordPress"]
tags: ["CMS","créer un site wordpress","extensions","Plugins","site web","thèmes","wordpress"]
description: "Wordpress News, les actualités du Wordpress.. Le guide ultime pour sécuriser votre connexion WordPress (gratuitement !) avec l'authentification Web"
cover: "https://leconceptmarketing.com/wp-content/uploads/2022/07/the-ultimate-guide-to-securing-your-wordpress-login.png"
source_url: "https://leconceptmarketing.com/le-guide-ultime-pour-securiser-votre-connexion-wordpress-gratuitement-avec-lauthentification-web/"
source_capture: "20220812171906"
---
[Défenseur](https://wordpress.org/plugins/defender-security/) avait déjà mis en place l’authentification à deux facteurs (2FA) dans WordPress pour une sécurité renforcée… nous avons maintenant ajouté la reconnaissance des empreintes digitales/faciales, ainsi que des clés de sécurité matérielles externes !

Il est devenu de plus en plus évident que se fier strictement aux noms d’utilisateur et aux mots de passe pour les connexions n’offre plus les niveaux de sécurité les plus élevés.

La solution de WPMU DEV pour résoudre ce problème consiste à utiliser le *WebAuthn* standard, qui contourne les vulnérabilités en fournissant un protocole de cryptographie à clé publique comme méthode d’authentification de connexion.

Notre dernière version de Defender, à la fois [Libre](https://wordpress.org/plugins/defender-security/) et les versions Pro – marquent le début de notre odyssée dans le monde de l’authentification Web ; offrant la possibilité de vérifier l’authenticité d’une connexion d’utilisateur au moyen de la biométrie (reconnaissance faciale ou d’empreintes digitales) ou d’une clé de sécurité USB (par exemple, YubiKey).

L’utilisation de ces nouvelles méthodes d’authentification Web est similaire aux méthodes 2FA déjà présentes dans Defender, aux côtés du TOTP (Time-based One-Time Password), des codes de sauvegarde et des méthodes d’authentification de secours par e-mail.

Dans cet article, nous allons voir comment implémenter ces nouvelles méthodes d’authentification Web, dans le cadre de nos fonctionnalités de plugin WordPress 2FA dans Defender.

Continuez à lire ou avancez en utilisant ces liens :

Explorons tout ce que Defender a à offrir sous forme de protection de connexion avec les nouvelles fonctionnalités 2FA WebAuth.

- 1 Le défenseur universel
- 2 Procédure pas à pas complète sur l’authentification Web
  - 2.1 Activer la clé de sécurité biométrique ou USB
  - 2.2 Enregistrer l’appareil
    - 2.2.1 Exemple 1:
    - 2.2.2 Exemple 2 :
  - 2.3 Authentifier l’appareil
  - 2.4 Renommer ou supprimer un appareil
  - 2.5 Conformité RGPD
  - 2.6 Activation de plusieurs méthodes 2FA
- 3 Le forfait complet

## Le défenseur universel

Defender vous offre le meilleur de la sécurité des plugins WordPress, en arrêtant les injections SQL, les scripts intersites XSS, les attaques de connexion par force brute et d’autres vulnérabilités, avec une liste de techniques de renforcement en un clic qui ajouteront instantanément des couches de protection à votre site.

Cela facilite également la sécurité pour vous et pour vous, en tirant parti des dernières mesures de sécurité WebAuth.

En guise d’aperçu rapide, voici comment cela fonctionne dans Defender… l’utilisateur entrera son nom d’utilisateur et son mot de passe pour se connecter, et si l’authentification de la plate-forme a été configurée pour cet appareil, ledit utilisateur peut vérifier son identité via son lecteur d’empreintes digitales ou sa reconnaissance faciale. Logiciel. De même, si l’authentification Roaming a été configurée pour cet appareil, l’utilisateur peut vérifier son identité via sa clé de sécurité USB.

Parce que nous utilisons le *WebAuthn* protocole, Defender ne reçoit à aucun moment des données biométriques ou de clé de sécurité, uniquement une confirmation ou un rejet de l’appareil de l’utilisateur.

Je veux intervenir ici avec un point d’intérêt rapide, partagé par l’un de nos techniciens, Marcel Oudejans (et paraphrasé par moi)…

La convention de nommer un chien “Fido” a été popularisée par Abraham Lincoln, bien que son utilisation comme nom d’animal de compagnie canin remonte aux anciens Romains.

“*Fido*» signifie « fidèle ». *FIDO* signifie “**F**dernièrement **IDENTIFIANT**entité **O**en ligne ». La nouvelle fonctionnalité d’authentification biométrique utilise *WebAuthn* protocole de FIDO.

Donc, d’une manière charmante et détournée, en utilisant le protocole FIDO pour implémenter cette fonctionnalité, on pourrait dire que nous insufflons de la “fidélité” dans Defender.

Fidèle FIDO.

Pour plus d’informations techniques sur [FIDO, consultez cet article](https://fidoalliance.org/fido2/).

Ok, examinons maintenant en profondeur ces nouvelles fonctionnalités impressionnantes d’authentification Web.

## Procédure pas à pas complète sur l’authentification Web

Tout d’abord, assurez-vous que le plugin Defender est installé et activé, et mettez-le à jour vers la dernière version (au moment d’écrire ces lignes, c’est 3.1.1). Les versions 3.0 et supérieures de Defender sont entièrement compatibles avec le WordPress 6.0 récemment publié.

Deux choses importantes à noter dès le départ :

1. La configuration des appareils autorisés est requise pour chaque utilisateur, car l’authentification est liée à des comptes d’utilisateurs individuels.
2. [PHP 7.2 ou supérieur est requis, car il améliore les performances et la sécurité, tout en prenant en charge la nouvelle fonctionnalité biométrique.](https://wpmudev.com/docs/getting-started/wpmu-dev-minimum-requirements/)

### Activer la clé de sécurité biométrique ou USB

Naviguez vers WordPress **Tableau de bord > Défenseur**. Si vous venez de mettre à jour, vous obtiendrez le modal contextuel. Lisez-le rapidement, puis cliquez sur le **J’ai compris** bouton.

![écran de démarrage du défenseur](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655305_117_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Les fonctionnalités WebAuth de WPMU DEV se sont à nouveau étendues !

Vous serez maintenant sur la page principale de Defender. Dans la barre latérale gauche, cliquez sur le **2FA** en-tête de menu.

Une autre fenêtre contextuelle apparaîtra ; clique sur le **Activer** bouton.

![Le défenseur active 2FA](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655305_7_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Activation en un clic dans Defender.

Vous verrez maintenant toutes les informations de la section sur l’authentification à deux facteurs et toutes les options disponibles ici.

À partir de la même page Defender 2FA, sous **Rôles d’utilisateur > Administrateur**basculez le bouton *Sur*. Assurez-vous de faire défiler vers le bas et cliquez sur **Sauvegarder les modifications**.

![Activez les rôles d'utilisateur administrateur.](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655305_193_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

L’autorisation d’activer 2FA est donnée par **Rôles d’utilisateur**.

Dans le menu latéral du tableau de bord, accédez au **Utilisateurs** section, et cliquez sur votre *Utilisateur administrateur* profil.

Faites défiler jusqu’à **Sécurité** section, et à côté de **Authentification Web**basculez le bouton *SUR*.

![activer l'authentification Web](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655305_42_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Sélection de la fonction WebAuth dans **Défenseur**.

Vous verrez une recommandation pour choisir une méthode d’authentification supplémentaire parmi ces options : **TOTP, codes de secours,** et **E-mail de secours**.

Dans l’exemple ci-dessous, vous verrez que j’ai sélectionné **E-mail de secours**, mais vous pouvez choisir la ou les méthodes que vous préférez. N’oubliez pas de cliquer sur le **Mettre à jour le profil** bouton en bas.

![Sélection de méthodes d'authentification supplémentaires](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_679_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

La sélection de méthodes d’authentification supplémentaires disponibles dans Defender.

L’authentification Web ne remplace pas votre connexion WordPress traditionnelle (c’est-à-dire, nom d’utilisateur et mot de passe), mais ajoute une couche sécurisée supplémentaire, comme les autres options d’authentification ci-dessus.

Bien que de nombreux navigateurs et systèmes d’exploitation soient compatibles avec le *WebAuthn* protocole utilisé pour gérer le processus d’authentification, certains ne le sont pas actuellement. Vérifiez ici pour voir *WebAuthn’s* navigateur et système d’exploitation [liste de compatibilité](https://webauthn.me/browser-support).

### Enregistrer l’appareil

Lorsque l’authentification WebAuth est activée, le **Appareil enregistré** tableau apparaîtra, avec des options pour **Enregistrer l’appareil** ou **Authentifier l’appareil**.

![Identificateurs d'appareils enregistrés](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_952_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Defender conserve une liste des identifiants d’appareils enregistrés.

En cliquant sur le **Enregistrer l’appareil** lancera l’invite de votre navigateur pour configurer la forme d’authentification Web que vous souhaitez utiliser, en fonction de ce qui est disponible sur votre appareil.

**Sélectionnez un type d’authentificateur**entrez n’importe quel nom dans **Identificateur d’authentificateur** champ, puis cliquez sur le **Commencer l’inscription** bouton.

![appareil d'enregistrement webauth](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_182_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Saisie d’informations pour authentifier un appareil ; dans ce cas, une clé de sécurité USB.

Selon le type d’authentificateur et l’appareil que vous utilisez, le processus d’enregistrement sera différent.

#### Exemple 1:

Enregistrement d’un **les fenêtres** ordinateur de bureau ou portable vous invitera à entrer votre code PIN Windows Hello, ou toute autre méthode d’authentification pouvant être activée sur votre appareil.

![Connexion par code PIN Windows Hello](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_388_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

L’entrée du code PIN de connexion Windows Hello.

#### Exemple 2 :

L’enregistrement d’un appareil mobile vous invitera à toucher le capteur d’empreintes digitales ou toute autre méthode d’authentification pouvant être activée sur votre appareil.

![Vérifier le capteur d'empreintes digitales](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_803_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Exemple de fenêtre d’authentification du capteur d’empreintes digitales.

**Exemple 3 :**

L’enregistrement d’une clé de sécurité USB vous invitera à suivre une brève série d’étapes.

![Publier une image](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_491_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

De retour sur votre **Profil des utilisateurs** page, si vous faites défiler vers le bas sous **Sécurité > Appareil enregistré**vous verrez votre appareil répertorié ici, ainsi qu’un message en dessous confirmant qu’il a bien été enregistré.

![confirmation enregistrée webauth](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_636_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Félicitations! Vous êtes inscrit. Ensuite… l’authentification.

L’étape suivante consiste à authentifier l’appareil que vous venez d’enregistrer.

### Authentifier l’appareil

Une fois l’appareil enregistré, cliquez sur le **Authentifier l’appareil** bouton.

La même méthode d’authentification utilisée pour enregistrer l’appareil vous demandera de confirmer l’action.

![périphérique authentifié avec succès](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655306_763_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Confirmations d’authentification de périphérique WebAuth pour un ordinateur de bureau et une clé YubiKey.

Une fois cela fait, vous verrez un message de réussite apparaître. Vous pourrez désormais utiliser les options WebAuth enregistrées comme moyens supplémentaires et sécurisés de vous connecter à votre site.

### Renommer ou supprimer un appareil

Si vous le souhaitez, vous pouvez renommer ou supprimer tout appareil authentifié.

Naviguez vers WordPress **Tableau de bord > Utilisateurs**et cliquez sur votre *Nom d’utilisateur*.

**Renommer**:

De **Profil > Sécurité > Appareil enregistré**clique sur le **Renommer** texte dans le **Action** colonne**.** Tapez le nouveau nom et cliquez sur **sauvegarder**.

![Renommer ou supprimer l'appareil enregistré](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655307_96_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Options d’action pour les appareils enregistrés.

**Supprimer:**

Même processus que ci-dessus, mais cliquez sur le **Effacer** texte dans le **Action** colonne, puis cliquez sur **D’ACCORD** à partir de la prochaine fenêtre contextuelle.

![Confirmer l'action de suppression](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655307_498_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Confirmation de la suppression d’une authentification.

Soyez avisé que le *Effacer* l’action n’enregistre pas les paramètres, donc si vous décidez de réutiliser la fonction biométrique à partir de cet appareil, vous devrez suivre le processus de configuration complet.

De même, si vous désactivez une fonctionnalité WebAuth sur votre appareil, la connexion ne fonctionnera plus et vous devrez répéter le processus sur votre appareil pour restaurer la fonctionnalité de la fonctionnalité.

### Conformité RGPD

Les normes de l’Alliance FIDO ont été créées dès le départ avec une approche de « confidentialité dès la conception » et sont parfaitement adaptées à la conformité au RGPD.

Étant donné que FIDO fournit une authentification sans implication de tiers ni suivi entre les comptes et les services, l’authentification biométrique avec les appareils compatibles FIDO2 est entièrement conforme au RGPD.

Avec FIDO, aucune information d’identification personnelle ne quitte jamais votre appareil.

Pour plus d’informations, consultez l’article suivant sur le site Web de FIDO : [Authentification FIDO et RGPD](https://fidoalliance.org/fido-authentication-and-gdpr-presentation/).

### Activation de plusieurs méthodes 2FA

Si vous activez plusieurs méthodes d’authentification supplémentaires dans votre profil, chacune s’affichera sous la forme d’options alternatives sous la méthode que vous avez définie par défaut. Dans l’exemple ci-dessous, l’authentification TOTP est ma méthode préférée.

Vous pouvez cliquer sur n’importe quelle option disponible dans la liste, et cela affichera la méthode d’authentification alternative sélectionnée.

![Authentification TOTP](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655307_917_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Utilisation d’un TOTP pour s’authentifier, avec des méthodes alternatives (selon votre sélection) répertoriées ci-dessous.

Une note finale… L’authentification Web nécessite que les extensions PHP suivantes soient activées sur votre serveur : *mbstring, GMP,* et *Sodium*. Ces extensions sont activées par défaut sur tous les sites hébergés par WPMU DEV.

Si vous hébergez ailleurs et que l’un d’entre eux n’est pas activé sur votre serveur, vous verrez une alerte comme celle ci-dessous. Contactez votre fournisseur d’hébergement pour qu’il active les extensions pour vous afin que vous puissiez utiliser cette fonctionnalité.

![Alerte de message, exigences non remplies](https://leconceptmarketing.com/wp-content/uploads/2022/07/1658655307_733_Le-guide-ultime-pour-securiser-votre-connexion-WordPress-gratuitement.png)

Si vous voyez ce message, ne paniquez pas, vous aurez juste besoin d’activer certaines extensions PHP.

Cliquez ici pour l’intégralité de WPMU DEV [documentation sur la fonctionnalité d’authentification Web de Defender.](https://wpmudev.com/docs/wpmu-dev-plugins/defender/#web-authentication)

## Le forfait complet

Comme les mesures de protection vont dans WordPress, il est difficile de battre Defender.

Defender dispose de puissants protocoles de sécurité, y compris l’analyse des logiciels malveillants, les analyses antivirus, le blocage IP, le pare-feu, le journal d’activité, le journal de sécurité et l’authentification à deux facteurs (2FA), y compris les deux méthodes d’authentification Web nouvellement ajoutées : biométrique et clé de sécurité USB.

La dernière version de Defender est également venue avec une amélioration supplémentaire et utile de la commande “scan” WP-CLI de Defender. En utilisant cette commande et cette option WP-CLI, si des problèmes sont détectés, Defender créera un tableau avec les résultats.

Auparavant, vous ne pouviez voir les résultats d’une analyse de logiciels malveillants qu’à partir du back-end du site (dans WP Admin > Defender Pro > Analyse de logiciels malveillants), mais vous pourrez désormais voir les résultats de l’analyse terminée directement dans la console.

Prochainement pour Defender… nous développerons notre utilisation de *WebAuthn*, nos développeurs travaillant actuellement sur la possibilité d’utiliser des dispositifs d’authentification matériels. Des plans sont également en cours pour mettre en œuvre des connexions « sans mot de passe » de la meilleure façon possible, en utilisant le *WebAuthn* protocole.

Vous pouvez en savoir plus sur les fonctionnalités à venir pour l’un de nos outils et services à tout moment dans notre produit [Feuille de route.](https://wpmudev.com/roadmap/)

Si 2FA est la question, Defender est la réponse. La gestion de la sécurité dans vos sites WordPress peut être aussi simple, mais complète, que l’activation [Défenseur](https://wordpress.org/plugins/defender-security/).
