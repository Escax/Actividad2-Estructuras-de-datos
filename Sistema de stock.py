# Creamos el stock
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1000, "stock": 5},
    {"id": 2, "nombre": "Smartphone", "precio": 600, "stock": 4},
    {"id": 3, "nombre": "Tablet", "precio": 500, "stock": 7},
    {"id": 4, "nombre": "Audífonos", "precio": 300, "stock": 25},
    {"id": 5, "nombre": "Smart Watch", "precio": 350, "stock": 10}
]

clientes = {
    "Juan": {"compras": [], "total_comprado": 0},
    "Maria": {"compras": [], "total_comprado": 0},
    "Carlos": {"compras": [], "total_comprado": 0},
    "Sofia": {"compras": [], "total_comprado": 0},
}

def mostrar_productos():
    print("\nProductos Disponibles")
    for producto in productos:
        print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']} (Stock: {producto['stock']})")
    print()

def realizar_compra(cliente, producto_id, cantidad):
    if cliente not in clientes:
        print("Cliente no encontrado.")
        return

    # Buscar el producto en la lista de productos
    producto = next((prod for prod in productos if prod["id"] == producto_id), None)
    if not producto:
        print("Producto no encontrado.")
        return

    if producto["stock"] >= cantidad:
        total = producto["precio"] * cantidad
        producto["stock"] -= cantidad  # Actualiza el stock
        clientes[cliente]["compras"].append({"producto": producto["nombre"], "cantidad": cantidad, "total": total})
        clientes[cliente]["total_comprado"] += total
        print(f"{cliente} compró {cantidad} {producto['nombre']}(s) por ${total}.")
    else:
        print(f"No hay suficiente stock de {producto['nombre']}. Solo hay {producto['stock']} unidades disponibles.")
    print()

def ver_historial(cliente):
    if cliente not in clientes:
        print(f"Cliente {cliente} no encontrado.")
        return
    
    print(f"\nHistorial de compras de {cliente}:")
    if not clientes[cliente]["compras"]:
        print("No ha realizado compras.")
    else:
        for compra in clientes[cliente]["compras"]:
            print(f"-- {compra['cantidad']} {compra['producto']}(s) - Total: ${compra['total']}")
    
    print(f"Total gastado: ${clientes[cliente]['total_comprado']}")
    print()

def total_ventas():
    ventas_totales = sum(cliente["total_comprado"] for cliente in clientes.values())
    print(f"Total de ventas realizadas: ${ventas_totales}")
    print()

def sistema_tienda():
    while True:
        # Creamos el menú
        print("Opciones:")
        print("1. Ver productos disponibles")
        print("2. Realizar compra")
        print("3. Ver historial de compras de un cliente")
        print("4. Ver total de ventas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            cliente = input("Ingrese el nombre del cliente: ")
            producto_id = int(input("Ingrese ID del producto: "))
            cantidad = int(input("Ingrese cantidad a comprar: "))
            realizar_compra(cliente, producto_id, cantidad)
        elif opcion == "3":
            cliente = input("Ingrese el nombre del cliente: ")
            ver_historial(cliente)
        elif opcion == "4":
            total_ventas()
        elif opcion == "5":
            print("Estamos saliendo del sistema...")
            break
        else:
            print("La opción seleccionada no es válida.")
        print()

# Ejecutar el sistema de tienda
sistema_tienda()
