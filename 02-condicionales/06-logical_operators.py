# AND
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# OR
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# NOT
# print(not True)
# print(not False)

age = 25
licensed = True

# AND
if age >= 18 and licensed:
    print("puedes conducir")

# OR
is_student = False
membership = True

if is_student or membership:
    print("Obtienes un descuento especial")

# NOT
is_admin = False

if not is_admin:
    print("Acceso denegado")