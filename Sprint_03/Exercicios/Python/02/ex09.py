primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for valor, nome in enumerate(primeirosNomes):
    print(f"{valor} - {nome} {sobreNomes[valor]} está com {idades[valor]} anos")

