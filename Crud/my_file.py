import json
from rich import print
from time import sleep
import core


def ffile_push_json(local_file: str, new_student:dict) -> bool:
    try:
        with open(local_file, 'r', encoding='utf-8') as arq:
            content = arq.read()
            registered_student = []
            if content:
                registered_student = json.loads(content)
    except FileNotFoundError:
        return 
    registered_student.append(new_student)    
    
    with open(local_file, 'w+') as arq:
        json.dump(registered_student, arq, indent=4, ensure_ascii=False)

    return True
    
    
def head_file(local_file):
    try:    
        with open(local_file, 'r', encoding='utf-8') as arq:
            content = arq.read()
            if not content:
                print('[red]ERRO! Você não adicionou nenhum aluno.[/]')
                sleep(1)
                return
            data = json.loads(content)
            cont = 0
            print('ID - NOME - IDADE')
            for item in data:
                print(f'{cont} - {item['name']} - {item['age']}')
                cont +=1
            print()
            sleep(1)
            return 
    except FileNotFoundError:
        return False
    

def att_student(local_archive):
    head_file(local_archive)
    try:
        opc_id = int(input('Qual aluno você quer atualizar? Escolha o id: '))
    except ValueError:
        print('[red]ERRO! Usuário digitou um valor inválido.[/]')
        sleep(1)
        return 
    try:
        with open(local_archive, 'r', encoding='utf-8') as arq:
            data = json.load(arq)
            len_data = len(data) - 1
            if opc_id > len_data:
                print('[red]ERRO! Id não encontrado.[/]')
                return
            name = input('Nome aluno: ').strip().capitalize()
            if len(name) < 2:
                print('[red]ERRO! Usuário digitou um nome inválido.[/]')
                sleep(1) 
            try:
                age = int(input('Idade aluno:'))
            except ValueError:
                print('[red]ERRO! Usuário digitou um valor inválido.[/]')
                sleep(1)
                return
            data[opc_id]['name'] = name
            data[opc_id]['age'] = age
        with open(local_archive, 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)
        print('[green]ALUNO ATUALIZADO![/]')
        return
    except FileNotFoundError:
        print('[red]ERRO! Você não adicionou nenhum aluno.[/]')
        sleep(1)
        return
    

def delete_student(local_archive):
    head_file(local_archive)
    log_data = None
    try:
        opc_id = int(input('Qual aluno você quer deletar? Escolha o id: '))
    except ValueError:
        print('[red]ERRO! Usuário digitou um valor inválido.[/]')
        sleep(1)
        return
    try:
        with open(local_archive, 'r', encoding='utf-8') as arq:
            data = json.load(arq)
            len_data = len(data) - 1
            if opc_id > len_data:
                print('[red]ERRO! Id não encontrado.[/]')
                return
            log_data = data.pop(opc_id)
        with open(local_archive, 'w', encoding='utf-8') as arq:
            json.dump(data, arq, indent=4, ensure_ascii=False)
        print(f'Aluno {log_data} deletado!')
            
            
    except FileNotFoundError:
        print('[red]ERRO! Você não adicionou nenhum aluno.[/]')
        sleep(1)
        return
