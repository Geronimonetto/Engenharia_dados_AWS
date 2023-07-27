def nomes(*args,**kwargs):
    for valor in kwargs.values():
        return *args,valor

valores= nomes(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

for nome in valores:
    print(nome)