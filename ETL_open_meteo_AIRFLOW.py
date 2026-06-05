
import pandas as pd
import requests
import psycopg2 
import json
from datetime import datetime
from etl_config import DB_CONFIG, CITIES


# =============================
# CONFIG
# =============================

def get_connection(): #tạo kết nối đến DB dựa trên Config
    return psycopg2.connect(**DB_CONFIG)


# =============================
# EXTRACT
# =============================

def extract(lat,lon):
    url_extracted = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        responses = requests.get(url_extracted, timeout = 30)
        responses.raise_for_status()
        return responses.json()
    except requests.RequestException as e:
        print(f"Failed at {e}")
        raise

# =============================
# LOADRAW
# =============================

def load_raw(conn, city, lat, lon, data): #conn = get_connection ở run_etl/ data = extract(lat,lon)
    query = """
    INSERT INTO raw.weather_forcast(city, lat, lon, data_json)
    VALUES(%s,%s,%s,%s)
"""
    with conn.cursor() as cursor:
        cursor.execute(query, (city, lat, lon, json.dumps(data)))
    


# =============================
# TRANSFORM
# =============================

def transform(city, lat, lon, data): #Tạo 1 tuple chứa các thông số kĩ thuật, trong đó time cần trả về đúng datetime
    Time_value = data.get("current_weather", {}).get("time")
    if Time_value is not None:
        Time_value = datetime.fromisoformat(Time_value)
    return(
        city,
        lat,
        lon,
        Time_value,
        data.get("current_weather", {}).get("temperature"),
        data.get("current_weather", {}).get("windspeed"),
        data.get("current_weather", {}).get("winddirection")
    )

# =============================
# LOAD
# =============================

def load(conn, row):
    query = """
    INSERT INTO stagging.weather_forcast(city, lat, lon, datetime, temp, wind_speed, wind_direction)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
"""
    with conn.cursor() as cursor:
        cursor.execute(query, row) #query: table trong database/ row = def transform

# =============================
# MAIN
# =============================

def run_etl():
    conn = None

    try:
        conn = get_connection()

        for city_info in CITIES:
            lat = city_info["lat"]
            lon = city_info["lon"]
            city = city_info["name"]

            print(f"Processing: {city}")

            #etract:
            data = extract(lat,lon)

            #Load_raw
            load_raw(conn, city, lat, lon, data)

            #Transform
            row = transform(city, lat, lon, data)

            #load
            load(conn, row)
            conn.commit()
        print("ETL done")

    except Exception as f:
        if conn is not None:
            conn.rollback()
        print(f"Failed at {f}")
        raise
    finally:
        if conn is not None:
            conn.close()

# =============================
# RUN
# =============================

if __name__ == "__main__":
    run_etl()

