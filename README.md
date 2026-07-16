# Refactorización del Sistema de Registro de Calificaciones

## Descripción

Este proyecto corresponde a la práctica de la asignatura **Sistemas Ágiles**, cuyo objetivo es aplicar principios de Código Limpio y técnicas de Refactorización sobre un sistema existente, manteniendo exactamente la misma funcionalidad.

El sistema permite:

- Registrar estudiantes y sus calificaciones.
- Calcular el promedio de cada estudiante.
- Determinar si un estudiante está aprobado o reprobado.
- Listar todos los registros almacenados.
- Mostrar un resumen de aprobados y reprobados.

## Tecnologías utilizadas

- Python 3
- Git
- GitHub

## Mejoras realizadas

Durante el proceso de refactorización se aplicaron las siguientes mejoras:

- Extracción de la función `calcular_promedio()`.
- Renombrado de variables para mejorar la legibilidad.
- Renombrado de funciones con nombres descriptivos.
- Uso de `with open()` para el manejo seguro de archivos.
- Organización del flujo principal mediante la función `main()`.
- Reemplazo del número mágico por la constante `NOTA_APROBACION`.

## Integrantes

- Stiven Vallejo
- Guillermo Vallejo