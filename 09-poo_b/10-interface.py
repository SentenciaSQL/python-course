from abc import ABC, abstractmethod

class Animal(ABC):

   @abstractmethod
   def sound(self):
       pass

   @abstractmethod
   def sleep(self):
       pass


class Dog(Animal):
    def sound(self):
        return "Woof woof"

    def sleep(self):
        return 'zzzzz..'


class Cat(Animal):
    def sound(self):
        return "Miau miau"

    def sleep(self):
        return 'zzzzz..'


taco = Dog()
print(taco.sound())
print(taco.sleep())

misuri = Cat()
print(misuri.sound())
print(misuri.sleep())