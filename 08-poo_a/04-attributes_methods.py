class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name #atributos de instancia
        self.age = age

    def work(self):
        return f"{self.name} esta trabajando muy duro"

    def eat(self, food):
        if food.lower() == "tacos":
            return "SUPERPOWERS"
        else:
            return "+Energia"

person1 = Person("Andres", 37)
print(person1.name)
print(person1.age)
print(person1.species)
print(person1.work())
print(person1.eat("tacos"))