def divide_numbers():
    try:
        a = int(input("Ingresa el numerador: "))
        b = int(input("Ingresa el denominador: "))

        result = a / b
        print(result)
        return result
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("Debe introducir un digito")
    except Exception as error:
        print(error)


divide_numbers()