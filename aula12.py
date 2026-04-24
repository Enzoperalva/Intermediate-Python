from os import system

palavra = 'escola'
letras_acertadas = ''
letra_igual = None
forca = len(palavra) * '*'
cont = 0

while True:
    try:
        escolha = input('\nEscolha: ').lower().strip()
        cont+=1
        if len(escolha) > 1:
            print('Escolha só 1 letra!')
            continue
    except ValueError:
        print('Digite só uma letra')
    except KeyboardInterrupt:
        print('Usuario decidiu sair')
    if escolha in palavra:
        letras_acertadas += escolha
    
    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra:
        system('clear')
        print('VOCE GANHOU! PARABÉNS.')
        print(f'Tentativas: {cont}')
        break