"""

Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. Como saída, imprima
o ano em que a pessoa completará 100 anos de idade.

"""

from datetime import date


nome = input("Nome: ")
idade = int(input("Idade: "))
ano_atual = date.today().year
ano_total = ano_atual + 100 - idade


print(ano_total)
