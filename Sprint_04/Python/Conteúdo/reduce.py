from functools import reduce

pessoas = [
    {'nome':'Geronimo','idade':28},
    {'nome':'Eunice','idade':25},
    {'nome':'Monica','idade':50},
    {'nome':'Joaquim','idade':51},
    {'nome':'Stanley','idade':25},
    {'nome':'Caio','idade':2},
    {'nome':'Thomas','idade':1},
    {'nome':'Geane','idade':45},
    {'nome':'Geronimo morais','idade':64},
    {'nome':'Rozimere','idade':60},
    {'nome':'Alexsandro','idade':40},


]
somente_idades = map(lambda x: x['idade'],pessoas)  # Recebendo apenas as idades
filtrando = filter(lambda idade: idade < 18, somente_idades)  # Filtrando as pessoas com idade menor que 18
soma_idades = reduce(lambda idades, idade: idades + idade,filtrando,0)  # Somando as idades, 0 é o valor inicial de idades (Acumulador)
print(soma_idades)
