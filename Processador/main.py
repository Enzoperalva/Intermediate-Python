import back as b

def processador_financeiro(gerador, validar):
    for item in gerador:
        print(item)

teste = processador_financeiro(
    b.gerador_transacoes(), b.validar_transacao(chave='valor')
    )