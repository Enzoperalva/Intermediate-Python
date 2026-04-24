from random import randint
from time import sleep

nove_digitos = '' 
for i in range(9):
    nove_digitos += str(randint(0,9))

contador_1 = 10
contador_2 = 11
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
print('GERANDO...')
sleep(1.5)
print(f'CPF GERADO: {cpf_gerado_pelo_calculo}')