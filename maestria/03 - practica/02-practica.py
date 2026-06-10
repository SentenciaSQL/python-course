numeros = []

for i in range(3):
    numero = float(input(f'Ingrese el  {i + 1}: '))
    numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print('El mayor es:', mayor)