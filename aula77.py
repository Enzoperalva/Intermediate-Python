import time
from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self._nome = titulo
        self._paginas_total = paginas
        self._pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro[/] '{self._nome}' [blue]que tem[/] {self._paginas_total} [blue]páginas no total. Você agora está na página[/] {self._pagina_atual}\n ")

    def avancar_pagina(self, quant):
        if not type(quant) in (int, float):
            print("Erro! Digite um número.")
            return 
        
        if quant > self._paginas_total or quant <= 0:
            print(f"Erro! Número de páginas para avançar tem que ser > 0 e <= numero de páginas.")    
            return 
        
        for _ in range(quant):
            if not self._paginas_total == self._pagina_atual:
                self._pagina_atual += 1
                print(f"{self._pagina_atual} :arrow_forward: ", end="")
                time.sleep(0.3)

            else:
                print(f"Voce chegou ao final do livro '{self._nome}'.")
                return
            
        
        print(f"Voce avançou {quant} páginas e agora está na página {self._pagina_atual}")


l1 = Livro("A Megera Domada", 20)
l1.avancar_pagina(5)
l1.avancar_pagina(5)
l1.avancar_pagina(5)
l1.avancar_pagina(6)
l1.avancar_pagina(6)