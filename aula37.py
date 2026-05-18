import time, os
from rich import print
import json

tasks = []
log = []

while True:
    try:
        print('1 - Listar \n' \
        '2 - Desfazer\n' \
        '3 - Refazer\n' \
        '4 - Limpar terminal\n' \
        '5 - Sair')
        opc = input('Digite uma tarefa ou comando: ')
        print()
    
    except ValueError:
        print('[red]ERRO! Escolha um valor válido.[/]')
        time.sleep(1)
        print()
        continue
    
    if not opc in '12345':
        tasks.append(opc)
        print(f'Task adicionada: {opc}')
        time.sleep(1)
        print()
        continue

    if opc == '1':
        if not tasks:
            print('Não há nada para listar!')
            time.sleep(1)
            print()
            continue
        for item in tasks:
            print(item)
        time.sleep(1)
        print()
    
    if opc == '2':
        if not tasks:
            print('Não há nada para desfazer.')
            time.sleep(1)
            print()
            continue
        item_apagado = tasks.pop()
        print(f'Item apagado: {item_apagado}')
        log.append(item_apagado)
        for item in tasks:
            print(item)
        time.sleep(1)
        print()
    
    if opc == '3':
        if not log:
            print('Não há nada para refazer!')
            print()
            time.sleep(1)
            continue

        print(f'Refazendo tarefa: {log[-1]}')
        tasks.append(log[-1])
        log.pop()
        print()
        time.sleep(1)

    if opc == '4':
        os.system('clear')
        time.sleep(1)

    if opc == '5':
        print('Obrigado por usar nosso software!')
        time.sleep(1)
        break
    