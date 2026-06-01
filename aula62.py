class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("APAGANDO", self.nome)

class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print("APAGANDO", self.rua, self.numero)

cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Av. Brasil", 54)
cliente1.inserir_endereco("Av. B", 5354)
cliente1.listar_enderecos()

del cliente1

print("###########FIMMM")