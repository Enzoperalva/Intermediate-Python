from rich import print
from re import sub
from sys import exit

contador_1 = 10
contador_2 = 11
entrada = input(
    'CPF [xxx.xxx.xxx-XX]: '
)
cpf_enviado_usuario = sub(
    r'[^0-9]',
    '',
    entrada
)
entrada_e_sequencia = entrada == entrada[0] * len(entrada)
if entrada_e_sequencia:
    print('[red]ERRO! Você enviou dados sequênciais.[/]')
    exit()

nove_digitos = cpf_enviado_usuario[:9]
resultado_1 = resultado_2 = 0


#--------------CALCULO PRIMEIRO DIGITO-----------------

for digito in nove_digitos:
    resultado_1 += int(digito) * contador_1
    contador_1 -= 1

digito_1 = (resultado_1 * 10) % 11

if digito_1 > 9:
    digito_1 = 0
else:
    digito_1 = digito_1
#-----------------------------------------------------

#----------------CALCULO SEGUNDO DIGITO------------------------   

dez_digitos = nove_digitos + str(digito_1)
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_2
    contador_2 -= 1

digito_2 = (resultado_2 * 10) % 11
if digito_2 > 9:
    digito_2 = 0
else:
    digito_2 = digito_2

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
#--------------------------------------------------------------

#-------------------Analisando se o cpf é válido--------------------
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(
        f'{cpf_enviado_usuario}[green] é válido![/]'
    )
else:
    print(
        '[red]CPF inválido[/]'
    )
 