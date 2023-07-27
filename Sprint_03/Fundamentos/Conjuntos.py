# Diferente da Lista
# * Não consegue acessar pelo indice
# * Valores iguais não são aceitos

a = {1, 2, 3}
b = {2, 5, 4}
type(a)
# a[0] - Não aceita indice

c = set("Geronimooooooo")  #mostra apenas o último o
# a = set("a","a")
print(a)
print("G" in a )
print({1,2,3} == {3,2,1,3})  # São iguais no fim
print(a.union(b))  #Une os 2 conjuntos tirando os repetidos
print(a.intersection(b)) #Pega apenas os items comum nos 2 conjuntos
a.update(b)  #Atualizando ("Inserindo valores no sett")
print(a <= b)
print(b >= a)
print({1, 2, 3} - {3})  #diferença do conjunto
print(a - b)  #imprime a diferença entre os 2 sets






