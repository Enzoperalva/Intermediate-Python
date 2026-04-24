#Desafio 7
def contador_elementos(elemento_procurado, *args):
    cont = 0
    for numeros in args:
        if numeros == elemento_procurado:
            cont += 1

    return f'O elemento procurado {elemento_procurado} apareceu {cont} vezes!'

print(contador_elementos(9, 12, 2, 2, 1, 4, 9, 8, 9, 4, 6))

# OU
def contador_elementos(elemento_procurado, lista):
    cont = 0
    for numeros in lista:
        if numeros == elemento_procurado:
            cont += 1

    return f'O elemento procurado {elemento_procurado} apareceu {cont} vezes!'

print(contador_elementos(9, (12, 2, 2, 1, 4, 9, 8, 9, 4, 6)))
print('-'*40)
print()

#Desafio 8
def achar_item(lista, item):
    posicao = []
    cont = 0
    for num in lista:
        if num == item:
            posicao.append(cont)
        cont+=1
    if len(posicao) == 1:
        return f'O item {item} foi encontrado na posição: {posicao}'
    elif len(posicao) > 1:
        return f'O item {item} apareceu mais de uma vez, nas posições: {posicao}!'
    else:
        return f'O item {item} não está na lista!'

print(achar_item((9, 1, 2, 3, 4, 9), 0))
print()
print('-'*40)

#Desafio 9
def limpar_texto(texto_sujo):
    texto_sujo = texto_sujo.upper()

    caracteres_permitidos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    texto_limpo = []

    for carcter in texto_sujo:
        if carcter in caracteres_permitidos:
            texto_limpo.append(carcter)
    texto_final = ''.join(texto_limpo)

    return f'O texto limpo: {texto_final.capitalize()}' 


print(limpar_texto('Enz0o00! Per333alv000a'))
print()
print('-'*40)