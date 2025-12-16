# default paramenter
def hello(greet="Hola", name="Invitado"):
    """
    Info: Esta es una funcion para devolver un mensaje personzalizado
    :param greet:
    :param name:
    :return:
    """
    print(f"{greet}, {name}")

hello(name="Antonio", greet="Hello")

def multiply(a: float, b: float) -> float:
    """
    Info: multiplica dos numeros y devuelve el resultado
    :param a:
    :param b:
    :return:
    """
    return a * b

print(multiply(2, 3))