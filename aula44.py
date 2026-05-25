class Carro:
    def __init__(self, nome, sobrenome= 'PEralva' ) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def acelerar(self):
        return 'Acelerando', self.nome

fusca = Carro('fusca')
print(fusca.acelerar())