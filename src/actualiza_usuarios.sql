-- Crear tabla si no existe
CREATE TABLE IF NOT EXISTS :"schema".usuarios_demo (
  id SERIAL PRIMARY KEY,
  nombre TEXT,
  email TEXT
);

-- Actualiza si existe el nombre 'Jorge'
UPDATE :"schema".usuarios_demo
SET email = 'jorge_actualizado@example.com'
WHERE nombre = 'Jorge';

-- Mostrar resultados
SELECT * FROM :"schema".usuarios_demo WHERE nombre = 'Jorge';
