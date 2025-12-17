import os # Operating System sert à communiquer avec l'ordinateur (créer des dossiers,manipuler des fichiers (lire, écrire, supprimer)).
# Langue principale (pour les prompts IA, etc.)
LANG = "fr"
# Flux RSS de news IA / Tech (tu pourras en ajouter)
#Ce sont les liens vers les flux RSS que mon script va lire
RSS_FEEDS = [
    "https://www.techbuzz.ai/api/rss/articles",
    "https://www.wired.com/feed/tag/artificial-intelligence/",
]

# Dossiers de données et rapports
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#sert à savoir où se trouve le fichier config.py


DATA_DIR = os.path.join(BASE_DIR, "data")#Ça permet d’écrire dans ces dossiers sans se tromper.
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# Fichier principal où on enregistre les news brutes
RAW_NEWS_CSV = os.path.join(DATA_DIR, "raw_news.csv") #C’est le fichier où ton script enregistrera toutes les news récupérées