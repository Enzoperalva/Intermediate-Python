from rich import panel, print

class Gamer:
    def __init__(self, nome, nick):
        self._nome = nome
        self._nick = nick
        self._fav_jogos = list()

    def add_favoritos(self, jogo):
        self._fav_jogos.append(jogo)
        self._fav_jogos.sort()

    def ficha(self):
        conteudo = f"Nome real: [black on white] {self._nome} [/]\n"
        conteudo += f"Jogos favoritos:\n"
        
        if self._fav_jogos:
            for item in self._fav_jogos:
                conteudo += f":video_game: {item}\n"
            
        painel = panel.Panel(conteudo, width=40, title=f"Jogador <{self._nick}>")
        print(painel)

j1 = Gamer("Enzo", "Holpex")
j1.add_favoritos("Minecraft")
j1.add_favoritos("Terraria")
j1.add_favoritos("Fortnite")
j1.ficha()