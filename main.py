import os
from enviar_log_por_correo import enviar_log_por_correo
import smtplib
from email.message import EmailMessage
from datetime import datetime
import sys
from sql_validator import validate_sql
from executor import execute_sql

BRANCH = os.getenv("GITHUB_REF", "refs/heads/development")
SCRIPT_LIST = "scripts_PRO.txt" if BRANCH == "refs/heads/main" else "scripts_DEV.txt"

def enviar_log_por_correo(log_path, entorno):
    asunto = f"Postgres_Pre_Pro | Date: {datetime.now().strftime('%Y-%m-%d')} | Entorno: {entorno}"
    cuerpo = f"Adjunto encontrarás el log de ejecución para el entorno {entorno}."

    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_DESTINO")
    msg.set_content(cuerpo)

    with open(log_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="plain", filename=os.path.basename(log_path))

    with smtplib.SMTP_SSL(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)
        print(f"📧 Log enviado por correo: {asunto}")

def main():
    if not os.path.exists(SCRIPT_LIST):
        print(f"❌ El archivo {SCRIPT_LIST} no existe.", file=sys.stderr)
        print(f"❌ El archivo {SCRIPT_LIST} no existe.")
        exit(1)

    with open(SCRIPT_LIST, "r") as f:
        scripts = [line.strip() for line in f if line.strip()]

    if not scripts:
        print(f"❌ El archivo {SCRIPT_LIST} está vacío. No hay scripts que ejecutar.", file=sys.stderr)
        print(f"❌ El archivo {SCRIPT_LIST} está vacío. No hay scripts que ejecutar.")
        exit(1)

    for script in scripts:
        script_path = os.path.join("src", script)
        print(f"🔍 Validando: {script_path}")
        is_valid, errors, line_count = validate_sql(script_path)

        if not is_valid:
            print("❌ Errores encontrados:")
            for e in errors:
                print(f"Línea {e['line']}: {e['message']}")
            return

        print("✅ Sintaxis válida. Ejecutando...")
        execute_sql(script_path)

if __name__ == "__main__":
    main()
      # Enviar el log por correo al finalizar
    log_file = "logs/pro.log"
    enviar_log_por_correo(log_file, entorno="Master-Pro")
