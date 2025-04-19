INSERT INTO usuarios (nombre) VALUES ('Luis'), ('Ana'), ('Carlos');
\set schema 'public'

CREATE TABLE IF NOT EXISTS :schema.usuarios_demo (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    email TEXT
);

INSERT INTO :schema.usuarios_demo (nombre, email)
VALUES ('Jorge', 'jorge@inicial.com');
