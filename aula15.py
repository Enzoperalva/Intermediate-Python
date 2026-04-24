estudantes = [[101, 'Jhonny'], [102, 'Ryan' ], [103, 'Enzo' ], [104, 'Rodrigo']]

add_matricula = int(input('Matricula: '))
add_nome = input('Nome: ')
tudo = [add_matricula, add_nome]
estudantes.append(tudo)

for c, i in enumerate(estudantes):
    print(f'Posição {c+1}: ID {i[0]} - Aluno: {i[1]}')
    print('-'*40)

estudantes[0][1] = 'Jhongavi'
print(estudantes)

estudantes.pop()
print('Estudante removido com sucesso!')
print(estudantes)