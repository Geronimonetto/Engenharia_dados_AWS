lista = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for valor in lista:
    if valor == valor[::-1]:
        print(f"A palavra: {valor} é um palíndrono")
    else:
        print(f"A palavra: {valor} não é um palíndrono")