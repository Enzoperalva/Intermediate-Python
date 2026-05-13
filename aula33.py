import os, json
pessoas = [
    {
        "nome": "Enzo",
        "idade": 18,
        "altura": 1.80
    },
    {
        "nome": "Enzo",
        "idade": 18,
        "altura": 1.80
    },
    {
        "nome": "Enzo",
        "idade": 18,
        "altura": 1.80
    },
    {
        "nome": "Enzo",
        "idade": 18,
        "altura": 1.80
    }
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)

print(json.dumps(pessoas, indent=2))