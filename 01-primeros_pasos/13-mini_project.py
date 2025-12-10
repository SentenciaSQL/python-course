nombre = input('Introduce tu nombre: ')
ano_nacimiento = input('Introduce tu año de nacimiento: ')
correo = input('Introduce tu correo: ')
contrasena = input('Introduce tu contraseña: ')

edad = 2050 - int(ano_nacimiento)
contrasena_encriptada = len(contrasena)

info = f'''
Nombre: {nombre}
Email: {correo}
Tendras {edad} años en el 2050
Tu contraseña es: {'*' * contrasena_encriptada}
'''

print(info)