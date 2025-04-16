# 🗂️ Postgres_Pre_Pro - Despliegue automatizado de scripts SQL

Este repositorio permite gestionar el despliegue de scripts SQL de forma automática en una base de datos PostgreSQL alojada en Render, utilizando GitHub Actions.

---

## ⚙️ ¿Cómo funciona?

Cada vez que se realiza un `push` a la rama `main` con cambios en:

- `src/instruccionesPRE.txt`
- `src/scripts.txt`
- Archivos `*.sql` en la carpeta `src/`

GitHub Actions ejecuta un flujo que:

1. Lee la base de datos y el esquema definidos en `instruccionesPRE.txt`
2. Lee la lista de scripts a ejecutar desde `scripts.txt`
3. Ejecuta cada script SQL en orden, conectándose a PostgreSQL de forma segura con `secrets`

---

## 🧾 Estructura esperada

```
src/
├── instruccionesPRE.txt
├── scripts.txt
├── inserta_usuarios.sql
├── actualiza_usuarios.sql
├── borra_usuario.sql
```

### instruccionesPRE.txt

```txt
BD=empresa_stlw
CURRENT_SCHEMA=public
SQL=scripts.txt
```

### scripts.txt

```txt
inserta_usuarios.sql
actualiza_usuarios.sql
borra_usuario.sql
```

---

## 🔐 Secrets necesarios en GitHub

Crea estos secrets en la sección **Settings → Secrets → Actions**:

- `PGHOST`: host de la base de datos
- `PGPORT`: puerto (por defecto 5432)
- `PGUSER`: usuario de conexión
- `PGPASSWORD`: contraseña del usuario
- `PGDATABASE`: nombre de la base

---

## 🚀 Despliegue automático

Con cada `push`, el flujo `Postgres_Pre - SQL Deployment` se activa y ejecuta:

```bash
psql -f src/inserta_usuarios.sql
psql -f src/actualiza_usuarios.sql
psql -f src/borra_usuario.sql
```

---

## 🧠 Autor

Creado por Jorge Montalvo para despliegue inteligente de scripts en entornos PostgreSQL vía CI/CD con GitHub Actions.
