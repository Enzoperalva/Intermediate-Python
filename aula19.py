def analisar_frequencia(texto):
    texto = texto.upper()

    repetidas = {}

    caracteres_permitidos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto_quase_limpo = []

    for caracter in texto:
        if caracter in caracteres_permitidos:
            texto_quase_limpo.append(caracter)
    texto_limpo = ''.join(texto_quase_limpo)
 

    for lyrics in texto_limpo:
        if lyrics not in repetidas:
            repetidas[lyrics] = 1
        else:
            repetidas[lyrics] += 1

    resultado_final = {}
    for chave, valor in repetidas.items():
        if valor > 1:
            resultado_final[chave] = valor
        
    return resultado_final


print(analisar_frequencia('Enzooo0 Peraaaalvaa334'))