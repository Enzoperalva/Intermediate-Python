from rich import print

class Caneta:
    def __init__(self, cor="azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            
            case "verde":
                escolha = "[green]"
            
            case "vermelho" | "vermelha":
                escolha = "[red]"

            case _:
                escolha = "[white]"

        
        self._cor = escolha
        self._caneta_destampada = False

    def destampar(self):
        if self._caneta_destampada:
            print("\n:prohibited: A caneta já está destampada")
            return
        
        self._caneta_destampada = True

    def tampar(self):
        if not self._caneta_destampada:
            print("\n:prohibited: A caneta já está tampada")
            return
        
        self._caneta_destampada = False
        
    def quebrar_linha(self, quant):
        for _ in range(quant):
            print("\n")

    def escrever(self, msg):
        if not self._caneta_destampada:
            print("\n:prohibited: A caneta já está tampada")
            return 
        
        print(f'{self._cor}{msg}[/]', end=' ')

     

c1 = Caneta("verde")
c1.destampar()
c1.escrever("Ola")
c1.quebrar_linha(10)
c1.escrever("Quebra")
c1.escrever("Teste")

c2 = Caneta()
c2.destampar()
c2.quebrar_linha(1)
c2.escrever("Ola")
c2.tampar()
c2.escrever("Ola")