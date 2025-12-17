import os
from datetime import datetime
import feedparser
import pandas as pd
from .config import RSS_FEEDS, DATA_DIR, RAW_NEWS_CSV
def ensure_data_dir(): #crée le dossier data/ si celui-ci n’existe pas
    os.makedirs(DATA_DIR,exist_ok=True) # pour être sûr qu’on peut écrire le fichier CSV sans erreur.

def parse_feed(url:str):
    """Récupère et normalise les entrées d'un flux RSS."""
    feed=feedparser.parse(url) #lit le flux RSS à partir de l’URL et le transforme en objet Python.
    items=[] #on crée une liste vide pour stocker chaque article qu’on va récupérer.
    # On veut savoir quelle est la source des articles
    source_title=feed.feed.get("title","").strip() if "feed" in feed else url

    for entry in feed.entries: # feed.entries contient tous les articles du flux RSS.
        title= entry.get("title","").strip()
        link= entry.get("link","").strip()
        summary= entry.get("summary","").strip()
    # On crée une variable pour stocker la date de publication de l’article.
        published_dt = None # On initialise à None au cas où la date n’est pas disponible
    # --- Récupération de la date ---
    # convertir la date de l’article en objet datetime Python pour pouvoir trier et analyser.
        if hasattr(entry, "published_parsed") and entry.published_parsed: # updated_parsed et published_parsed sont des formats structurés fournis par feedparser et la on Vérifie si la date existe dans un format clair.
            published_dt = datetime(*entry.published_parsed[:6]) #convertit un tuple (année, mois, jour, heure, minute, seconde) en objet datetime.
        elif hasattr(entry, "updated_parsed") and entry.updated_parsed:#Vérifier un autre format possible
            published_dt = datetime(*entry.updated_parsed[:6])
        
        else:# Sinon, on essaye de parser une chaîne brute avec pandas.to_datetime.lire le texte brut
             # certain flux mettent une date sous forme de texte Donc on tente de lire ça
            raw_date= entry.get("published", "") or entry.get("updated", "")
            if raw_date :# Puis pytz/pandas essaie de la convertir automatiquement
                try:
                    published_dt = pd.to_datetime(raw_date, errors="coerce")
                except Exception: #Si aucun format ne marche
                    published_dt=None    


  # On crée un dictionnaire pour chaque article
        items.append(
            { "source": source_title,
             "feed_url":url ,
             "title" : title ,
             "link" : link ,
             "summary" : summary ,
             "published" : published_dt}
        )

    return items #La fonction renvoie une liste de dictionnaires, prête à être transformée en DataFrame ou analysée.
##Appelle parse_feed() pour CHAQUE flux dans la liste RSS_FEEDS, combine tout, nettoie et trie
def fetch_all_feeds() -> pd.DataFrame:
    """Boucle sur tous les flux RSS et concatène les résultats dans un DataFrame."""
    all_items = []#Création d’une liste pour stocker tous les articles
    for url in RSS_FEEDS:
        print(f"Récupération du flux : {url}")#on affiche le flux qu'on est en train de traiter (juste pour suivre l’exécution
        try:
            items = parse_feed(url)#retourne une liste d’articles (chaque article est un dictionnaire)
            all_items.extend(items)# ajoute ces articles à la grande liste all_items
        except Exception as e:
            print(f"Erreur sur le flux {url}: {e}")#Cela évite que mon script s’arrête si un seul flux est cassé
    df = pd.DataFrame(all_items)# on transforme la liste de dictionnaires en un tableau Pandas
    if not df.empty:
        # Supprimer les doublons sur titre + source
        df.drop_duplicates(subset=["source", "title"], inplace=True)
        # Tenter de trier par date
        if "published" in df.columns:
            df["published"] = pd.to_datetime(df["published"], errors="coerce")
            df.sort_values(by="published", ascending=False, inplace=True)
    return df
def save_raw_news(df: pd.DataFrame):
    """Sauvegarde le DataFrame dans un CSV."""
    ensure_data_dir()#elle vérifie si le dossier data/ existe sinon elle le crée automatiquement
    df.to_csv(RAW_NEWS_CSV, index=False, encoding="utf-8")
    print(f"{len(df)} articles sauvegardés dans {RAW_NEWS_CSV}")#Afficher combien d’articles ont été sauvegardés
    
def run_fetch():
    """Fonction appelée par main.py pour cette étape."""
    df = fetch_all_feeds()
    if df.empty:
        print("Aucun article récupéré. Vérifie les flux RSS.")
    else:
        print(df[["source", "title", "published"]].head())
        save_raw_news(df)
if __name__ == "__main__":
        run_fetch()