from rich import print

valor = ''

try:
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        valor = 'PAR'
    else:
        valor = 'ÍMPAR'
    print(f'Seu valor é {valor}!')
except ValueError:
    print(f'[red]ERRO! Digite um número inteiro.[/]')


#EXERCICIO 2
try:
    hora = int(input('Que horas são agora? '))
    if 0 <= hora <= 11:
        print('Bom dia')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif hora > 17:
        print('Boa noite!')
    else:
        print('Não conheco essa hora!')
except ValueError:
    print('Por favor digite apenas números inteiros! ')  

#EXERCICIO 3
first_name = input('Primeiro nome: ')

if first_name:
    count_first_name = len(first_name)
    if count_first_name <= 4:
        print('Seu nome é curto!')
    elif 5 <=count_first_name <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Por favor digite alguma coisa!')