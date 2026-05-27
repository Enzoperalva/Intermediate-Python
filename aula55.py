import time

temp_inicial = time.time()
class ContaBancaria:
    def __init__(self, titular_da_conta, saldo, limite_saque_diario):
        self._titular_conta = titular_da_conta
        self._saldo = saldo
        self._limite_saque_diario = limite_saque_diario

    # GETTER AND SETTER NAME
    @property
    def titular_conta(self):
        return self._titular_conta

    @titular_conta.setter
    def titular_conta(self, valor):
        if len(valor) < 3:
            print('Nome inválido')
            return
        
        for item in valor:
            if item in '1234567890':
                print('Nome inválido')
                return

        self._titular_conta = valor
    
    # GETTER AND SETTER SALDO
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Saldo inválido, adicione um valor positivo!')
            return 
        
        self._saldo = valor 
    
    # GETTER AND SETTER SAQUE
    @property
    def limite_saque_diario(self):
        return self._limite_saque_diario

    @limite_saque_diario.setter
    def limite_saque_diario(self, valor):
        if valor < 0 or valor > 5000:
            print('Limite inválido, o valor tem que ser maior que 0 e menor ou igual a 5000.')
            return
        self._limite_saque_diario = valor 
    

p1 = ContaBancaria("Enzo", 100, 500)

temp_final = time.time()
tempo_total = temp_final - temp_inicial
print(round(tempo_total, 6))