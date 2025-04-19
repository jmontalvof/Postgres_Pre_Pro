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
```

Cada tag representa una versión validada y lista para ser trazada o recuperada si es necesario.

---

## ✅ Ventajas del Modelo

- Separación clara de entornos (pre y producción)
- Revisión manual antes del despliegue en producción
- Histórico claro de versiones desplegadas
- Seguridad y trazabilidad en cada paso del ciclo DevOps

---