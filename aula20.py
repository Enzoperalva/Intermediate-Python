from random import shuffle,choice, randint
from rich import print

numeros1 = randint(0, 9)
numeros2 = randint(0, 9)
numeros3 = randint(0, 9)
operacao = choice(['+', '-', '/', '*'])
pergunta_final = numeros1, operacao, numeros2

    
if operacao == '/':
    resposta = numeros1 / numeros2
    resposta = f'{resposta:.1f}'
    resposta = float(resposta)
elif operacao == '*':
    resposta = numeros1 * numeros2
elif operacao == '+':
    resposta = numeros1 + numeros2
elif operacao == '-':
    resposta = numeros1 - numeros2

opcoes = [float(numeros1), float(numeros2), float(numeros3), float(resposta)]
shuffle(opcoes)

perguntas = [ 
    {
        'Pergunta': '',
        'Resposta': ''
    },
    {
        'A': '',
        'B': '',
        'C': '',
        'D': '',
    }
]
perguntas[0]['Pergunta'] = pergunta_final
perguntas[1]['A'] = opcoes[0]
perguntas[1]['B'] = opcoes[1]
perguntas[1]['C'] = opcoes[2]
perguntas[1]['D'] = opcoes[3]
perguntas[0]['Resposta'] = resposta

print('Pergunta: ', end='')
for c in pergunta_final:
    print(c, end=' ')
print('= x')
print()

for chave, item in perguntas[1].items():
    print(f'{chave}) {item}')

resposta_usuario = input('Resposta: ').upper().strip()
if resposta_usuario not in 'ABCD':
    print('[red]ERRO! Opção inválida.[/]')
elif perguntas[1][resposta_usuario] == perguntas[0]['Resposta']:
    print('[green]Parabéns! Você acertou.')
else:
    print(f'[red]RESPOSTA ERRADA! A opção correta é {perguntas[0]['Resposta']}.')
