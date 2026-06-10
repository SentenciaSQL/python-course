number = int(input('Introduzca un calificacion: '))

def calificacion(number):
    if number >= 70 and number <= 100:
        print('Aprobado')
    elif number < 70:
        print('Reprobado')
    else:
        print('Debe introducir una calificacion validad')
        
calificacion(number)