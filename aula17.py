#Desafio 1
def somar_apenas_numeros(*args):
    lista_numeros = []
    for numeros in args:
        if type(numeros) == int or type(numeros) == float:
            lista_numeros.append(numeros)

    soma = sum(lista_numeros)
    resultado = f'A soma de todos os NÚMEROS é: {soma}!'
    
    return resultado
    

print(somar_apenas_numeros(1, 2, 'a', 200, 'Python', 'Oi gemini', 211212142))
print('-'*40)
#-------------------------------------------------------------------------------------------

#Desafio 2
def multiplicar_todos(multiplicador, *args):
    lista_resultados = []
    for numeros in args:
        lista_resultados.append(numeros * multiplicador)

    lista_resultados = tuple(lista_resultados)
    return lista_resultados   

print(multiplicar_todos(3, 10, 20, 30))
print('-'*40)
#-------------------------------------------------------------------------------------------------

#Desafio 3
def encontrar_extremos(*args):
    if not args:
        return 'Nenhum argumento foi passado!'
    
    else:
        primeiro_numero = args[0]
        maior = primeiro_numero
        menor = primeiro_numero

        for numero in args:
            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero
        return f'O maior número é {maior}\nE o menor número é {menor}'

print(encontrar_extremos(2, 90, 2, 102, -1))