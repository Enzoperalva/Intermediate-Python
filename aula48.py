class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return f'Valor depositado: R${valor}'

    def sacar(self, valor):
        if valor > self.saldo:
            return 'Saldo insuficiente.'
        self.saldo -= valor
        return f'Valor sacado: R${valor}'
        
    def mostrar_saldo(self):
        return f'Saldo atual: R${self.saldo}'
    

p1 = ContaBancaria("Enzo")
print(p1.depositar(2000))
print(p1.sacar(500))
print(p1.mostrar_saldo())