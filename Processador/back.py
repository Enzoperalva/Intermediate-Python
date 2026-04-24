import random


def gerador_transacoes(quant_transacoes=10):
    cont = 0
    while cont < quant_transacoes:
        num_aleatorio = random.randint(-1000, 15000)
        id_aleatorio = random.randint(0, 1000)
        tipo = random.sample(('pix', 'dinheiro', 'cartão'), 1)
        yield {
            'id': id_aleatorio,
            'valor': num_aleatorio,
            'tipo': tipo[0]
        }
        cont += 1


def validar_transacao(chave, item):
    if item[chave] < 0:
        item['status'] = 'inválido'
        yield item

    elif item[chave] > 10000:
        item['status'] = 'suspeita de fraude'
        yield item
    
    else:
        item['status'] = 'valido'
        yield item


teste = validar_transacao(chave='valor')

for item in teste:
    print(item)