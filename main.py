import os
import sys
from sql_validator import validate_sql
from executor import execute_sql

BRANCH = os.getenv("GITHUB_REF", "refs/heads/development")
SCRIPT_LIST = "scripts_PRO.txt" if BRANCH == "refs/heads/main" else "scripts_DEV.txt"

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
        print(f"🔍 Validando: {script}")
        is_valid, errors, line_count = validate_sql(script)

        if not is_valid:
            print("❌ Errores encontrados:")
            for e in errors:
                print(f"Línea {e['line']}: {e['message']}")
            return

        print("✅ Sintaxis válida. Ejecutando...")
        execute_sql(script)

if __name__ == "__main__":
    main()
