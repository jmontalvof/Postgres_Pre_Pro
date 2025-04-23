-- Borra el usuario llamado 'Jorge'
DELETE FROM public.usuarios_demo
WHERE nombre = 'Jorge';

-- Muestra la tabla después de eliminar
SELECT * FROM public.usuarios_demo;
