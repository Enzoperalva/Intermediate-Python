from rich import print
from time import sleep
import json
import core



ARCHIVE_LOG_STUDENT = 'alunos.json'
while True:
    print('[blue]1 -[/] [purple]Criar usuário[/] \n'
        '[blue]2 -[/] [purple]Listar usuários[/] \n'
        '[blue]3 -[/] [purple]Atualizar usuários[/]\n'
        '[blue]4 -[/] [purple]Deletar usuário[/] \n'
        '[blue]5 -[/] [purple]Sar[/]'
    )

    try:
        option = int(input('Opção: '))
        print()
    except KeyboardInterrupt:
        print('\n[red]Usuário forçou saida![/]')
    except ValueError:
        print('[red]ERRO! Usuário digitou um valor inválido.[/]')
        sleep(1)
        continue

    if option == 1:
        name = input('Nome aluno: ').strip().capitalize()
        if len(name) < 2:
            print('[red]ERRO! Usuário digitou um nome inválido.[/]')
            sleep(1)
            continue 
        try:
            age = int(input('Idade aluno:'))
        except ValueError:
            print('[red]ERRO! Usuário digitou um valor inválido.[/]')
            sleep(1)
            continue
        core.add_student(name, age, ARCHIVE_LOG_STUDENT)
    
    if option == 2:
        try:    
            with open('alunos.json', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if not conteudo:
                    print('[red]ERRO! Você não adicionou nenhum aluno.[/]')
                    sleep(1)
                    continue
                dados = json.loads(conteudo)
                cont = 0
                print('ID - NOME - IDADE')
                for item in dados:
                    print(f'{cont} - {item['nome']} - {item['idade']}')
                    cont +=1
                print()
                sleep(1)
        except FileNotFoundError:
            print('[red]ERRO! Você não adicionou nenhum aluno.[/]')
            sleep(1)
            continue
    
    if option == 3:
        ...
    if option == 5:
        print('[cyan]Obrigado por usar nosso programa<3[/]')
        break