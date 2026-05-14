from functools import reduce

pessoas = [
    {'nome': 'Ana', 'idade': 17},
    {'nome': 'João', 'idade': 22},
    {'nome': 'Maria', 'idade': 15},
    {'nome': 'Pedro', 'idade': 30},
    {'nome': 'Lucas', 'idade': 19},
]

def max_age(pessoa):
    if pessoa['idade'] >= 18:
        return pessoa

def ages(pessoa):
    return pessoa['idade']

def my_sum(acc, value):
    acc += value
    return acc    

filtrando = filter(
    max_age,
    pessoas
)

mapeando = map(
    ages,
    filtrando
)

reduzindo = reduce(
    my_sum,
    mapeando
)

print(reduzindo)