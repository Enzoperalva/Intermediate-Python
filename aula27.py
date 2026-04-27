def criar_caixa(taxa_inicial):
    taxa_cashback = 0
    taxa_atual = taxa_inicial
    saldo_cashback = 0

    def processar_compra(valor_compra):
        nonlocal taxa_cashback
        nonlocal taxa_atual
        nonlocal saldo_cashback

        taxa_cashback = valor_compra * taxa_atual
        saldo_cashback += taxa_cashback
        taxa_atual *= 0.9
        return f'Recebeu R${taxa_cashback:.1f}. Saldo total: R${saldo_cashback:.1f}. Próxima taxa: {taxa_atual:.1%}'
    
    return processar_compra


teste = criar_caixa(0.1)
print(teste(100))
print(teste(100))
print(teste(100))
print(teste(100))
print(teste(100))
print(teste(100))