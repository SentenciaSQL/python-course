import random
import string


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__password = '1234' # name mangling
        # _Person__password

    def __generate_password(self):
        return  f"$${self.name}{self.age}"
        # return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        # Person__generate_password


person1 = Person("Andres", 37)
print(person1.name)
# print(person1.__password)
# print(person1.__generate_password())
