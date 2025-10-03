# 🎧 Spotify Dashboard – Análisis de Churn

Este proyecto forma parte de un taller práctico cuyo objetivo es recorrer el **ciclo completo de trabajo con datos**: desde la obtención de un dataset público, su carga en una base de datos relacional y la construcción de un **dashboard interactivo** en una notebook.

---

## 📊 Dataset seleccionado
- **Nombre:** Dataset de Spotify para Análisis de Cancelación (Churn)  
- **Fuente:** [Kaggle – Spotify Dataset for Churn Analysis](https://www.kaggle.com/datasets/nabihazahid/spotify-dataset-for-churn-analysis/data)  
- **Descripción:** Dataset ficticio de usuarios de Spotify con información sobre edad, género, país, tipo de suscripción, hábitos de escucha y la variable `is_churned` que indica si el usuario canceló su suscripción (1) o se mantiene activo (0).  

---

## 🗄️ Motor de base de datos elegido
- **Motor:** SQLite  
- **Motivo:** Es un motor **relacional, ligero y portable**, no requiere instalación de servidor y está incluido en Python.  
- **Esquema de la tabla:**

```sql
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
    offline_listening INTEGER, -- 0/1
    is_churned INTEGER         -- 0/1
);
```
---

## 📓 Pasos para ejecutar el dashboard 

Google Colab (recomendada)

Abrir la notebook dashboard.ipynb en Google Colab.
Subir el archivo data/spotify_churn_dataset.csv o montarlo desde Google Drive.
Ejecutar todas las celdas:
- Se crea la base spotify.db.
- Se cargan los datos.
- Se generan las visualizaciones interactivas

---

## 📦 Dependencias

- **Python 3.9+**
- **pandas**
- **plotly**
- **ipywidgets**
- **sqlite3 (incluido en Python)**

---

## 👨‍💻 Autores

**Pablo Ariel, Blanco Cuevas**