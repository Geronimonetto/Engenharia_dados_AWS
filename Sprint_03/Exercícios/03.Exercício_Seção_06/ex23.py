"""Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois.
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos
dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:

x = 4
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1

"""


class Calculo:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        return f"Somando {self.x} + {y.x} = {self.x + y.x}"

    def __sub__(self, y):
        return f"Sutraindo {self.x} - {y.x} = {self.x - y.x}"


Numerosx = Calculo(5)
NumerosY = Calculo(6)

print(Numerosx + NumerosY)
print(Numerosx - NumerosY)
