from rich.traceback import install
install(show_locals=True)

class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Professor():
    def __init__(self, idade):
        self.idade = idade

class Diretor(Aluno, Professor):
    def __init__(self, nome, idade):
        Aluno.__init__(self, nome)
        Professor.__init__(self, idade)

    def apresentar(self):    
        print(f"Sou {self.nome} e tenho {self.idade} anos")

enzo = Diretor("Enzo", 19)
enzo.apresentar()