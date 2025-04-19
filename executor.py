
import os
import psycopg2

def execute_sql(path):
    config = {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT")
    }

    with open(path, "r") as f:
        query = f.read()

    try:
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("✅ Script ejecutado correctamente.")
    except Exception as e:
        print("❌ Error ejecutando el script:", str(e))
    finally:
        cursor.close()
        conn.close()
