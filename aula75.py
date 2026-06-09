class Pai:
    def apresentar(self):
        print("Sou a classe PAI")

class Mae:
    def apresentar(self):
        print("Sou a classe MAE")

class Filho(Pai, Mae):
    ...

filho = Filho()
filho.apresentar()