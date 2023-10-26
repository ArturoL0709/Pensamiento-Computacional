# Pensamiento-Computacional
TEC

# README - Sistema de Inventario y Ventas de GamePlanet

Este documento es un **Readme** que proporciona una descripción y una guía de uso para el programa de sistema de inventario y ventas de GamePlanet desarrollado por **Arturo López García** (Número de estudiante: A01276405). El proyecto es parte del "Proyecto Integrador de Pensamiento Computacional para la Ingeniería" y se enfoca en administrar el inventario y las ventas de una tienda de videojuegos llamada GamePlanet, que se especializa en la venta de consolas de diferentes marcas.

## Descripción del Proyecto

El proyecto GamePlanet es una aplicación de consola que permite gestionar el inventario de productos, realizar ventas, registrar llegadas de productos al almacén, consultar datos del inventario y las ventas, y generar reportes de ventas por vendedor y por producto. El programa utiliza listas y diccionarios para mantener un registro de productos en inventario, vendedores y ventas.

## Funciones del Programa

El programa proporciona las siguientes funcionalidades:

1. **Registrar Producto**: Esta función permite al usuario ingresar información sobre un producto, como modelo, nombre y cantidad en existencia, y agrega estos datos al inventario.

2. **Registrar Vendedor**: Permite al usuario registrar un nuevo vendedor proporcionando su nombre. Los vendedores se mantienen en una lista.

3. **Registrar Venta**: Con esta función, el usuario puede registrar una venta, ingresando el modelo del producto, el nombre del vendedor y la cantidad vendida. El programa actualiza automáticamente el inventario y registra la venta.

4. **Registrar Llegada de Productos**: Permite registrar la llegada de productos al almacén al ingresar el modelo del producto y la cantidad llegada. Si el producto ya existe, se actualiza la cantidad; de lo contrario, se solicita el nombre del producto y se crea un nuevo registro.

5. **Consultar Inventario**: Muestra una lista de todos los productos en el inventario, incluyendo su modelo, nombre y cantidad.

6. **Consultar Ventas**: Muestra una lista de todas las ventas registradas, incluyendo el modelo del producto, el nombre del vendedor y la cantidad vendida.

7. **Reporte de Ventas por Vendedor**: Genera un reporte que muestra la cantidad total vendida por cada vendedor.

8. **Reporte de Ventas por Producto**: Crea un reporte que muestra la cantidad total vendida de cada producto.

9. **Guardar Estado**: Guarda el estado actual del inventario y las ventas en un archivo de texto llamado "inventario_ventas.txt". Esto proporciona la capacidad de respaldo y recuperación de datos.

## Cómo Usar el Programa

Para usar el programa, siga estos pasos:

1. Ejecute el programa y aparecerá un menú con varias opciones numeradas.
2. Elija la opción deseada ingresando el número correspondiente y siga las instrucciones proporcionadas por el programa.
3. Puede registrar productos, vendedores, ventas, llegadas de productos, consultar datos, generar reportes y guardar el estado del sistema.
4. Para salir del programa, seleccione la opción "0".

## Notas Adicionales

- Los productos se registran con su modelo y nombre, y se mantiene un registro de la cantidad en existencia.
- Los vendedores se registran por nombre y se mantienen en una lista.
- Cada venta reduce la cantidad de productos vendidos en el inventario.
- Los reportes proporcionan información útil para evaluar el rendimiento de ventas por vendedor y producto.
- El estado actual del sistema puede guardarse en un archivo de texto para respaldo.

Este programa ofrece una solución eficaz para administrar el inventario y las ventas de GamePlanet, lo que facilita un seguimiento efectivo de las operaciones y el rendimiento de ventas.
