class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):
        return f"Titular: {self.titular}\nSaldo: R$ {self.saldo}"
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        self.rendimento = 0.05

    def exibir_saldo(self):
        return super().exibir_saldo()+ f"\nRendimento mensal: {self.saldo * self.rendimento}"
    
enzo = ContaPoupanca("Enzo", 2000)
print(enzo.exibir_saldo())