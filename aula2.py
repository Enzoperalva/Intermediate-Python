from time import sleep

notas = list()
x = media = 0
situacao = ''

name = input('Nome do aluno: ')
while True:
    notas.append(int(input(f'Nota {x+1}: ')))

    x += 1
    opc = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if opc == 'N':
        break

media = sum(notas) / len(notas)

if media < 5:
    situacao = '\033[31mREPROVADO\033[m'
elif 5 <= media < 6.9:
    situacao = '\033[33mRECUPERAÇÃO\033[m'
else:
    situacao = '\033[32mAPROVADO\033[m'

print(f'Aluno: {name}')
sleep(0.5)
print(f'Média: {media}')
sleep(0.5)
print(f'Situação: {situacao}')