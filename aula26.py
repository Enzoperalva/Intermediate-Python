def configurar_elevador(andar_inicial):
    total_de_viagens = 0

    def mover(novo_andar):
        nonlocal total_de_viagens
        nonlocal andar_inicial

        if novo_andar == andar_inicial:
            return f'O elevador já está no andar {novo_andar}'
        else:
            total_de_viagens += 1
            diferenca = andar_inicial - novo_andar 
            andar_inicial = novo_andar
            return f'Movendo para o andar {novo_andar}... Viagens totais: {abs(total_de_viagens)}'
    
    return mover


meu_elevador = configurar_elevador(andar_inicial=0)
print(meu_elevador(novo_andar=12))
print(meu_elevador(novo_andar=12))
print(meu_elevador(novo_andar=2))
print(meu_elevador(novo_andar=6))
print(meu_elevador(novo_andar=1))