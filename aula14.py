from time import sleep
from rich import print
from os import system

lista_compras = []


while True:
   #----------------------------------------------------------------------------------------------
   #TRATANDO ERRO
    try: 
        opc= input('Selecione a opção\n' 
        '[i]nserir ' 
        '[a]pagar ' 
        '[l]istar: ').lower().strip()
        if not opc:
            print('[red]ERRO! Espaço vazio.[/]')
            sleep(1)
            continue
        if len(opc) > 1:
            print('[red]ERRO! Digite apenas 1 caracter.[/]')
            sleep(1)
            continue
    except EOFError:
        print('[red]ERRO! Conexão interrompida![/]')
        sleep(1)
    except KeyboardInterrupt:
        print('[red]ERRO! Usuário interrompeu o programa.[/]')
        sleep(1)
        break
    #----------------------------------------------------------------------------------------------
    if opc == 'i':
      system('clear')
      lista_compras.append(input('Inserir: '))

    elif opc == 'a':
        for c,i in enumerate(lista_compras):
            print(f'[ {c} ] - {i}')
        try:
            lista_compras.pop(int(input('Apagar: ')))
            print(f'[green]Tarefa apagada[/]')
        except ValueError:
            print('[red]ERRO! Digite valor inteiro.[/]')
        except IndexError:
            print('[red]ERRO! Indice não encontrado.[/]')

    elif opc == 'l':
        system('clear')
        if not lista_compras:
            print('[red]ERRO! Lista vazia.[/]')
        else:
            for i in lista_compras:
                print(i)
                sleep(0.5)

    else:
        print('[red]ERRO! Opção inválida.[/]')