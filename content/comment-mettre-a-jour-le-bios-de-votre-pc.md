---
title: "Comment mettre à jour le BIOS de votre PC"
permalink: "/comment-mettre-a-jour-le-bios-de-votre-pc/"
legacy_permalinks: []
type: "post"
date: "2023-10-09T08:42:11+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["High Tech"]
tags: ["BIOS","mettre à jour le BIOS"]
description: "Une minuscule puce BIOS se cache à l'intérieur de chaque ordinateur, sur votre carte mère, pour donner vie à votre système lorsque vous appuyez sur le bout"
cover: "https://leconceptmarketing.com/wp-content/uploads/2023/10/image-10.png"
source_url: "https://leconceptmarketing.com/comment-mettre-a-jour-le-bios-de-votre-pc/"
source_capture: "20231201110402"
---
Une minuscule puce BIOS se cache à l’intérieur de chaque ordinateur, sur votre carte mère, pour donner vie à votre système lorsque vous appuyez sur le bouton d’alimentation. Non seulement elle alimente votre PC, mais elle contribue également à le protéger, comme en témoigne la décision d’AMD de collaborer avec ses partenaires pour diffuser des mises à jour BIOS critiques pour les cartes mères AM5 après que les nouvelles puces**[ Ryzen 7000 X3D](https://amzn.to/3tronxO)** ont commencé à brûler littéralement (bien que rarement).

![](https://leconceptmarketing.com/wp-content/uploads/2023/10/image-10-1024x634.png)

BIOS est l’abréviation de Basic Input and Output System (système d’entrée et de sortie de base), et la puce BIOS initialise tous les autres périphériques de votre PC, comme le CPU, le GPU et le chipset de la carte mère.

Mais il y a quelques années, les fabricants de cartes mères, en partenariat avec Microsoft et Intel, ont introduit une solution de remplacement des puces [BIOS traditionnelles](https://learn.microsoft.com/fr-fr/windows-hardware/manufacture/desktop/boot-to-uefi-mode-or-legacy-bios-mode?view=windows-11), appelée UEFI (Unified Extensible Firmware Interface).

Presque toutes les cartes mères commercialisées aujourd’hui sont équipées d’une puce UEFI plutôt que d’une puce BIOS (l’UEFI est d’ailleurs une exigence du système Windows 11), mais elles ont toutes deux le même objectif principal : préparer le système à démarrer dans le système d’exploitation. Cela dit, la plupart des gens continuent d’appeler l’UEFI le “BIOS” en raison de la familiarité du terme.

## Pourquoi vous devriez (ou ne devriez pas) mettre à jour votre BIOS :

Il est important de comprendre l’UEFI pour savoir comment (et si) tirer parti des mises à jour de fonctionnalités et des corrections de bogues qui accompagnent les mises à jour du BIOS proposées par les fabricants de cartes mères.

Votre carte mère utilise probablement la révision du micrologiciel que le fabricant de la carte mère avait adoptée au moment de sa construction. Au cours de la durée de vie d’une carte mère, les fabricants publient de nouveaux microprogrammes ou des mises à jour du BIOS qui permettent la prise en charge de nouveaux processeurs et de nouvelles mémoires, ou qui résolvent des bogues fréquemment signalés.

Pendant des années, la seule véritable raison de mettre à jour un micrologiciel est de résoudre un bogue dans l’UEFI ou de remplacer un processeur plus récent que la carte mère.

Certaines personnes aiment vérifier et mettre à jour régulièrement leurs paquets de microprogrammes UEFI pour rester à jour. Il fut un temps où cette pratique était considérée comme risquée, étant donné que le processus de mise à jour du micrologiciel pouvait potentiellement faire disjoncter votre carte mère, de la même manière que le flashage d’une ROM personnalisée sur un téléphone Android peut faire disjoncter l’appareil.

Il est préférable de ne pas mettre à jour votre micrologiciel UEFI à moins que vous n’ayez besoin de quelque chose de spécifique offert par le micrologiciel mis à jour.

Cela dit, vous devriez probablement rester au courant des mises à jour du BIOS si vous utilisez une puce ou une plate-forme de carte mère qui vient tout juste d’être lancée – comme en témoignent les mises à jour critiques du BIOS pour la nouvelle plate-forme de carte mère AM5 d’AMD mentionnée ci-dessus. Vivre à la pointe de la technologie exige souvent de la diligence.

## Comment mettre à jour le BIOS de votre PC :

Veillez à sauvegarder vos données essentielles avant de procéder à une mise à jour du BIOS ! Ces mises à jour modifient des aspects essentiels de votre PC et il est vital de disposer de sauvegardes en cas de problème.

![](https://leconceptmarketing.com/wp-content/uploads/2023/10/image-11-1024x590.png)

mise a jour des informations systeme du bios

1. **Recherchez la version actuelle de votre BIOS :** Avant de mettre à jour votre BIOS, assurez-vous que vous installez bien une nouvelle version. Le moyen le plus simple de trouver la version de votre BIOS est d’ouvrir l’application Informations système en tapant msinfo dans la barre de recherche de Windows. Dans la fenêtre qui s’ouvre, la version de votre BIOS doit apparaître à droite, sous la vitesse de votre processeur. Notez le numéro et la date de la version, puis comparez-la à la dernière version disponible sur la page d’assistance de votre carte mère sur le site web du fabricant.
2. **Entrez dans le BIOS UEFI :** Lorsque vous démarrez votre PC, un texte vous indique le bouton sur lequel vous devez appuyer pour entrer dans le BIOS UEFI. Appuyez dessus ! (Le bouton exact nécessaire et la conception du panneau de contrôle UEFI de chaque carte mère diffèrent, c’est pourquoi ces instructions seront plus des points de repère que des instructions étape par étape).
3. **Démarrez dans le panneau de contrôle UEFI (si possible) :** Bien que toutes les cartes mères ne proposent pas cette fonction, sur certains modèles, vous pouvez démarrer dans le panneau de contrôle UEFI et utiliser un utilitaire de mise à jour intégré pour vous connecter à Internet et flasher le dernier micrologiciel à partir du serveur du fabricant. Cette fonction extrêmement intéressante rend la mise à jour vers les dernières révisions du micrologiciel aussi facile que possible.

Le processus est un peu plus complexe pour les cartes mères qui ne prennent pas en charge cette fonction.

![](https://leconceptmarketing.com/wp-content/uploads/2023/10/image-12-1024x768.png)

4. **Recherchez la dernière mise à jour du BIOS sur la page d’assistance de votre carte mère :** Allez sur la page d’assistance de votre carte mère sur le site web du fabricant. La dernière mise à jour du BIOS devrait se trouver dans la section d’assistance et de téléchargement.
5. **Téléchargez et décompressez le fichier de mise à jour du BIOS.**
6. **Transférez le fichier de mise à jour sur une clé USB.**
7. **Redémarrez votre ordinateur dans le panneau de contrôle UEFI.**
8. Lancez l’outil de mise à jour du micrologiciel de l’UEFI ou l’outil de flashage et sauvegardez le micrologiciel existant de votre PC sur votre clé USB : Cela vous protège en cas de problème.
9. **Utilisez le même utilitaire UEFI pour sélectionner la nouvelle image du microprogramme que vous avez sauvegardée sur le lecteur flash :** L’exécution de l’utilitaire de mise à jour du microprogramme ne devrait prendre que quelques minutes, mais veillez à ne pas éteindre votre PC pendant ce processus. C’est essentiel.
10. **Une fois le processus de flashage terminé, redémarrez votre ordinateur :** Votre BIOS PC mis à jour est prêt à fonctionner.

Certains fabricants proposent des utilitaires qui peuvent mettre à jour votre puce UEFI directement dans Windows en exécutant un fichier .exe, mais nous recommandons vivement d’utiliser l’une des deux méthodes ci-dessus pour éviter tout problème.

Encore une fois, la mise à jour du BIOS de votre PC peut présenter de nombreux avantages, mais il est important d’en comprendre les risques. N’y touchez pas s’il n’y a pas de raison claire et impérieuse de mettre à jour votre micrologiciel UEFI.

Cela dit, si vous souhaitez intégrer un processeur plus récent dans une carte mère plus ancienne, il est clair qu’une mise à jour du BIOS est à prévoir.

→ 🔥 **D’autres articles qui pourraient vous intéresser** :
