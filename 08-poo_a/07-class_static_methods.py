class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_specie(cls, new_specie):
        cls.species = new_specie

    @staticmethod
    def is_older(age):
        return age >= 18

# person1 = Person("Andres", 37)
# print(person1.species)
# person1.change_specie("Humanoide")
# print(person1.species)
#
#
# person2 = Person("Jose", 20)
# print(person2.species)

print(Person.is_older(19))
person1 = Person("Andres", 37)
print(person1.is_older(person1.age))