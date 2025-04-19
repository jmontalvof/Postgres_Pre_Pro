-- Borra usuarios llamados 'Jorge' si existen en la tabla usuarios_demo
DELETE FROM :"schema".usuarios_demo
WHERE nombre = 'Jorge';

-- Muestra la tabla después de eliminar
SELECT * FROM :"schema".usuarios_demo;
