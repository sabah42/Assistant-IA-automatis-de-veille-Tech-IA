from datetime import datetime, timedelta
from collections import Counter
import re
import pandas as pd
from .config import RAW_NEWS_CSV

def load_raw_news()-> pd.DataFrame:
    """Charger le csv des news brutes """
    try:
        df=pd.read_csv(RAW_NEWS_CSV,parse_dates=["published"] )
        return df
    except FileNotFoundError:
        print("Fichier raw_news.csv introuvable. Lance d'abord la récupération des news.")
        return pd.DataFrame()
def filter_recent(df: pd.DataFrame, days: int = 1)->pd.DataFrame:
    """ Garder uniquement les articles des Xdernier jours"""
    if df.empty:
        return df
    now = datetime.utcnow() #date/heure actuelle
    cutoff= now - timedelta(days=days)
    df_recent=df.copy()
    df_recent["published"]= pd.to_datetime(df_recent["published"],errors="coerce")
    df_recent = df_recent[df_recent["published"]>= cutoff]
    return df_recent
 
def get_basic_stats(df:pd.DataFrame)-> dict:
    """ Retourne quelques stats simples sur lrs articles """
    if df.empty:
        return {
            "nb_articles" :0,
            "nb_sources":0,
            "articles_par_source": {},
            "top_mots":[],

        }
    nb_articles = len(df)
    nb_sources  = df["source"].nunique()
    articles_par_source = df["source"].value_counts().to_dict()
    # Petit top mots-clés très simple sur les titres
    text= " ".join(df["title"].dropna().tolist()).lower()
    # On enlève les caractères spéciaux
    words=re.findall(r"[a-zA-Zàâçéèêëîïôûùüÿñæœ0-9]+", text)
    stopwords = {
        "the", "and", "for", "with", "from", "this", "that", "les", "des", "une", "un",
        "dans", "sur", "aux", "pour", "qui", "est", "ses", "nos", "vos", "ces", "par",
        "de", "la", "le", "du", "en", "et", "a", "an", "to", "of", "on", "ai"
    } #On enlève les petits mots inutiles

    filtered_words = [w for w in words if w not in stopwords and len(w) > 2]
    counter= Counter(filtered_words)
    top_mots = counter.most_common(10)
    return {
        "nb_articles": nb_articles,
        "nb_sources": nb_sources,
        "articles_par_source": articles_par_source,
        "top_mots": top_mots,
    }
def run_analyze(days: int=1):
    df= load_raw_news()
    if df.empty:
        return None, None
    df_recent= filter_recent(df, days=days)
    stats= get_basic_stats(df_recent)
    print("=== Stats basiques ===")
    print(f"Nombre d'articles (sur {days} jour(s)) : {stats['nb_articles']}")
    print(f"Nombre de sources différentes : {stats['nb_sources']}")
    print("Articles par source :")
    for src, n in stats["articles_par_source"].items():
        print(f"  - {src}: {n}")
    print("Top mots-clés (titres) :")
    for mot, count in stats["top_mots"]:
        print(f"  - {mot}: {count}")
    return df_recent, stats

if __name__ == "__main__":
    run_analyze()