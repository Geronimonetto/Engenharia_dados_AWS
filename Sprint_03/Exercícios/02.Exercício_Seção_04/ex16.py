"""
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"

"""

stg = "1,3,4,6,10,76"


def valida(x):
    acumulador = 0
    for verfify in stg.split(","):
        if verfify.isnumeric():
            verfify = int(verfify)
            acumulador += verfify
        else:
            pass
    return acumulador


print(valida(stg))
