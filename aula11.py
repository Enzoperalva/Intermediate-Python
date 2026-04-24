salva = ''
i = repetiu = apareceu_mais_vezes = 0
letra_que_apareceu = ''

frase = input('Frase: ')

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    repetiu = frase.count(letra_atual)

    if apareceu_mais_vezes < repetiu:
        apareceu_mais_vezes = repetiu
        letra_que_apareceu = letra_atual

    i += 1
print(letra_que_apareceu)