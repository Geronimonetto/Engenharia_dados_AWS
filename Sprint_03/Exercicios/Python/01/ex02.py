"""
Escreva um código Python para verificar se três números digitados na entrada padrão são
pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).


Importante: Aplique a função range() em seu código.


Exemplos de saída:

Par: 2
Ímpar: 3
"""


first_number = int(input("Primeiro Número: "))
second_number = int(input("Segundo Número: "))
third_number = int(input("Terceiro Número: "))

for i in range(1):
    if first_number %2 ==0:
        print(f"Par: {first_number}")
    else:
        print(f"Ímpar: {first_number}")
    if second_number % 2 == 0:
        print(f"Par: {second_number}")
    else:
        print(f"Ímpar: {second_number}")
    if third_number %2 ==0:
        print(f"Par: {third_number}")
    else:
        print(f"Ímpar: {third_number}")
