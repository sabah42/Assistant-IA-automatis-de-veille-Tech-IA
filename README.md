# Assistant IA de veille Tech / IA

## Table des matières
- [Description du projet](#description-du-projet)
- [Contenu du projet](#contenu-du-projet)
- [Objectifs du projet](#objectifs-du-projet)
- [Étapes principales](#étapes-principales)
- [ Principaux insights](#principaux-insights)
- [Recommandations](#recommandations)
- [Compétences utilisées](#compétences-utilisées)

## Description du projet

Ce projet est un **assistant automatique de veille Tech et IA** développé en Python.  
Il permet de récupérer des actualités, de les analyser, puis de générer un **résumé intelligent** et un **rapport automatique**.
Le but est de montrer comment construire un **pipeline data complet**, avec une intégration simple de l’IA.

## Contenu du projet
Le projet comprend :
- la collecte d’actualités via des flux RSS,
- le stockage des données dans des fichiers CSV,
- l’analyse des articles (sources, mots-clés, volumes),
- la génération d’un résumé intelligent via un modèle d’IA,
- la création automatique d’un rapport Markdown.

## Objectifs du projet
- Automatiser la veille Tech et IA  
- Analyser les articles collectés  
- Identifier les tendances principales  
- Générer un résumé intelligent  
- Produire un rapport automatique et lisible

## Étapes principales

1. Récupération des actualités depuis des flux RSS  
2. Nettoyage et organisation des données  
3. Analyse simple des articles (statistiques et mots-clés)  
4. Génération d’un résumé via un **LLM (modèle d’IA)** exécuté avec **Groq**  
5. Création d’un rapport Markdown horodaté

## Principaux insights

- Les actualités sont récupérées automatiquement sans intervention manuelle  
- Certaines sources publient plus fréquemment que d’autres  
- Des mots-clés récurrents permettent d’identifier les tendances du moment  
- Le résumé IA facilite la compréhension rapide de l’actualité  
- Le rapport final est prêt à être consulté ou partagé 

## Recommandations

- Ajouter davantage de sources d’actualités  
- Améliorer l’analyse du texte (mots-clés plus précis)  
- Ajouter des visualisations (graphiques, dashboard)  
- Automatiser l’exécution quotidienne du pipeline  
- Déployer le projet sur un serveur  

## Compétences utilisées

- Python (structuration de projet, scripts)
- Manipulation de données avec pandas  
- Analyse de texte (NLP simple)  
- Automatisation de pipelines  
- Intégration d’un modèle d’IA (LLM via Groq)  
- Génération de rapports automatisés  
- Gestion d’environnements virtuels  

