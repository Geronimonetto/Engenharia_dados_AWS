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

totais = tuple(
    map( lambda compras: compras['Quantidade'] * compras['preco'],
    compras


))

print(f'Preços Totais: ',totais)
print(f'Preço Total: ',sum(totais))