import re

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class InvalidAgeError(Exception):
    def __init__(self, age, message="La edad debe ser mayor o igual a 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InvalidEmailError(Exception):
    def __init__(self, email, message="El correo electronico no es valido"):
        self.email = email
        self.message = message
        super().__init__(self.message)


def validate_email(email):
    email = email.strip()
    return bool(re.fullmatch(EMAIL_REGEX, email))

def register_user(name, age, email):
    if age < 18:
        raise InvalidAgeError(age)

    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmailError(email, "Correo no valido")

    print(f"{name} ha sido registrado con la edad: {age} y el email: {email}")

    # if validate_email(email):
    #     raise InvalidEmailError(email)
    # print(f"{email} ha sido registrado")

try:
    register_user("Andres", 20, "afrias@gmail.com")
except InvalidAgeError as error:
    print(f"{error}")
except InvalidEmailError as error:
    print(f"{error}")