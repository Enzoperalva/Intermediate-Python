import json
import aula45 as al
    
with open(al.CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arq:
    data = json.load(arq)

p1 = al.Pessoa(**data[0])
p2 = al.Pessoa(**data[1])
p3 = al.Pessoa(**data[2])
print(p1.saudacao())
print(p2.saudacao())
print(p3.saudacao())