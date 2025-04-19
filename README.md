<<<<<<< HEAD
# 🚀 Flujo de Despliegue Controlado con GitHub Actions

Este repositorio implementa un flujo CI/CD completo y profesional para gestionar scripts SQL y despliegues controlados en entornos de preproducción y producción, con uso de versiones por `tags`.

---

## 🧱 Estructura del Flujo

### 1. Despliegue a Preproducción (`deploy-pre.yml`)
- Se lanza manualmente desde la pestaña **Actions**
- Requiere ingresar:
  - Versión (ej: `1.0.0`)
  - Comentario (opcional)
- Valida que `scripts_DEV.txt` exista y tenga contenido
- Ejecuta los scripts en la base de datos de desarrollo/preproducción
- Crea automáticamente el tag con la versión ingresada (`git tag 1.0.0`)

📂 Ubicación: `.github/workflows/deploy-pre.yml`

---

### 2. Validación final (opcional)
- Se puede revisar el resultado de la ejecución en los logs de Actions
- Si todo fue exitoso, se considera el tag como **validado para Producción**

---

### 3. Despliegue a Producción (`deploy-pro.yml`)
- También se lanza manualmente desde **Actions**
- Solicita el nombre del **tag aprobado**
- Clona el repositorio desde ese tag exacto
- Valida `scripts_PRO.txt`
- Requiere aprobación manual mediante el entorno `produccion`
- Ejecuta los scripts en la base de datos de Producción

📂 Ubicación: `.github/workflows/deploy-pro.yml`

---

## 🏷️ Versionado con Tags

Se siguen buenas prácticas de versionado semántico:

```
MAJOR.MINOR.PATCH  →  1.0.0, 1.1.2, 2.0.0
=======

# 📦 Postgres_Pre_Pro – Automatización de despliegue SQL

Este repositorio contiene un flujo de trabajo automatizado para desplegar scripts SQL sobre bases de datos PostgreSQL, diferenciando entornos de desarrollo (`development`) y producción (`main`) mediante GitHub Actions.

---

## 📂 Estructura del repositorio

```bash
Postgres_Pre_Pro/
├── .github/
│   └── workflows/
│       └── deploy-sql.yml       # Workflow principal
├── src/
│   ├── scripts_dev.txt          # Lista de scripts para entorno DEV
│   ├── scripts_pro.txt          # Lista de scripts para entorno PRO
│   ├── *.sql                    # Scripts SQL que se aplicarán en orden
└── README.md
>>>>>>> main
```

Cada tag representa una versión validada y lista para ser trazada o recuperada si es necesario.

---

<<<<<<< HEAD
## ✅ Ventajas del Modelo

- Separación clara de entornos (pre y producción)
- Revisión manual antes del despliegue en producción
- Histórico claro de versiones desplegadas
- Seguridad y trazabilidad en cada paso del ciclo DevOps

---
=======
## 🔁 Funcionamiento del flujo

- Cada vez que se hace `push` sobre las ramas `main` o `development` que afecte archivos `.sql` o listas `.txt`, se activa el workflow.
- El script `deploy-sql.yml` detecta la rama:
  - `main` = entorno **PRO**
  - `development` = entorno **DEV**
- Según la rama, lee los secrets (`PGHOST_DEV`, `PGUSER_DEV`, etc.) y ejecuta los scripts listados en `scripts_dev.txt` o `scripts_pro.txt`.

---

## ⚙️ Variables necesarias en GitHub Secrets

Para que funcione correctamente, debes configurar los siguientes secrets:

| Entorno     | Secrets requeridos                          |
|-------------|----------------------------------------------|
| Desarrollo  | `PGHOST_DEV`, `PGUSER_DEV`, `PGPASSWORD_DEV`, `PGPORT_DEV`, `PGDATABASE_DEV` |
| Producción  | `PGHOST_PRO`, `PGUSER_PRO`, `PGPASSWORD_PRO`, `PGPORT_PRO`, `PGDATABASE_PRO` |

---

## 🚀 ¿Cómo desplegar?

### Despliegue en desarrollo

1. Haz `push` de tus scripts a la rama `development`.
2. Asegúrate de tener `scripts_dev.txt` con el orden correcto de ejecución.
3. El workflow se ejecutará automáticamente.

### Promoción a producción

1. Verifica qué scripts funcionaron en DEV.
2. Copia solo los que necesites a `scripts_pro.txt`.
3. Haz `push` a la rama `main` (con los scripts .sql si son nuevos).
4. El workflow se encargará de desplegarlos en PRO.

---

## ✅ Buenas prácticas

- Versiona tus scripts de forma clara: `update_tabla_3_1.sql`, `update_tabla_3_2.sql`, etc.
- Solo incluye en `scripts_pro.txt` los scripts validados en desarrollo.
- Utiliza `git log`, `git diff` o ramas para identificar versiones anteriores.
- Usa `trigger.txt` si necesitas lanzar un despliegue sin modificar scripts.

---

## 🧠 Autor

- Jorge Montalvo  
- Automatización con ❤️ usando GitHub Actions y PostgreSQL
>>>>>>> main
