import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def enviar_log_por_correo(log_file_path, entorno="Pre"):
    remitente = os.getenv("EMAIL_SENDER")
    destinatario = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")
 
    print("📧 Remitente:", remitente)
    print("📧 Destinatario:", destinatario)
    print("📦 Leyendo log desde:", log_file_path)

    if not all([remitente, destinatario, password]):
        print("❌ Faltan variables de entorno: EMAIL_SENDER, EMAIL_RECEIVER o EMAIL_PASSWORD")
        return

    # Asunto con formato
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    asunto = f"Postgres_Pre_Pro: date: {fecha_actual}: Master-{entorno}"

    # Cuerpo del correo con contenido del log
    try:
        with open(log_file_path, "r") as f:
            contenido = f.read()
    except FileNotFoundError:
        contenido = "⚠️ El archivo de log no se encontró."

    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(contenido, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        print(f"📬 Log enviado correctamente a {destinatario}")
    except Exception as e:
        print(f"❌ Error al enviar el correo: {e}")


if __name__ == "__main__":
    log_path = os.getenv("LOG_PATH", "logs/pre.log")
    entorno = os.getenv("ENTORNO", "Master-Pre")
    enviar_log_por_correo(log_path, entorno)
