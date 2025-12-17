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

class Duck:
    def __init__(self):
        self.flyer = Flyer()
        self.swimmer = Swimmer()

    def quack(self):
        print("Quack")

    def start_fly(self):
        self.flyer.fly()

    def start_swimm(self):
        self.swimmer.swim()

donald = Duck()
donald.start_fly()
donald.start_swimm()
donald.quack()
