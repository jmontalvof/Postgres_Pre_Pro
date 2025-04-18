import os
import openai
import sys
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def corregir_sql(file_path):
    with open(file_path, 'r') as f:
        contenido = f.read()

    prompt = f"""
Corrige el siguiente código SQL. Devuelve solo el SQL corregido sin comentarios adicionales ni explicación:

{contenido}
"""

    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en SQL que corrige errores de sintaxis."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return respuesta.choices[0].message.content.strip()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python fix_sql.py archivo_entrada.sql archivo_salida.sql")
        sys.exit(1)

    entrada, salida = sys.argv[1], sys.argv[2]
    sql_corregido = corregir_sql(entrada)

    with open(salida, 'w') as f:
        f.write(sql_corregido)

    print(f"✅ SQL corregido guardado en {salida}")
