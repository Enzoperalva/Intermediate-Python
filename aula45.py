import json

CAMINHO_ARQUIVO = 'pessoas.json'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def saudacao(self):
        return f'Olá {self.nome} {self.sobrenome}! Seja bem vindo.'

p1 =  Pessoa('Enzo', 'Peralva')
p2 =  Pessoa('Marcos', 'Benevoli')
p3 =  Pessoa('Orteu', 'Canadoli')

data = [p1.__dict__, p2.__dict__, p3.__dict__]
with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arq:
    json.dump(data, arq, indent=4, ensure_ascii=False)