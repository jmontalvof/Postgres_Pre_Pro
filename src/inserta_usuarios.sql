CREATE TABLE IF NOT EXISTS :"schema".usuarios_demo (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    email TEXT
);

INSERT INTO :"schema".usuarios_demo (nombre, apellido, email)
VALUES 
    ('Jorge', 'Montalvo', 'jorge@example.com'),
    ('Luis', 'García', 'luis@example.com'),
    ('Ana', 'López', 'ana@example.com');
