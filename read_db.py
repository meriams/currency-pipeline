# read_db.py

import sqlite3
import pandas as pd

def read_db():
    conn = sqlite3.connect("db/exchange_rates.db")
    df = pd.read_sql_query("SELECT * FROM exchange_rates", conn)
    conn.close()
    
    print("📊 Første 5 rækker i databasen:")
    print(df.head())

    print("\n💰 Dagens højeste valutakurser:")
    today = df["date"].max()
    top_today = df[df["date"] == today].sort_values(by="rate", ascending=False)
    print(top_today.head())

if __name__ == "__main__":
    read_db()
