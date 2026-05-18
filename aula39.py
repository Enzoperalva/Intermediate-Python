def saudacao():
    return 'Seja bem vindo!'


def medo():
    return 'Você está com medo!'


def ola():
    return 'Olá meu amigo.'


print('1 - Saudacao\n' \
'2 - Medo\n' \
'3 - Ola')

opc = input('Digite sua opção: ')
opcoes = {
    '1': lambda: saudacao(),
    '2': lambda: medo(),
    '3': lambda: ola()
}
try:
    dados = opcoes.get(opc)
    print(dados())
except Exception as e:
    print('Erro inesperado', e)