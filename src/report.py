import os
from datetime import datetime
import pandas as pd 
from .config import REPORTS_DIR
def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def generate_markdown_report(df_recent:pd.DataFrame, stats: dict, ai_summary:str) -> str:
    """ Génère un rapport Markdown et retourne le chemin du fichier"""
    ensure_reports_dir()
    now = datetime.now()
    date_str=now.strftime("%Y-%m-%d_%H-%M")
    filename=f"report_{date_str}.md" # chaque rapport a un nom unique
    filepath= os.path.join(REPORTS_DIR, filename)
    nb_articles = stats.get("nb_articles", 0)
    nb_sources = stats.get("nb_sources", 0)
    articles_par_source = stats.get("articles_par_source",{})
    top_mots = stats.get ("top_mots",[])

    lines = []
    lines.append(f" # Rapport de veille Tech / IA - {now.strftime('%Y- %m-%d %H:%M')}\n")
    lines.append("## 1. Statistiques génerales/n")
    lines.append(f"- Nombre d'articles récents : **{nb_articles}**")
    lines.append(f"- Nombre de sources : **{nb_sources}**")        
    lines.append("### articles par source\n")
    for src, n in articles_par_source.items():
        lines.append(f" - {src} : {n} articles")
    lines.append("")

    lines.append("### Top mots-clé (titres\n")
    for mot, count in top_mots:
        lines.append(f"- **{mot}** : {count}")
    lines.append("")
    lines.append("## 2. Résumé IA des actualités \n")
    if ai_summary:
        lines.append(ai_summary)
    else:
        lines.append("_Aucun résumé IA disponible._")
    lines.append("")

    lines.append("## 3. Liste des articles récents \n")
    if df_recent is not None and not df_recent.empty:
        for _, row in df_recent.iterrows():
            title = row.get("title","")
            src = row.get("source", "")
            link = row.get("link", "")
            published = row.get("published", "")
            lines.append(f"- **{title}** ({src}, {published})\n - lien : {link}")
    else:
        lines.append("_Aucun article récent._")

    content = "\n".join(lines)    #On transforme la liste en un seul texte   
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n Rapport généré : {filepath}")
    return filepath
def run_report(df_recent: pd.DataFrame, stats: dict, ai_summary: str) -> str:
    return generate_markdown_report(df_recent, stats, ai_summary)

if __name__ == "__main__":
    pass