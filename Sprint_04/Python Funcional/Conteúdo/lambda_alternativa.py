lista1 = [1,2,3]
lista2 = []

m = list(map(lambda x: x * 2,lista1))  # Retornando uma lista
print(m)

a = list(map(lambda x: x**2,lista1))  # Retornando uma lista
print(a)

b = tuple(map(lambda x:x**2,lista1))  # Retornando uma tupla
print(b)


compras = (
    {'Quantidade':2, 'preco':10},
    {'Quantidade':2, 'preco':10},
    {'Quantidade':2, 'preco':10},

)
def calcular_preco_total(compra):  # Criando uma função para passar no map
    return compra['Quantidade'] * compra['preco']

totais = tuple(map(calcular_preco_total,compras))

print(f'Preços Totais: ',totais)
print(f'Preço Total: ',sum(totais))