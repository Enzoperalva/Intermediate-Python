def ler_em_blocos(caminho_arquivo, bloco):
    if bloco <= 0:
        raise ValueError('Bloco deve ser maior que zero')
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arq:
            while dados := arq.read(bloco):
                yield dados
                
    except FileNotFoundError as e:
        raise FileNotFoundError('Caminho não existente!') from e


for item in ler_em_blocos('texto.txt', 10): 
    print(item)