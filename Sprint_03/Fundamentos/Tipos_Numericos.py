from decimal import Decimal, getcontext


a = 2.5
b = 6
c = 10

print(a - b)
print(b - c)

print(type(a))

print(a.is_integer())  # Identifica se o número é inteiro ou seja se o valor após a vírgula é 0
print(5.0.is_integer())

print(int.__add__(2, 5))  # Soma
print((-2).__abs__())  # Mostra o valor absoluto

a = 1.02
b = 2.02

print(a + b)

getcontext().prec = 4  #Aumentando o nível de precisão das casas decimais.
print(Decimal(a) + Decimal(b))
print(Decimal.max(Decimal(a), Decimal(b)))

