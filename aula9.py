from rich import print
num = '0123456789'
caracter_salvo = ''
erros = 0

while True:
    x = 0
    tem_num = None
    tem_oito = None
    senha = input('Senha: ')
    while x < len(senha):
        caracter_salvo = senha[x]
        if caracter_salvo in num:
            tem_num = True
        x += 1
    if tem_num is None:
        print('[red]Senha deve conter pelo menos 1 número![/]')
        erros += 1
    if len(senha) < 8:
        print('[red]Senha deve conter pelo menos 8 caracteres![/]')
        erros += 1
    elif len(senha) >= 8:
        tem_oito = True

    if tem_oito is True and tem_num is True:
        print('[green]Senha válida![/]')
        if erros > 0:
            print(f'Voce errou a senha {erros} vezes')
        break