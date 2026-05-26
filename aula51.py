class Jogador:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def mostrar_status(self):
        return f'Jogador: {self.nome} | Nível: {self.nivel}'
    
    @classmethod
    def criar_jogador_padrao(cls):
        return cls('Player1', 1)
        
p1 = Jogador('Enzo', 999)
print(p1.mostrar_status())
p2 = Jogador.criar_jogador_padrao()
print(p2.mostrar_status())