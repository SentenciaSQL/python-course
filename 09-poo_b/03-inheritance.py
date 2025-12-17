class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animal):
    def dog_sound(self):
        print(f'{self.name} dice: Guau!')

class Cat(Animal):
    def cat_sound(self):
        print(f'{self.name} dice: Miau!')

firulays = Dog('firulays')
firulays.sleep()
firulays.dog_sound()

malva = Cat('malva')
malva.sleep()
malva.cat_sound()