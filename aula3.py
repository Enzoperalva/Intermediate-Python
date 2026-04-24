name = input('Seu nome: ')
idade = input('Idade: ')
sp = 0

if ' ' in name:
    esp = 'contém'
else:
    esp = 'não contém'

if name and idade:
    print(f'Seu nome é: {name} \n' 
    f'Seu nome invertido é: {name[::-1]} \n' 
    f'Seu nome {esp} espaços!\n' 
    f'Seu nome tem {len(name)} letras!\n' 
    f'A primeira letra do seu nome é: {name[0]} \n' 
    f'A última letra do seu nome é {name[-1]} ')
else:
    print('Desculpe, voce deixou campos vazios')