"""
Dada a seguinte lista:



a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



Faça um programa que gere uma nova lista contendo apenas números ímpares.

"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_pares = []
for valor in a:
    if valor % 2 != 0:
        lista_pares.append(valor)

print(lista_pares)
