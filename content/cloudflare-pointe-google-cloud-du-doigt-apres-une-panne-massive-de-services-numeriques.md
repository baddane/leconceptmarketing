---
title: "Cloudflare pointe Google Cloud du doigt après une panne massive de services numériques"
permalink: "/cloudflare-pointe-google-cloud-du-doigt-apres-une-panne-massive-de-services-numeriques/"
legacy_permalinks: []
type: "post"
date: "2025-06-13T11:41:36+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Le Journal E-marketing"]
tags: ["Cloudflare","Google Cloud","cloudflare status","une panne","La panne de Google Cloud"]
description: "Panne massive du cloud le 12 juin 2025 Google Cloud et Cloudflare accusés de dysfonctionnements ayant impacté Spotify Discord et d’autres plateformes Analyse complète de l’incident et de ses implications"
cover: "https://leconceptmarketing.com/wp-content/uploads/2025/06/Cloudflare.webp"
source_url: "https://leconceptmarketing.com/cloudflare-pointe-google-cloud-du-doigt-apres-une-panne-massive-de-services-numeriques/"
source_capture: "20250714223953"
---
## Une interruption majeure des services numériques touche plusieurs géants du cloud

Le 12 juin 2025 une panne de grande ampleur a secoué l’écosystème numérique mondial affectant simultanément les services de Cloudflare Google Cloud ainsi que plusieurs applications tierces très utilisées à l’échelle mondiale Parmi les plateformes impactées figurent notamment Spotify Discord Snapchat et Vimeo bien que le lien de causalité direct avec l’incident principal demeure incertain La société Cloudflare spécialisée dans la distribution de contenu et la cybersécurité a rapidement attribué cette panne à une défaillance survenue dans l’infrastructure de[ Google Cloud ](https://cloud.google.com/)Un porte-parole de Cloudflare a affirmé dans un communiqué adressé à CRN que cette panne provenait de Google Cloud Un nombre limité de services de Cloudflare utilisent l’infrastructure de Google Cloud et ont donc été affectés Cependant les services centraux de Cloudflare ont continué à fonctionner normalement et n’ont pas été compromis

## Une défaillance critique du service KV de Cloudflare

La société Cloudflare a publié une mise à jour sur sa page de statut à 19h57 UTC indiquant que tous ses services étaient à nouveau pleinement opérationnels Elle a précisé qu’elle surveillait encore activement ses indicateurs de performance pour s’assurer d’une stabilité durable L’incident a été attribué à une défaillance d’un service tiers considéré comme une dépendance clé pour le service [Workers KV de Cloudflare](https://developers.cloudflare.com/kv/) qui est essentiel pour le stockage et la diffusion de données Cette défaillance a rendu indisponibles plusieurs produits Cloudflare dépendant de ce service Parmi les services affectés figuraient Access WARP Realtime Workers AI Stream une partie du tableau de bord Cloudflare ainsi que la fonctionnalité AutoRAG Les ingénieurs de l’entreprise se sont mobilisés pour rétablir l’ensemble des services dans les plus brefs délais tout en reconnaissant l’ampleur de l’impact subi par les utilisateurs

## Google Cloud reconnait une perturbation et commence une reprise partielle

Google Cloud de son côté a également fait face à des perturbations majeures sur plusieurs de ses produits clés La société a signalé une perturbation de ses services et a communiqué les mises à jour via son tableau de bord public À 14h00 heure du Pacifique Google a indiqué avoir mis en place une mesure d’atténuation pour la région us-central1 incluant l’Iowa et pour la région multi-region/us L’entreprise a observé des signes de reprise progressive dans ces zones ainsi que dans d’autres régions selon les données internes et les retours clients Elle s’attendait à une récupération complète dans l’heure qui suivait avec une nouvelle mise à jour prévue à 14h30 pour fournir les dernières informations disponibles

## Les données Downdetector confirment l’ampleur de la panne

L’outil de surveillance Downdetector géré par Ookla a enregistré un pic de signalements concernant Google Cloud avec environ 14 000 signalements à 11h25 heure du Pacifique Ce chiffre est redescendu à 3 000 vers 12h40 Pour Cloudflare environ 3 000 rapports ont été recensés à 11h41 avant de diminuer à 1 000 une heure plus tard Ces chiffres témoignent de l’ampleur et de la répercussion de la panne à l’échelle mondiale

## D’autres géants du cloud également touchés mais sans confirmation officielle

Amazon Web Services AWS un concurrent direct de Google Cloud a également connu une augmentation de signalements de pannes atteignant environ 6 000 à 11h55 Cependant son tableau de bord officiel n’a mentionné aucun problème Les signalements ont ensuite diminué à environ 2 000 à 12h40 De son côté Microsoft Azure a enregistré environ 1 000 signalements sur Downdetector à 11h49 sans pour autant refléter de dysfonctionnement sur sa page de statut Ces éléments laissent à penser qu’une fragilité généralisée pourrait exister au sein de plusieurs grandes infrastructures cloud même si toutes n’ont pas été officiellement reconnues

## Chronologie de l’incident chez Cloudflare

La première alerte émise par Cloudflare date de 18h19 UTC lorsque l’entreprise a indiqué qu’elle enquêtait sur un problème ayant un impact sur l’authentification via Access ainsi que sur la connectivité via WARP Zero Trust Un peu plus tard à 19h12 UTC Cloudflare annonçait des signes de reprise des services puis à 19h57 elle confirmait la restauration complète des fonctionnalités Le diagnostic a révélé une défaillance du service KV critique pour plusieurs opérations internes

## Produits Google Cloud affectés par l’incident

Selon le tableau de bord de Google Cloud les services touchés comprenaient notamment Vertex AI Google Cloud SQL Google BigQuery Google Cloud Console Google Cloud DNS Google Identity and Access Management et Google Cloud Storage L’entreprise a reconnu que de nombreux produits de la plateforme connaissaient des niveaux variables d’impact opérationnel notamment au niveau des requêtes API À 12h09 heure du Pacifique Google indiquait que ses ingénieurs poursuivaient les efforts de résolution et confirmaient une amélioration de la situation dans certaines zones géographiques

## Impact potentiel sur les applications tierces

Même si la corrélation directe entre les pannes de Cloudflare et de Google Cloud avec celles de plusieurs applications populaires n’a pas été formellement établie de nombreuses plateformes ont enregistré des interruptions importantes Spotify a atteint 46 000 signalements à 12h02 Discord en a recensé 11 000 à 11h32 Snapchat 7 000 à 12h33 Character AI 4 000 à 11h19 et Vimeo environ 2 000 à 11h51 Ces interruptions simultanées suggèrent un effet domino provoqué par la défaillance des infrastructures critiques sur lesquelles s’appuient ces services

## Conclusion

Cette panne massive soulève une fois de plus la question cruciale de la résilience des services cloud dans un monde de plus en plus dépendant de ces infrastructures Bien que les services centraux de Cloudflare soient restés opérationnels l’incident a montré combien la dépendance à des fournisseurs tiers peut affecter même les géants les mieux préparés L’interconnexion entre les acteurs du cloud la complexité des architectures distribuées et la rapidité avec laquelle une panne peut se propager appellent à une meilleure surveillance à des systèmes de redondance renforcés et à une transparence accrue vis-à-vis des utilisateurs finaux
