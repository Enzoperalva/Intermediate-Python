class Aluno:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    def inf_aluno(self):
        return f"{self._nome} - {self._idade}"


class Escola:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._alunos = []

    def matricular_aluno(self, aluno):
        self._alunos.append(aluno)

    def listar_alunos(self):
        if not self._alunos:
            print("Não tem alunos matriculados.")
            return
        for aluno in self._alunos:
            print(aluno.inf_aluno())
            print("-" * 30)

    def quant_alunos(self):
        print(f"{len(self._alunos)} alunos matriculados.")

escola = Escola("Polivalente")
aluno1 = Aluno("Enzo", 19)
aluno2 = Aluno("JP", 20)

escola.matricular_aluno(aluno1)
escola.matricular_aluno(aluno2)
escola.listar_alunos()
escola.quant_alunos()