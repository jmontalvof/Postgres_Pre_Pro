import os
import psycopg2

def execute_sql(script_path):
    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT", "5432")

    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        with open(script_path, "r") as f:
            sql = f.read()
            cursor.execute(sql)
            connection.commit()
        print("✅ Script ejecutado correctamente.")
    except Exception as e:
        print(f"❌ Error ejecutando el script: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
