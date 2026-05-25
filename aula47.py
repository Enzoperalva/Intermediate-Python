class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

p1 = Pessoa('Jojoba', 30)    
p2 = Pessoa.criar_com_50_anos('Enzo')
print(p2.nome, p2.idade)