---
title: "Multi-agent Architecture Search : Un nouveau cadre d’apprentissage automatique qui optimise les systèmes multi-agents"
permalink: "/multi-agent-architecture-search-un-nouveau-cadre-dapprentissage-automatique-qui-optimise-les-systemes-multi-agents/"
legacy_permalinks: ["/?p=24139/"]
type: "post"
date: "2025-02-21T15:11:15+00:00"
modified: ""
author: "Sébastian Magni @ Responsable du contenu"
categories: ["Intelligence artificielle"]
tags: ["MaAS","Multi-agent Architecture Search"]
description: "Pour remédier aux limites des systèmes multi-agents existants, les chercheurs ont proposé MaAS (Multi-agent Architecture Search)"
cover: "https://leconceptmarketing.com/wp-content/uploads/2025/02/image-5.png"
source_url: "https://leconceptmarketing.com/multi-agent-architecture-search-un-nouveau-cadre-dapprentissage-automatique-qui-optimise-les-systemes-multi-agents/"
source_capture: "20250326012127"
---
**Les grands modèles de langage ([LLM](https://www.cloudflare.com/fr-fr/learning/ai/what-is-large-language-model/))** sont à la base des systèmes multi-agents, permettant à plusieurs agents d’intelligence artificielle de collaborer, de communiquer et de résoudre des problèmes. Ces agents utilisent les LLM pour comprendre les tâches, générer des réponses et prendre des décisions, imitant ainsi le travail d’équipe chez les humains.

Cependant, l’efficacité de ces types de systèmes n’est pas au rendez-vous car ils sont basés sur des conceptions fixes qui ne changent pas pour toutes les tâches, ce qui les amène à utiliser trop de ressources pour traiter des problèmes simples et complexes, gaspillant ainsi les calculs et conduisant à une réponse lente.

**👉🏼 Lecture complémentaire :** [Découvrez Midjourney AI Art : Combiner la puissance de l’IA et la créativité d’un artiste](https://leconceptmarketing.com/decouvrez-midjourney-ai-art-combiner-la-puissance-de-lia-et-la-creativite-dun-artiste/)

![](https://leconceptmarketing.com/wp-content/uploads/2025/02/image-5-1024x512.png)

Cela crée donc des défis majeurs lorsqu’il s’agit d’équilibrer la précision, la vitesse et le coût tout en traitant des tâches diversifiées.

Actuellement, les systèmes multi-agents s’appuient sur des méthodes existantes telles que CAMEL, AutoGen, MetaGPT, DsPy, EvoPrompting, GPTSwarm et EvoAgent, qui se concentrent sur l’optimisation de tâches spécifiques telles que le réglage de l’invite, le profilage de l’agent et la communication. Toutefois, ces méthodes se heurtent à des problèmes d’adaptabilité.

Elles suivent des modèles préétablis sans s’adapter aux diverses tâches, ce qui rend le traitement des requêtes simples et complexes quelque peu inefficace. Elles manquent de flexibilité grâce à des approches manuelles, alors qu’un système automatisé ne peut que cibler la recherche de la meilleure configuration sans réajustement dynamique vers l’efficacité.

Cela rend ces méthodes coûteuses en termes de calcul et se traduit par des performances globales inférieures lorsqu’elles sont appliquées à des défis du monde réel.

![l'IA présente MaAS (Multi-agent Architecture Search) : Un nouveau cadre d'apprentissage automatique qui optimise les systèmes multi-agents](https://leconceptmarketing.com/wp-content/uploads/2025/02/image-2-1024x414.png)

Pour remédier aux limites des systèmes multi-agents existants, les chercheurs ont proposé MaAS (Multi-agent Architecture Search). Ce cadre utilise un super-réseau probabiliste d’agents pour générer des architectures multi-agents en fonction des requêtes. Au lieu de sélectionner un système optimal fixe, [MaAS](https://www.maasify.io/mobility-as-a-service/une-definition-simple-du-maas/) échantillonne dynamiquement des systèmes multi-agents personnalisés pour chaque requête, en équilibrant les performances et les coûts de calcul.

**👉🏼 Lecture complémentaire :**

L’espace de recherche est défini par des opérateurs agentiques, qui sont des flux de travail basés sur LLM impliquant de multiples agents, outils et invites.

Le super-réseau apprend une distribution des architectures agentiques possibles, en l’optimisant en fonction de l’utilité de la tâche et des contraintes de coût. Un réseau de contrôleurs échantillonne les architectures en fonction de la requête, en utilisant un mécanisme de type mélange d’experts (MoE) pour une sélection efficace. Le cadre effectue l’optimisation par le biais d’un Monte Carlo Bayes empirique tenant compte des coûts, en mettant à jour les opérateurs agentiques à l’aide de méthodes textuelles basées sur le gradient.

Le cadre fournit une évolution multi-agents automatisée, permettant l’efficacité et l’adaptabilité lors du traitement de requêtes diverses et complexes.

**👉🏼 Lecture complémentaire :**

![l'IA présente MaAS (Multi-agent Architecture Search) : Un nouveau cadre d'apprentissage automatique qui optimise les systèmes multi-agents](https://leconceptmarketing.com/wp-content/uploads/2025/02/image-3-1024x386.png)

Les chercheurs ont évalué MaAS sur six benchmarks publics concernant le raisonnement mathématique (GSM8K, MATH, MultiArith), la génération de code (HumanEval, MBPP) et l’utilisation d’outils (GAIA), en le comparant à 14 références, dont des méthodes à agent unique, des systèmes multi-agents fabriqués à la main et des approches automatisées.

MaAS a constamment surpassé toutes les références, obtenant un meilleur score moyen de 83,59 % pour l’ensemble des tâches et une amélioration significative de 18,38 % pour les tâches de niveau 1 de GAIA.

L’analyse des coûts a montré que MaAS est économe en ressources, nécessitant le moins de jetons de formation, les coûts d’API les plus bas et le temps le plus court. Des études de cas ont mis en évidence son adaptabilité dans l’optimisation dynamique des flux de travail multi-agents.

![l'IA présente MaAS (Multi-agent Architecture Search) : Un nouveau cadre d'apprentissage automatique qui optimise les systèmes multi-agents](https://leconceptmarketing.com/wp-content/uploads/2025/02/image-6-1022x1024.png)

En résumé, la méthode a permis de résoudre les problèmes des systèmes multi-agents traditionnels en utilisant un super-réseau d’agents qui s’adapte aux différentes requêtes. Cela a permis au système de mieux fonctionner, d’utiliser les ressources à bon escient et de devenir plus flexible et évolutif.

Dans les travaux futurs, [le MaAS](https://www.maasify.io/mobility-as-a-service/une-definition-simple-du-maas/) peut être développé en un cadre flexible et étendu pour améliorer l’automatisation et l’auto-organisation. Les travaux futurs pourraient également porter sur l’optimisation des stratégies d’échantillonnage, l’amélioration de l’adaptabilité au domaine et l’incorporation des contraintes du monde réel pour stimuler l’intelligence collective.

**👉🏼 Lecture complémentaire :**
