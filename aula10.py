evento_aberto = True


while evento_aberto:
    try:
        idade = int(input('Idade: '))
        if idade >= 18:
            print('Bem vindo')

        elif idade == 0:
            evento_aberto = False
        
        else:
            print('Voce não pode entrar!')

    except ValueError:
        print('Digite algo válido!')
    