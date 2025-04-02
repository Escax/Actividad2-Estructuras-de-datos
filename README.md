# Sistema de Gestión de Biblioteca 📒📚
### Estructura de datos | CORPORACIÓN UNIVERSITARIA IBEROAMERICANA.

## Descripción ✍🏽
Este proyecto es un **Sistema de Gestión de Biblioteca** que utiliza **Estructuras de Datos Lineales** como **listas, pilas, colas y arreglos** para administrar de manera eficiente la información de libros y usuarios. Es una implementación inicial enfocada en la organización y manipulación de datos con estructuras fundamentales en computación.

## Características
- **Registro de libros** con detalles como título, autor, género y disponibilidad.
- **Gestor de usuarios** con información sobre los lectores.
- **Préstamos y devoluciones** mediante una estructura de **cola** (FIFO).
- **Historial de libros leídos** utilizando una **pila** (LIFO).
- **Búsqueda de libros** mediante listas ordenadas y desordenadas.
- **Cálculo del total de préstamos realizados**.
- **Interfaz interactiva de línea de comandos** para la gestión del sistema.

## Tecnologías y Herramientas🧑🏽‍💻
- **Lenguaje:** Python
- **Estructuras de Datos:** Listas, Pilas, Colas, Diccionarios
- **Interacción con el usuario:** Entrada y salida a través de la consola

## Uso
1. Registrar libros y usuarios.
2. Realizar préstamos y devoluciones de libros.
3. Consultar el historial de lectura de los usuarios.
4. Buscar libros disponibles.
5. Ver el total de préstamos realizados.
6. Utilizar el menú interactivo para navegar por las opciones.

## Arquitectura del Código
El sistema está estructurado de la siguiente manera:
- **Estructuras de Datos**: Se utilizan listas para almacenar libros y usuarios, una cola para los préstamos y una pila para el historial de libros leídos.
- **Funciones principales:**
  - `mostrar_libros()`: Muestra la lista de libros disponibles.
  - `registrar_usuario(nombre)`: Agrega un usuario al sistema.
  - `realizar_prestamo(usuario, libro)`: Registra el préstamo de un libro y actualiza el stock.
  - `devolver_libro(usuario, libro)`: Gestiona la devolución de un libro.
  - `ver_historial(usuario)`: Muestra el historial de lectura de un usuario.
  - `total_prestamos()`: Muestra el total de libros prestados en el sistema.
- **Menú interactivo:** Permite al usuario gestionar la biblioteca mediante opciones en consola.



---
**Autores:** Andres Felipe Luenguas | Jhojan Esneider Monroy | Eduardo Romero | Alejandro Rodriguez. 🫱🏽‍🫲🏽

