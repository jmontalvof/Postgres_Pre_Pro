from sqlfluff.core import Linter

def validate_sql(path):
    linter = Linter(dialect="postgres")  # Forzamos el dialecto aquí directamente
    result = linter.lint_path(path)

    errors = []
    for v in result.get_violations():
        errors.append({"line": v.line_no, "message": v.desc})

    with open(path, "r") as f:
        lines = f.readlines()

    return len(errors) == 0, errors, len(lines)
