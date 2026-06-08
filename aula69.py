class Pessoa:
    def __init__(self, nome):
        self.nome = nome 

    def apresentar(self):
        return "Mensagem genérica."
    
class Aluno(Pessoa):
    def __init__(self, nome, ano):
        super().__init__(nome)
        self.ano = ano

    def apresentar(self):
        return f"Meu nome é {self.nome} e eu estou no {self.ano} ano"

class Professor(Pessoa):
    def __init__(self, nome, materia):
        super().__init__(nome)
        self.materia = materia

    def apresentar(self):
        return f"Me chamo {self.nome} e sou professor de {self.materia}."
    
enzo = Aluno("Enzo", "Terceiro")
titilo = Professor("Titilo", "Historia")
print(enzo.apresentar())
print(titilo.apresentar())