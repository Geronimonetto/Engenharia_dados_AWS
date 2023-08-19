lista_1 = [1,2,3]
dobro = list(map(lambda x: x * 2,lista_1))

print(dobro)

lista_2 = [
    {'nome':'Geronimo','idade':28},
    {'nome':'Eunice','idade':25},
    {'nome':'Caio','idade':2}
]

so_nome = map(lambda x: x['nome'],lista_2)
print(list(so_nome))

so_idade = map(lambda x:x['idade'], lista_2)
print(sum(so_idade))

#Usando Map retorne frases '<Nome> tem <idade> anos.

nome_idade = map(lambda x : f'{x["nome"]} tem {x["idade"]} anos',lista_2)
for i in nome_idade:
    print(i)
