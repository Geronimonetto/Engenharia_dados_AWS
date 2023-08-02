"""
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json,

"""

import json

with open("person.json", "r") as arquivo:
    arquivo_json = arquivo.read()
    arquivo_json = json.loads(arquivo_json)
    print(arquivo_json)
