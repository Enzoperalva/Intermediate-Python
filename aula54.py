class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    # NOME
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if len(valor) < 3:
            print('Nome inválido!')
            return 
        self._nome = valor
    
    # PRECO
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor < 0:
            print('Preço inválido!')
            return 
    
        self._preco = valor
    
    # QUANTIDAE
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, valor):
        if valor < 0:
            print('Quantidade inválido!')
            return 
        
        self._quantidade = valor

    # VALOR TOTAL
    def valor_total(self):
        tot = self.preco * self.quantidade
        return f'Produto: {self.nome} | Valor total: {tot}'
        
    
p1 = Produto("Teclado", 150, 20)
p1.nome = 'A1'
p1.preco = 200


print(p1.valor_total())