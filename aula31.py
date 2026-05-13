import requests
from time import sleep

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
requisicao = requisicao.json()
print(requisicao['USDBRL']['bid'])