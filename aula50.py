class Personagem:
    def __init__(self, nome, ataque, vida=100):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo['vida'] - self.ataque



p1 = Personagem('Legolas', 25)
p2 = Personagem('Orc', 15)

print(p1.atacar(p2))