import os 
from textwrap import shorten
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
from .config import LANG
from pathlib import Path
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_context_from_articles(df: pd.DataFrame, max_chars : int = 6000)-> str :
    """ Construit un texte avec titres + résumés pour le prompt IA."""
    if df.empty:
        return "Aucun article disponible"
    lines= [] #Liste qui va contenir les articles sous forme de texte.
    for _,row in df.iterrows():
        title = row.get("title","")
        summary = row.get("summary","")
        line = f" =Titre :{title}\n Résumé : {summary}"
        lines.append(line)# Chaque article devient un petit bloc texte clair pour l’IA
    full_text="\n\n".join(lines)# On assemble tous les articles en un seul texte
    ## On coupe pour ne pas envoyer un prompt trop long
    full_text = shorten(full_text, width=max_chars, placeholder= "...\n[text coupé]")
    return full_text
def summarize_articles(df_recent: pd.DataFrame) -> str:
    """ Demande à l'IA de résumé les news récentes"""
    context = build_context_from_articles(df_recent)
    if LANG == "fr":
        system_msg= (
            "Tu es un assisatant qui résume des actualités en français."
            "Donne un résumé clair, structuré en puces, avec les grandes tendances, "
            "et mentionne les sujets les plus importants."
        )

        user_msg= (
            "Voici des actualités récentes autour de la tech et de l'IA. \n\n"
            "Résume-les en français en :\n "
            "- listant 3 à 5 tendances principales\n"
            "- donnant des exemples concrets_n"
            "- restant concise. \n\n"
            f"ACTUALIÉS :\n{context}"
        )
    else:
        system_msg = "You are an assistant summarizing tech/AI news."
        user_msg = f"Summarize the following news:\n\n{context}"
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.4,
        max_tokens=300,
    
    )
    return response.choices[0].message.content#On récupère le texte généré par l’IA


def run_ai_summary(df_recent: pd.DataFrame) -> str:
    if df_recent is None or df_recent.empty:
        print("Pas d'articles récents pour le résumé IA.")
        return ""
    print("\n=== Étape 3 : résumé IA des news via Groq (gratuit)===")
    summary = summarize_articles(df_recent)
    print(summary)
    return summary
if __name__ == "__main__":
    pass
  
    

