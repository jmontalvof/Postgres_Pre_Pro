CREATE TABLE IF NOT EXISTS usuarios (id SERIAL PRIMARY KEY, nombre TEXT);
CREATE SCHEMA IF NOT EXISTS empleados;

CREATE TABLE IF NOT EXISTS empleados.nueva_tabla (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    cargo TEXT
);
