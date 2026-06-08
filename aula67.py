class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        return f'{self.nome} {self.salario}'

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor 

    def exibir_dados(self):
        return super().exibir_dados() +' '+self.setor
    
enzo = Funcionario("Enzo", 2000)
carlos = Gerente("Carlos", 8000, "TI")
print(carlos.exibir_dados())
