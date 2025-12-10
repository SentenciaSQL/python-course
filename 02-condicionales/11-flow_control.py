edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa")
elif edad <= 20:
    print("Eres un infante")
elif edad <= 17:
    print("Eres un adolecesnte")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")