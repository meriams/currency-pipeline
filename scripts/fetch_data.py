# scripts/fetch_data.py

import requests
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime

def fetch_exchange_rates():
    url = "https://www.nationalbanken.dk/_vti_bin/DN/DataService.svc/CurrencyRatesXML?lang=en"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        # Find dato (fra dailyrates)
        daily_rates = root.find(".//dailyrates")
        date_str = daily_rates.attrib["id"]
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # Hent valutakurser
        records = []
        for currency in daily_rates.findall("currency"):
            code = currency.attrib["code"]
            rate = float(currency.attrib["rate"])
            desc = currency.attrib["desc"]

            records.append({
                "date": date,
                "currency": code,
                "description": desc,
                "rate": rate,
                "base": "DKK"
            })

        df = pd.DataFrame(records)
        return df
    else:
        raise Exception(f"API request failed with status code {response.status_code}")
