from string import Template

nome, idade = "Geronimo", 28.4548
print("Nome: %s idade : %d %r" %(nome,idade, True))  #Substituindo nome por Nome e Idade por idade
print("Nome: {0} Idade: {1}".format(nome,idade))
print(f"Nome: {nome} Idade: {idade}")

# %s - Substituindo string
# %d - Sustituindo inteiro
# %f - Float
# %.2f - 2 numeros após a vírgula
# %r - Booleanos

s = Template("Nome: $n Idade: $i")
print(s.substitute(n=nome, i=idade))


