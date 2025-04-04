import sqlite3

def load_to_db(df, db_path="db/exchange_rates.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("exchange_rates", conn, if_exists="append", index=False)
    conn.close()