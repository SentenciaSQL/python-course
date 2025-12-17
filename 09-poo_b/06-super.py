class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print(f'{self.name} hace un sonido')

    def info(self):
        print(f'Soy {self.name} y tengo {self.age} anos')

class Dog(Animal):
    def __init__(self, name, age, bread):
        super().__init__(name, age)
        self.bread = bread

    def sound(self):
        super().sound()
        print(f'{self.name} dice: Guau!')

    def info(self):
        super().info()
        print(f'Soy de raza {self.bread}')

class Cat(Animal):
    def sound(self):
        super().sound()
        print(f'{self.name} dice: Miau!')


fido = Dog('Fido', 3, 'Labrador')
fido.sound()
fido.info()

