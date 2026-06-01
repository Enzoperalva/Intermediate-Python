class Empresa:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._lista_funcionarios = []

    def sum_salarios(self):
        return sum([
            p.salario 
            for p in self._lista_funcionarios
            ])
    
    def contratar_funcionario(self, funcionario):
        if funcionario in self._lista_funcionarios:
            print("Funcionario já foi contratado.")
            return 
        self._lista_funcionarios.append(funcionario)
        print("Funcionario contratado.")

    def listar_funcionarios(self):
        if not self._lista_funcionarios:
            print("Não há funcionarios.")
            return
        for funcionario in self._lista_funcionarios:
            print(funcionario.informacoes_funcionario())
            print("-" * 20)

    def demitir_funcionario(self, indice):
        if not self._lista_funcionarios:
            print("Não tem funcionarios para demitir.")
            return
        try:
            demitido = self._lista_funcionarios.pop(indice)
            print(f'Funcionario {demitido.informacoes_funcionario()} demitido.')
        except IndexError:
            print("Indice inexistente. Tente novamente!")

    def buscar_cargos(self, cargo=None):
        for item in self._lista_funcionarios:
            if cargo == item.cargo:
                print(item.informacoes_funcionario())
            
            

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def informacoes_funcionario(self):
        return f"{self.nome} - {self.cargo} - {self.salario}"

empresa = Empresa("DevBussines")
funcionario1 = Funcionario("Enzo", "Dev", 80000)
funcionario2 = Funcionario("Gabriel", "Dev", 80000)

empresa.contratar_funcionario(funcionario1)
empresa.contratar_funcionario(funcionario2)
empresa.buscar_cargos("Dev")
print(empresa.sum_salarios())

# empresa.listar_funcionarios()
# empresa.demitir_funcionario(0)