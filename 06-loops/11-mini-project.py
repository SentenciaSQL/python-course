inventory = {
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galleta": 12
}

cart = []

print("Bienvenido a la tienda de dulces, DevCandy!")
print("Inventario: ")

for candy, price in inventory.items():
    print(f"{candy.capitalize()} - ${price}")

while True:
    choice = input("Que dulces deseas comprar? (Escribe salir para terminar) ").lower()

    if choice == "salir":
        break

    if choice in inventory:
        cart.append(choice)
        print(f"Agregaste {choice} a tu carrito")
    else:
        print(f"El dulce de {choice} no existe")

total = 0;
print("Tu carrito")
for candy in cart:
    print(f"{candy.capitalize()} - ${inventory[candy]}")
    total += inventory[candy]

print(f"Total: ${total}")
print("Gacias")