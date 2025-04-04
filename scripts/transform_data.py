# scripts/transform_data.py

import pandas as pd

def transform_exchange_data(raw_data):
    base = raw_data["base"]
    date = raw_data["date"]
    rates = raw_data["rates"]

    df = pd.DataFrame(list(rates.items()), columns=["currency", "rate"])
    df["base"] = base
    df["date"] = pd.to_datetime(date)

    # Sæt rækkefølge
    df = df[["date", "base", "currency", "rate"]]
    return df
