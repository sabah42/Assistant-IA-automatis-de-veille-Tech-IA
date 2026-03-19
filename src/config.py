import os # Operating System sert à communiquer avec l'ordinateur (créer des dossiers,manipuler des fichiers (lire, écrire, supprimer)).
# Langue principale (pour les prompts IA, etc.)
LANG = "fr"
# Flux RSS de news IA / Tech (tu pourras en ajouter)
#Ce sont les liens vers les flux RSS que mon script va lire
RSS_FEEDS = [
    # USA / Global
    "https://www.techbuzz.ai/api/rss/articles",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
    "https://www.wired.com/feed/tag/artificial-intelligence",

    # Europe
    "https://www.zdnet.fr/feeds/rss/actualites/",
    "https://www.lemonde.fr/intelligence-artificielle/rss_full.xml",

    # Business / IA
    "https://venturebeat.com/category/ai/feed/",
    "https://www.analyticsvidhya.com/feed/",
]

# Dossiers de données et rapports
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#sert à savoir où se trouve le fichier config.py


DATA_DIR = os.path.join(BASE_DIR, "data")#Ça permet d’écrire dans ces dossiers sans se tromper.
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# Fichier principal où on enregistre les news brutes
RAW_NEWS_CSV = os.path.join(DATA_DIR, "raw_news.csv") #C’est le fichier où ton script enregistrera toutes les news récupérées
DASHBOARD_SUMMARY_CSV = os.path.join(DATA_DIR, "dashboard_summary.csv")