from rich import print
from time import sleep
import json
import my_file 

def inf_student() -> dict:
    name = input('Nome aluno: ').strip().capitalize()
    if len(name) < 2:
        sleep(1)
        return 'ERRO! Usuário digitou um nome inválido.'
    try:
        age = int(input('Idade aluno:'))
        new_student = {
            "name": name,
            "age": age
        }
        return new_student
    except ValueError:
        print('[red]ERRO! Usuário digitou um valor inválido.[/]')
        sleep(1)
        return 


def add_student(local_file:str):
    new_student = inf_student()
    student_json = my_file.ffile_push_json(local_file, new_student)
    if student_json:
        print('[green]ALUNO CADASTRADO![/]')
        print()
        return
    
    print('[red]ERRO! Tente novamente.[/]')
    print()

# def head_student_file(local_file):
# file.head_file('alunos.json')

add_student('alunos.json')