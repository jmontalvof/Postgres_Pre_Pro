-- Actualiza el email de un usuario llamado 'Jorge'
UPDATE :"schema".usuarios_demo
SET email = 'jorge_actualizado@example.com'
WHERE nombre = 'Jorge';

-- Confirma la actualización
SELECT * FROM :"schema".usuarios_demo WHERE nombre = 'Jorge';
