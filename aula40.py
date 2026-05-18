import random

caracteres_senha = '!@#$%&abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def senhas(tam_senha=8):
    log_senha = set()
    while True:
        lista_senha = random.choices(caracteres_senha, k=tam_senha)
        senha = "".join(lista_senha)
        
        while senha in log_senha:
            lista_senha = random.choices(caracteres_senha, k=tam_senha)
            senha = "".join(lista_senha)
            
        log_senha.add(senha)
        yield senha
        


try:
    tam = int(input('Tamanho da senha: '))
    while tam < 8:
        print('Senha mínima: 8')
        tam = int(input('Tamanho da senha: '))

    for item in senhas(tam):
        print(item)
        opc = input('Deseja continuar? [S/N]').strip().upper()[0]
        while opc not in 'SN':
            print('ERRO! Resposta inválida.')
            opc = input('Deseja continuar? [S/N]').strip().upper()[0]
        
        if opc == 'N':
            break

except ValueError:
    print('ERRO! Digite um valor válido.')
except IndexError:
    print('ERRO! Digite um valor válido.')
