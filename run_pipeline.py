# run_pipeline.py

from scripts.fetch_data import fetch_exchange_rates
from scripts.load_data import load_to_db

def run():
    print("🚀 Henter valutadata fra Nationalbanken...")
    df = fetch_exchange_rates()  # <-- fjern base="USD"
    
    print("💾 Gemmer i SQLite database...")
    load_to_db(df)

    print("✅ Pipeline kørt færdig!")

if __name__ == "__main__":
    run()
