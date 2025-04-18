import openai
import os
import argparse

# Cargar la API key desde el entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def corregir_sql(error_msg, sql_original):
    prompt = f"""
Eres un asistente experto en SQL. Se ha producido el siguiente error al ejecutar el siguiente script:

--- ERROR ---
{error_msg}

--- SCRIPT ORIGINAL ---
{sql_original}

Corrige el script para que sea válido y funcional, manteniendo el propósito original. Devuelve solo el nuevo script SQL corregido, sin explicaciones ni comentarios.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message['content'].strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--error', required=True, help='Mensaje de error')
    parser.add_argument('--file', required=True, help='Archivo SQL original')
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"❌ Archivo no encontrado: {args.file}")
        return

    with open(args.file, 'r') as f:
        sql_original = f.read()

    print("🔍 Enviando script con error al modelo GPT...")
    script_corregido = corregir_sql(args.error, sql_original)

    new_file = args.file.replace('.sql', '_fix.sql')
    with open(new_file, 'w') as f:
        f.write(script_corregido)

    print(f"✅ Script corregido guardado en: {new_file}")

if __name__ == "__main__":
    main()

