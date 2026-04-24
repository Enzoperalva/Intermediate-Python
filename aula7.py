while True:
    operador = input('Operador [+-/*]: ')
    numero1 = input('Primeiro número: ')
    numero2 = input('Segundo número: ')
    numeros_validos = None
    operadores_validos = '+-/*'
    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        numeros_validos = True
    except ValueError:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    if operador not in operadores_validos:
        print('Digite um operador válido!')
        continue

    if operador == '+':
        print(f'{numero1} + {numero2} = {numero1 + numero2:.1f}')

    elif operador == '-':
        print(f'{numero1} - {numero2} = {numero1-numero2:.1f}')

    elif operador == '*':
        print(f'{numero1} * {numero2} = {numero1*numero2:.1f}')

    elif operador == '/':
        try:
            print(f'{numero1} / {numero2} = {numero1/numero2:.1f}')
        except ZeroDivisionError:
            print('Não existe divisão por zero, seu burro!')

    continuar = input('Quer sair? [S/N] ').strip().upper()
    if continuar.startswith('S'):
        break