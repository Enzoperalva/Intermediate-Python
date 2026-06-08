class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def ligar(self):
        return f"Mensagem genérica"
    
class Carro(Veiculo):
    def ligar(self):
        print("LOG carro:", self.marca)
        return "Vrum Vrum!"

class Moto(Veiculo):
    def ligar(self):
        print("LOG moto:", self.marca)
        return "Ram Ramdam!"


mercedes = Carro("mercedes")
print(mercedes.ligar())

kawasaki = Moto("Kawasaki")
print(kawasaki.ligar())