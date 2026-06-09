class Animal:
    def identificar(self):
        print("Sou a classe Animal")

class Mamifero(Animal):
    def identificar(self):
        print("Sou a classe Mamifero")

class Aquatico(Animal):
    def identificar(self):
        print("Sou a classe Aquatico")

class Golfinho(Mamifero, Aquatico):
    ...