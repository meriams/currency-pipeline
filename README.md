# 💱 Currency Pipeline – Daglige valutakurser fra Danmarks Nationalbank 🇩🇰

Et simpelt Python-baseret data engineering-projekt, der henter valutakurser fra Danmarks Nationalbank, transformerer og gemmer dataen i en SQLite-database.

Projektet er bygget med fokus på struktur, automatisering og real-world data workflows.

---

## 🧰 Teknologier

- Python 3
- Pandas
- SQLite
- Requests
- XML parsing (`ElementTree`)
- Git + GitHub

---

## 📁 Projektstruktur

- `currency-pipeline/`  
  - `scripts/`  
    - `fetch_data.py` – Henter valutadata fra Nationalbankens XML-API  
    - `load_data.py` – Indlæser data i en SQLite-database  
  - `db/`  
    - `exchange_rates.db` – Lokal database med valutakurser  
  - `run_pipeline.py` – Kører hele pipelinen  
  - `read_db.py` – Læser og viser data fra databasen  
  - `requirements.txt` – Python-afhængigheder  
  - `README.md` – Projektbeskrivelse og guide