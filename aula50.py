class Personagem:
    def __init__(self, nome, ataque, vida=100):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        if inimigo.vida <= 0:
            inimigo.vida = 0
            return 'Inimigo derrotado! Você não pode mais atacar'
        return f'{inimigo.nome} atacado! Vida atual: {inimigo.vida}'

    def mostrar_status(self):
        return f'\nNome: {self.nome}\nVida: {self.vida}\nAtaque: {self.ataque}'



p1 = Personagem('Legolas', 30)
print(p1.mostrar_status())
p2 = Personagem('Orc', 20)

print(p1.atacar(p2))
print(p1.atacar(p2))
print(p1.atacar(p2))
print(p1.atacar(p2))
print(p2.mostrar_status())
