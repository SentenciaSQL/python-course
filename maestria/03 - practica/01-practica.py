number = int(input('Introduzca un numero: '))

def par_number(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(par_number(number))