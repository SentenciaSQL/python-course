import random
import string


def password_generator(longitud):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    chars = letters + numbers + symbols

    # password = "".join(random.choice(chars) for i in range(longitud))

    # return password


    password = []
    for i in range(longitud):
        index = random.choice(chars)
        password.append(index)

    return "".join(password)

length = int(input("Enter the length of the password: "))
print(password_generator(length))