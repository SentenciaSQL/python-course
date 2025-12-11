print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]
option = input("Elige una opción (1-6): ")

if option == "1":
    product = input("Ingresa un nombre de producto: ")
    if product not in shopping_cart:
        shopping_cart.append(product)
        print("Producto agregado")
    else:
        print("Producto ya existe")
elif option == "2":
    product = input("Ingresa un nombre de producto: ")
    if product in shopping_cart:
        shopping_cart.remove(product)
        print("Producto eliminado")
    else:
        print("Producto no existe")
elif option == "3":
    if len(shopping_cart) > 0:
        shopping_cart.sort()
        print("Productos ordenadas")
    else:
        print("lista no existe")
elif option == "4":
    product = input("Ingresa un nombre de producto: ")
    if product in shopping_cart:
        print(f"producto {product} encontrado")
    else:
        print("Producto no existe")
elif option == "5":
    print(f"Total de productos: {len(shopping_cart)}")
elif option == "6":
    shopping_cart.clear()
    print("Lista vacia")
else:
    print("Opcion no valida")

print(shopping_cart)