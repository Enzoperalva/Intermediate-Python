import os, json

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    print(json.dumps(pessoas))

# for pessoa in pessoas:
#     print(pessoa)