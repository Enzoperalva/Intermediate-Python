import json
from rich import print

def add_student(name, age, local_archive):
    new_student = {
        "name": name,
        "age": age
    }
    try:
        with open(local_archive, 'r', encoding='utf-8') as arq:
            content = arq.read()
            if not content:
                registered_student = []
            else:
                registered_student = json.loads(content)
    except FileNotFoundError:
        registered_student = []
    registered_student.append(new_student)    
    
    with open(local_archive, 'w+') as arq:
        json.dump(registered_student, arq, indent=4, ensure_ascii=False)

    print('[green]ALUNO CADASTRADO![/]')
    print()