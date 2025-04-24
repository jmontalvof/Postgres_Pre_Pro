# main.py
import os
import psycopg2
from datetime import datetime
from enviar_log_por_correo import enviar_log_por_correo

def log(mensaje, log_path):
    with open(log_path, "a") as f:
        f.write(mensaje + "\n")
    print(mensaje)

def validar_sintaxis_sql(file_path):
    with open(file_path, "r") as f:
        sql = f.read()
    return ";" in sql  # validación muy básica

def ejecutar_sql(script_path, conn, log_path):
    log(f"🔍 Validando: {script_path}", log_path)
    if not validar_sintaxis_sql(script_path):
        log(f"❌ Sintaxis inválida en {script_path}", log_path)
        return

    try:
        with open(script_path, "r") as f:
            sql = f.read()

        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
        log(f"✅ Script ejecutado correctamente: {script_path}", log_path)
    except Exception as e:
        log(f"❌ Error ejecutando el script {script_path}: {e}", log_path)

def main():
    entorno = os.getenv("ENTORNO", "Master-Pre")
    log_file = "logs/pre.log" if "Pre" in entorno else "logs/pro.log"

    os.makedirs("logs", exist_ok=True)

    log(f"🚀 Iniciando despliegue en entorno {entorno}", log_file)

    db_params = {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT")
    }

    script_file = "src/scripts_dev.txt" if "Pre" in entorno else "src/scripts_PRO.txt"

    try:
        conn = psycopg2.connect(**db_params)
        with conn:
            with open(script_file, "r") as f:
                for line in f:
                    script_path = line.strip()
                    if script_path:
                        ejecutar_sql(script_path, conn, log_file)
    except Exception as e:
        log(f"❌ Error de conexión a la base de datos: {e}", log_file)
    finally:
        if 'conn' in locals():
            conn.close()

    enviar_log_por_correo(log_file, entorno=entorno)

if __name__ == "__main__":
    main()
