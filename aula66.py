class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(self.nome+':', 'Som genérico!')

class Cachorro(Animal):
    def fazer_som(self):
        print(self.nome, "Au Au!")

animal1 = Cachorro("Rex")
animal1.fazer_som()