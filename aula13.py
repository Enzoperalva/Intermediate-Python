som_idade = 0

for c in range(6):
    try:
        idade = int(input(f'Idade [ {c+1} ]: '))
        som_idade += idade
    except ValueError:
        print('Digite uma idade válida!')

print(f'A média de idades é {som_idade / 6:.1f}')
if (som_idade / 6) > 20:
    print('Equipe veterana')
else:
    print('Equipe jovem!')