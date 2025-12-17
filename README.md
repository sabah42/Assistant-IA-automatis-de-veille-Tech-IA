# Assistant IA de veille Tech / IA

## Table des matières
- [Description du projet](#description-du-projet)
- [Contenu du projet](#contenu-du-projet)
- [Objectifs du projet](#objectifs-du-projet)
- [Structure du projet](#structure-du-projet)
- [Étapes principales](#étapes-principales)
- [Principaux insights](#principaux-insights)
- [Recommandations](#recommandations)
- [Compétences utilisées](#compétences-utilisées)
- [Résultats](#résultats)
- [Installation et exécution](#installation-et-exécution)

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

## Structure du projet

ai_news_assistant/

├──  data/ # fichiers de données (news brutes)

├──  reports/  # rapports générés

├──  src/ # code source du projet

│  ├── fetch_news.py # récupération des news via RSS

│  ├── analyze.py  # analyse de base avec pandas

│  ├── ai_summary.py  # résumé des news via IA (Groq)

│  ├── report.py  # génération d'un rapport Markdown

│  └── config.py # configuration (chemins, flux RSS, etc.)

├──  main.py # Lancement du pipeline

└──  README.md

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

## Résultats
Les fichiers générés sont :
- data/raw_news.csv : actualités brutes récupérées depuis les flux RSS ;
- reports/report_YYYY-MM-DD_HH-MM.md : rapport Markdown avec statistiques et résumé IA.

## Installation et exécution

```bash
python -m venv venv # Créer un environnement virtuel (recommandé)
venv\Scripts\activate # Activation
pip install -r requirements.txt # Installer les dépendances
pip install pandas feedparser python-dotenv requests schedule groq
Créer un fichier `.env` à la racine du projet (non versionné dans Git) # GROQ_API_KEY=ta_cle_api_groq_ici
python main.py # Lancer le pipeline

