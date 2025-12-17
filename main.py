import time 
import schedule
# on importe les fonctions passerelles de chaque module
from src.fetch_news import run_fetch
from src.analyze import run_analyze
from src.ai_summary import run_ai_summary
from src.report import run_report


def run_pipeline_once():
    print("=== Pipline de veille IA / Tech ===")
    run_fetch()#récupération des news et Sauvegarde dans data/raw_news.csv
    df_recent, stats = run_analyze(days=1)# charge le CSV, filtre les articles du dernier jour, calcule les statistiques et renvoie : (df_recent → DataFrame stats → dictionnaire)
    ai_summary = run_ai_summary(df_recent) #envoie les articles à l’IA et récupère le résumé
    run_report(df_recent, stats, ai_summary) # génère le rapport Markdown et l’enregistre dans reports/
    print("=== Fin du pipline ===\n")

def run_once_manually():
    """ Mode manuel: exécuter une seule fois."""
    run_pipeline_once()

def run_daily_at(hour: str = "08:00"):
    """ Mode automatique : exécuter tous les jours à l'heure donnée ( format HH : MM)."""
    schedule.every().day.at(hour).do(run_pipeline_once)
    print(f" Tâche planifiée tous les jours à {hour}")

    while True:
        schedule.run_pending()
        time.sleep(30)

         
if __name__ == "__main__":
    # choisis un des deux modes :
    # 1) Je préfère lancer le pipeline manuellement pour démontrer le fonctionnement de bout en bout.
    run_once_manually()
    # 2) (option) Activer le mode automatique : mais Le mode automatique peut poser problème en démo
    #run_daily_at("08:00")