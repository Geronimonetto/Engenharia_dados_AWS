#Tudo sobre dicionários
variavel = 30
dicionario = {"Nome":"Professora ana", variavel:38,"Cursos":["Inglês, Português"]}  #Por ventura isso pode acontecer
dicionario2 = {"Nome":"Professora ana", "idade":38,"Cursos":["Inglês, Português"]}  #Geralmente usado assim

print(type(dicionario))
print(len(dicionario))

print(dicionario)
print(dicionario.keys())  #mostra as chaves do dicionario
print(dicionario.values())
print(dicionario.items())

print(dicionario.get("Nome"))  #busca o valor
print(dicionario.get("valorinexistente"))  #Não retorna nada
print(dicionario.get("Valorinexistente", "Valor não existe"))
print(dicionario)

dicionario = {"Nome":"Geronimo", variavel:38,"Cursos":["Inglês, Português"]}  #Modificando tudo do dicionario
dicionario["Cursos"].append("Alemão")  #Adicionando valor ao dicionario e a lista de cursos

dicionario["Nome"] = "Eunice"  #Modificando valor no dicionario
dicionario.pop("Nome")  #Removendo chave e valor dentro do dicionário
print(dicionario)

del dicionario["Nome"]  #Excluindo de outra forma
dicionario.clear()  #Limpando o dicionário


