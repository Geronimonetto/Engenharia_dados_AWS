nome = "Geronimo Morais"
print(nome)
print(nome[0])  # Pegando a primeira letra do nome
# nome[0] = "P"  # não conseguimos mudar, uma string é imutável dessa forma

"Aspas duplas 'precisamos usar aspas simples dentro' para funcionar "  #Para usar aspas diferentes dentro da outra
"Aspas \"nome\""  #usando escape

nome = """Geronimo"""
print(nome)
nome2 = "Estou quebrando \n linha"
nome3 = "Estou usando um tab \t linha"
print(nome2)
print(nome3)

print(nome[4:])  #Iniciando da casa 4 até o final.
# nome[start:end:increment]  #formula

print("Ge" in nome)  #Verificando se tem algo no nome - O python é sensível a letras maiúsculas e minúsculas.

nome = nome.upper()
nome = nome.lower()
nome = nome.capitalize()
# nome = nome.split()  # Também pode ser usado assim nome.split('parametro inicial - vai partir a frase começando nessa letra')
# nome = nome.split('G')
print(nome)
print(nome.__add__(nome2)) # unindo 2 variaveis
print(str.__add__(nome,nome2))  #Igual a união de cima

print(len(nome))  # Função len() Verifica o tamanho de uma string
nome.__len__()  #Função builtins

print("Ge" in nome)  # Isso em builtins fica assim:
"Ge".__contains__(nome)  #Mesmo que o de cima
nome.__contains__("Ge")  #Ou dessa forma

