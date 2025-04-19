
import os
from sql_validator import validate_sql
from executor import execute_sql

BRANCH = os.getenv("GITHUB_REF", "refs/heads/development")
SCRIPT_LIST = "scripts_PRO.txt" if BRANCH == "refs/heads/main" else "scripts_DEV.txt"

def main():
    with open(SCRIPT_LIST, "r") as f:
        scripts = [line.strip() for line in f if line.strip()]

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
