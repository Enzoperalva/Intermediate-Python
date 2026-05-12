import requests
import json
from time import sleep

informacoes = '{"nome": "Ryan"}'

# requisicao = requests.get('https://teste-da7e2-default-rtdb.firebaseio.com/.json')
requisicao2 = requests.delete('https://teste-da7e2-default-rtdb.firebaseio.com/1/nome.json' )
print(requisicao2.json())
