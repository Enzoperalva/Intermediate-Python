class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self, bonus=1.1):
        final_bonus = self.salario * bonus
        return f"Aumento de {(bonus-1)*100:.0f}%: {final_bonus:.1f}"
    
class Gerente(Funcionario):
    def calcular_bonus(self):
        bonus = 1.2
        return super().calcular_bonus(bonus)

class Dev(Funcionario):
    def calcular_bonus(self):
        bonus = 1.15
        return super().calcular_bonus(bonus)
    
gerente = Gerente("Jobs", 9000)
dev = Dev("Enzo", 5000)
print(gerente.calcular_bonus())
print(dev.calcular_bonus())