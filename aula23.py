import random
import time

def gerador_sensor(num_min=0, num_max=120, tamanho_gerador=12):
    cont = 0
    while cont < tamanho_gerador:
        num_aleatorio = random.randint(num_min, num_max)  
        yield num_aleatorio
        cont += 1


def processador_media(gerador=None):
    try:
        if gerador is None:
            gerador = gerador_sensor()
        cont = acumulador = media = 0
        for item in gerador:
            acumulador += item
            cont += 1

            if cont % 3 == 0:
                media = acumulador / 3
                yield from perigo_media(media=media)
                acumulador = cont = 0

    except Exception as erro:
        yield f'[ERRO]: {erro}'


def perigo_media(media):
    if media < 60:
        yield round(media, 1)
        time.sleep(1)
    
    elif media < 85:
        yield round(media, 1)
        yield '--- PERIGO ---'
        time.sleep(1)

    else:
        yield round(media, 1)
        yield 'TEMPERATURA CRÍTICA'
        yield 'DESLIGANDO SISTEMA (Simulado)'
        time.sleep(1)

gerador = gerador_sensor(tamanho_gerador=100)
teste = processador_media(gerador=gerador)

for item in teste:
    print(item)