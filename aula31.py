import itertools as it

compras = [
    'maçã',
    'maçã',
    'banana',
    'banana',
    'banana',
    'leite',
    'leite',
    'pão',
    'maçã',
    'maçã'
]

ordem_compras = it.groupby(compras)
for chave, produtos in ordem_compras:
    cont = 0
    for produto in produtos:
        cont += 1
    print(f'{chave} -> {cont}')