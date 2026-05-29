class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self._titular = titular 
        self._saldo = saldo 
        self._limite = limite

    # titular
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor: str) -> None:
        if not type(valor) == str:
            print('Erro! Valor aceitado: str')
            return
        
        valor = valor.strip().capitalize()
            
        if len(valor) < 2:
            print('Erro! Nome inválido')
            return
        
        self._titular = valor

    # saldo
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Erro! Valor negativo.')
            return
        print(self._saldo)
        self._saldo = valor
    
    # limite
    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        if valor <= 0:
            print('Erro! valor negativo ou igual a 0.')
            return
        
        elif valor > 1000:
            print('Erro! Limite passou do valor permitido.')
            return
        
        self._limite = valor
    
    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            return 'Erro! Valor deposito não pode ser negativo.'
            
        self._saldo += valor_deposito
        return f'R${valor_deposito} depositado na conta de {self._titular}.'
    
    def sacar(self, valor_saque):
        if valor_saque > self._saldo or valor_saque < 0:
            print('Erro! Valor de saque inválido.')
            return 
        if valor_saque > self._limite:
            print('Erro! Saque passou do limite.')
            return
        
        self._saldo -= valor_saque
        print(f'R${valor_saque} sacado.')
        return 
    
    def transferir_dinheiro(self, valor_tranferencia, conta_bancaria):
        if valor_tranferencia > self._saldo or valor_tranferencia < 0:
            print('Erro! Valor de saque inválido.')
            return
        if valor_tranferencia < self._limite:
            print('Erro! Saque passou do limite.')
            return
        
        self._saldo -= valor_tranferencia
        conta_bancaria._saldo = valor_tranferencia

        print(f'R${valor_tranferencia} transferido para {conta_bancaria.titular}')
    


p1 = ContaBancaria("Enzo", 100, 50)
p2 = ContaBancaria("Joao", 2000, 500)
print(p1.saldo)
print(p2.saldo)
p2.transferir_dinheiro(1000, p1)
print()
print(p1.saldo)
print(p2.saldo)
p1.transferir_dinheiro(200, p2)
print(p1.saldo)
print(p2.saldo)