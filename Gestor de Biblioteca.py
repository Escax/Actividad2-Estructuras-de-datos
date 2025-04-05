from collections import deque

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"id": 2, "titulo": "Satanás", "autor": "Mario Mendoza", "disponible": True},
    {"id": 3, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "disponible": True}
]

usuarios = {}

devoluciones = []

colas_espera = {}

# Esta función crea los libros
def agregar_libro():
    id_libro = len(libros) + 1
    titulo = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    libros.append({"id": id_libro, "titulo": titulo, "autor": autor, "disponible": True})
    print(f"El Libro '{titulo}' se ha creado correctamente.\n")


# Esta función agrea un usuario
def agregar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario ya existe.\n")
    else:
        usuarios[nombre] = {"prestamos": []}
        print(f" El Usuario '{nombre}' se ha creado correctamente.\n")


# Esta Función muestra los libros disponibles
def mostrar_libros():
    print("\nLibros disponibles:")
    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"{libro['id']}. {libro['titulo']} - {libro['autor']} ({estado})")
    print()


# Esta función es para prestar los libros
def prestar_libro():
    usuario = input("Ingrese el nombre del usuario: ")
    if usuario not in usuarios:
        print("Usuario no encontrado.\n")
        return
    
    mostrar_libros()
    id_libro = int(input("Ingrese el ID del libro que va prestar: "))
    libro = next((l for l in libros if l["id"] == id_libro), None)
    
    if libro and libro["disponible"]:
        libro["disponible"] = False
        usuarios[usuario]["prestamos"].append(libro["titulo"])
        print(f"Libro '{libro['titulo']}' prestado a {usuario}.\n")
    elif libro:
        print(f"El libro '{libro['titulo']}' está prestado en este momento. Se agregará a la lista de espera.\n")
        if id_libro not in colas_espera:
            colas_espera[id_libro] = deque()
        colas_espera[id_libro].append(usuario)
    else:
        print("Libro no encontrado.\n")


# Esta función es para devolver los libros
def devolver_libro():
    usuario = input("Ingrese el nombre del usuario: ")
    if usuario not in usuarios or not usuarios[usuario]["prestamos"]:
        print("El usuario no tiene libros prestados.\n")
        return
    
    print("Libros prestados:")
    for i, titulo in enumerate(usuarios[usuario]["prestamos"], 1):
        print(f"{i}. {titulo}")
    
    seleccion = int(input("Seleccione el ID del libro a devolver: ")) - 1
    if 0 <= seleccion < len(usuarios[usuario]["prestamos"]):
        titulo_devuelto = usuarios[usuario]["prestamos"].pop(seleccion)
        libro = next(l for l in libros if l["titulo"] == titulo_devuelto)
        libro["disponible"] = True
        
        devoluciones.insert(0, titulo_devuelto)
        if len(devoluciones) > 5:
            devoluciones.pop()
        
        print(f"El Libro '{titulo_devuelto}' se ha devuelto.\n")
        
        if libro["id"] in colas_espera and colas_espera[libro["id"]]:
            siguiente_usuario = colas_espera[libro["id"]].popleft()
            print(f"El usuario '{siguiente_usuario}' ahora puede usar el libro '{titulo_devuelto}'.\n")
    else:
        print("Selección inválida.\n")


# Esta función muestra las devoluciones
def mostrar_devoluciones():
    print("\n Los siguientes Libros se devolvieron recientemente:")
    for libro in devoluciones:
        print(f"- {libro}")
    print()


# Esta función muestra la lista de espera de un libro
def mostrar_espera():
    id_libro = int(input("Ingrese el ID del libro: "))
    if id_libro in colas_espera and colas_espera[id_libro]:
        print("Usuarios esperando:")
        for usuario in colas_espera[id_libro]:
            print(f"- {usuario}")
    else:
        print("No hay usuarios esperando el para este libro.\n")


#Esta Función muesta la IU 
def sistema_biblioteca():
    while True:
        print("\nOpciones:")
        print("1. Agregar un Libro")
        print("2. Agregar un Usuari@")
        print("3. Ver Libros disponibles")
        print("4. Prestar Libro")
        print("5. Devolver Libro")
        print("6. Ver Libros devueltos recientemente")
        print("7. Ver lista de espera para un libro")
        print("8. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            agregar_usuario()
        elif opcion == "3":
            mostrar_libros()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            mostrar_devoluciones()
        elif opcion == "7":
            mostrar_espera()
        elif opcion == "8":
            print("Saliendo del sistema...")
            return
        else:
            print("Opción no válida.")
        
        repetir = input("¿Desea realizar otra operación? (S/N): ").strip().lower()
        if repetir != 's':
            print("Saliendo del sistema...")
            return

#Esta Función reinicia el sistema
while True:
    sistema_biblioteca()
    reiniciar = input("¿Desea volver a ingresar al sistema? (S/N): ").strip().lower()
    if reiniciar != 's':
        print("Finalizando el programa...")
        break