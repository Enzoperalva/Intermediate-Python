from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal=1, volume=1):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_delisga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_max:
                self.volume_atual = ControleRemoto.volume_min
            else:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_min:
                self.volume_atual = ControleRemoto.volume_max
            else:
                self.volume_atual -= 1


    def mostrar_tv(self):
        if not self.ligado:
            conteudo = ":prohibited: [red]A TV está desligada[/]"
        else:
            conteudo = "CANAL  = "
            
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += f"\nVolume = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"

        tv = Panel(conteudo, title="[ TV ]", width=35)
        print(tv)

c = ControleRemoto()

while True:
    c.mostrar_tv()
    comando = input(f"\n< CH >   - VOL + ")
    match comando:
        case '0':
            break
        case '@':
            c.liga_delisga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    
    print("\n" * 10)