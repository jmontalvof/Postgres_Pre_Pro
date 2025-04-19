
# 🚀 Postgres_Pre_Pro

Este proyecto automatiza el despliegue de scripts SQL a bases de datos PostgreSQL, utilizando GitHub Actions, validación de sintaxis con `sqlfluff` y ejecución controlada por entorno (`DEV` o `PRO`).

---

## 📂 Estructura del repositorio

```
Postgres_Pre_Pro/
├── .github/workflows/
│   └── deploy-sql.yml        # Flujo GitHub Actions que valida y ejecuta
├── src/                      # Carpeta con los scripts .sql
│   ├── crear_tabla_usuarios.sql
│   └── inserta_usuarios.sql
├── scripts_DEV.txt           # Lista de scripts para entorno desarrollo
├── scripts_PRO.txt           # Lista de scripts para entorno producción
├── main.py                   # Lógica de validación y ejecución
├── executor.py               # Ejecuta los scripts en la base de datos
├── sql_validator.py          # Valida sintaxis SQL con sqlfluff
├── requirements.txt          # Dependencias necesarias (sqlfluff, psycopg2, etc.)
└── Dockerfile (opcional)     # Imagen personalizada (no se usa en producción)
```

---

## 🛠️ Requisitos

- Tener configurados los **Secrets** en GitHub:

### 🔐 Desarrollo (`development`)
- `PGDATABASE_DEV`
- `PGUSER_DEV`
- `PGPASSWORD_DEV`
- `PGHOST_DEV`
- `PGPORT_DEV`

### 🔐 Producción (`main`)
- `PGDATABASE_PRO`
- `PGUSER_PRO`
- `PGPASSWORD_PRO`
- `PGHOST_PRO`
- `PGPORT_PRO`

---

## ⚙️ ¿Cómo funciona?

### Al hacer `push` a `main` o `development`:
1. Se activa el flujo `deploy-sql.yml`
2. Se instala `psycopg2`, `sqlfluff` y `postgresql-client`
3. Se carga el archivo de scripts (`scripts_PRO.txt` o `scripts_DEV.txt`)
4. Se valida cada archivo `.sql` con `sqlfluff`
5. Si tiene errores:
   - ❌ Se muestra el mensaje de error con línea y detalle
   - 🚫 No se ejecuta
6. Si todo es válido:
   - ✅ Se ejecuta en la base de datos PostgreSQL usando `psql`

---

## 🧪 Casos controlados

- ❌ `scripts_DEV.txt` vacío → el flujo se detiene con mensaje
- ❌ `scripts_DEV.txt` no existe → el flujo se detiene con mensaje
- ❌ Error de sintaxis en SQL → se muestra línea y detalle
- ✅ Script válido → se ejecuta automáticamente

---

## 💡 Ejemplo de `scripts_DEV.txt`

```
src/crear_tabla_usuarios.sql
src/inserta_usuarios.sql
```

---

## 📦 Instalación local (opcional)

```bash
pip install -r requirements.txt
python main.py
```

---

## 📌 Notas

- La imagen Docker `postgres-ia-runner` fue creada, pero finalmente no se utilizó en GitHub Actions por problemas de estabilidad. Se optó por ejecución directa en `ubuntu-latest`.

---

## 👨‍💻 Autor

Jorge Montalvo – [jmontalvof@outlook.es](mailto:jmontalvof@outlook.es)

---
