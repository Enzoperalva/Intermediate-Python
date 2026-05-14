from itertools import groupby

palavras = [
    'amor',
    'avião',
    'banana',
    'bola',
    'casa',
    'carro',
    'dado',
    'dinheiro',
    'elefante',
]

organization = sorted(palavras, key=lambda p: p[0])
grup = groupby(organization, key= lambda p: p[0])

for chave, valor in grup:
    print(chave + ':')
    for item in valor: 
        print(item)
    print()