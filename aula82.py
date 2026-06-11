from rich import inspect, print, print_json
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, curso, turma,  nome, idade):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        ...


class Professor(Pessoa):
    def __init__(self, nivel, especialidade, nome, idade):
        super().__init__(nome, idade)
        self.nivel = nivel
        self.especialidade = especialidade


    def dar_aula(self):
        ...


class Funcionario(Pessoa):
    def __init__(self, cargo, setor, nome, idade):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_pont(self):
        ...


a1 = Aluno("Eng. software", "T01", "Enzo", 18 )
a1.fazer_aniversario()
inspect(a1)

p1 = Professor("Mestre", "TI", "Titilo", 60)
p1.fazer_aniversario()
