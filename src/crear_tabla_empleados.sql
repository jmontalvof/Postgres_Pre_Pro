-- src/crear_tabla_empleados.sql

CREATE TABLE IF NOT EXISTS empleados (
    identificacion VARCHAR(20) PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    jornal NUMERIC(10, 2) NOT NULL
);
