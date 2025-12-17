class CoffeMaker:
    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        print("Pip Pip")
        print("Tu cafe esta listo")

    def __boil_water(self):
        print("Hirviendo agua")

    def __mix(self):
        print("Conbinando cafe y agua")

coffe_maker = CoffeMaker()
coffe_maker.make_coffe()