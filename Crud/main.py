from rich import print
from time import sleep
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
    options = {
        1: lambda: core.add_student(ARCHIVE_LOG_STUDENT),
        2: lambda: core.head_archive(ARCHIVE_LOG_STUDENT),
        3: lambda: core.att_student(ARCHIVE_LOG_STUDENT),
        4: lambda: core.delete_student(ARCHIVE_LOG_STUDENT)
    }

    data = options.get(option)
    if data:
        data()
    else:
        print('[cyan]Obrigado por usar nosso pograma<3[/]')
        break