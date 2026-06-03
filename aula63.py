class Computador:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.processador = None
        self.memoria_ram = None
        self.armazenamento = None

    def inserir_processador(self, processador, nucleos):
        self.processador = Processador(processador, nucleos)
    
    def inserir_memoria_ram(self, gb):
        self.memoria_ram = MemoriaRAM(gb)

    def inserir_armazenamento(self, modelo, capacidade):
        self.armazenamento = Armazenamento(modelo, capacidade)

    def especificacoes(self):
        if self.processador and self.memoria_ram and self.armazenamento:
            return (f"Marca: {self.marca}\nModelo: {self.modelo}\n\n"
                  f"Processador: {self.processador.processador}\nNúcleos: {self.processador.nucleos}\n\n"
                  f"Memória RAM: {self.memoria_ram.gb} gb\n\n"
                  f"Armazenamento: {self.armazenamento.modelo}\nCapacidade: {self.armazenamento.capacidade} GB")
        
        return "Está faltando peças para a máquina ligar." 
    
    def trocar_ram(self, gb):
        if not self.memoria_ram:
            print("Você ainda não tem memória RAM.")
            return 
        
        print(f"Memória RAM de {self.memoria_ram.gb} GB, trocada para uma de {gb} GB")
        self.memoria_ram = MemoriaRAM(gb)
    
    def trocar_armazenamento(self, modelo, capacidade):
        if not self.armazenamento:
            print("Você ainda não tem armazenamento.")
            return 
        print(f"Armazenamento: {self.armazenamento.modelo} | {self.armazenamento.capacidade} GB, trocada para: {modelo} | {capacidade} GB")
        self.armazenamento = Armazenamento(modelo, capacidade)

    def adequado(self):
        print("Adequado para:")
        if self.armazenamento.capacidade <= 128 and self.processador.nucleos <= 4:
            print("✓ Navegação\n"
                "✗ Programação\n"
                "✗ Jogos")
        if self.armazenamento.capacidade <= 512 and self.processador.nucleos <= 16:
            print("✓ Navegação\n"
                "✓ Programação\n"
                "✗ Jogos")
        else:
            print("✓ Navegação\n"
                "✓ Programação\n"
                "✓ Jogos")
        



class Processador:
    def __init__(self, processador, nucleos):
        self.processador = processador 
        self.nucleos = nucleos

class MemoriaRAM:
    def __init__(self, gb):
        self.gb = gb


class Armazenamento:
    def __init__(self, modelo, capacidade):
        self.modelo = modelo
        self.capacidade = capacidade

pc = Computador("Asus", "Vivobook")
pc.inserir_processador("Ryzen 5", 16)
pc.inserir_memoria_ram(16)
pc.inserir_armazenamento("SSD", 512)
print(pc.especificacoes())
print()
pc.trocar_armazenamento("NvMe", 1024)
pc.trocar_ram(32)
print(pc.especificacoes())
pc.adequado()
