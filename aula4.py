from rich import print

try: 
    idade = int(input('Idade: '))
    print(f'O dobro de {idade} é {idade * 2}')
except \
    ValueError:
    print('Desculpe, voce não digtou algo válido')