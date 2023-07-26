"""
Escreva um código Python para imprimir todos os números primos entre 1 até 100.
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

Importante: Aplique a função range().
"""


for n in range(2,101):
    if n > 2 and n % 2 ==0 or n > 3 and n % 3 == 0 or n > 5 and n % 5 == 0 or n > 7 and n % 7 ==0:
        pass
    else:
        print(n)