CREATE TABLE IF NOT EXISTS :"schema".usuarios_demo (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    email TEXT
);

UPDATE :"schema".usuarios_demo
SET email = 'jorge@actualizado.com'
WHERE nombre = 'Jorge';

SELECT * FROM :"schema".usuarios_demo
WHERE nombre = 'Jorge';
