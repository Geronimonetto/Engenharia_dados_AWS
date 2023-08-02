"""

Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a
seguir para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']

"""

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_nova = set()
for valor in lista:
    lista_nova.add(valor)

print(list(lista_nova))
