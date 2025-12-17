class Person:
    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

person1 = Person("Andres", 37)
print(person1.name)
print(person1.age)

person2 = Person("Fidia", 25)
print(person2.name)
print(person2.age)

person3 = Person("Elianny", 9)
print(person3.name)
print(person3.age)