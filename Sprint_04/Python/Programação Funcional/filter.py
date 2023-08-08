# Função filter serve para filtrar valores em subconjuntos

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

menores = filter(lambda p: p['idade'] < 20, pessoas)  #Pegando apenas os menores de 20 anos
nomes_maiores = filter(lambda p: len(p['nome']) > 6,pessoas)
print(list(nomes_maiores))
print(list(menores))