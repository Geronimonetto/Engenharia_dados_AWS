lista = ["Geronimo", "alow",2,3,4]  #Criando listas
print(type(lista))
lista2 = list() #Outra opção de criar listas

"""
-   As listas são mutáveis e podem ser modificadas, crescendo dinamicamente se preciso
-   Podemos colocar diversos tipos de dados
-   lista.append()  -  adicionar item na lista
-   é ideal que podemos 

"""
# lista.remove("Valor")  - Removendo um valor
# lista.reverse() - inverte a lista
# len(lista) - Mostra o tamanho da lista

# Acessando elementos de uma lista

# lista.index(variavel ou string) - Mostra o indice de onde está o valor.

print(lista.index("alow"))
print(lista[-1])  #mostra o ultimo valor
print(lista[-1:])
del lista[0]  #Excluindo indice 0 da lista
del lista[1]  #Excluindo indice 1 da lista