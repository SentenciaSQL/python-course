class Animal:
    def make_sound(self):
        print("Sonido de animal")


class Dog(Animal):
    def make_sound(self):
        print("Woof woof!")

class Cat(Animal):
    def make_sound(self):
        print("Miua Miau!")


def make_noise(animal):
    if isinstance(animal, Animal):
        animal.make_sound()
    else:
        print("No es un animal")

make_noise(Dog())
make_noise(Cat())
make_noise("Hola mundo")