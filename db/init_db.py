# db/init_db.py
import sqlite3
import pandas as pd
import os

DB_PATH = os.environ.get("DB_PATH", "spotify.db")
CSV_PATH = os.environ.get("CSV_PATH", "data/spotify_churn_dataset.csv")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS spotify_users (
    user_id INTEGER PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    country TEXT,
    subscription_type TEXT,
    listening_time INTEGER,
    songs_played_per_day INTEGER,
    skip_rate REAL,
    device_type TEXT,
    ads_listened_per_week INTEGER,
    offline_listening INTEGER,
    is_churned INTEGER
);
"""

def main():
    # Crear DB + tabla
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(SCHEMA_SQL)
    conn.commit()

    # Cargar CSV (reemplaza la tabla si ya existe)
    df = pd.read_csv(CSV_PATH)
    df.to_sql("spotify_users", conn, if_exists="replace", index=False)

    conn.close()
    print(f"Base creada en {DB_PATH} con {len(df)} registros.")

if __name__ == "__main__":
    main()
