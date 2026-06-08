class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.__class__.__name__)
class Cliente(Pessoa):
    ...
        
c1 = Cliente("Enzo", "Peralva")
c1.falar_nome_classe()