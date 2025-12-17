class Flyer:
    def fly(self):
        print("Puedo volar")

    def do_something(self):
        print("Fly Fly")

class Swimmer:
    def swim(self):
        print("Puedo Nadar")

    def do_something(self):
        print("Swim Swimm")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack")

donald = Duck()
donald.fly()
donald.swim()
donald.quack()
donald.do_something()

# MRO: Method Resolution Order
print(Duck.__mro__)