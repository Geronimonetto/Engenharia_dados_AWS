# operador de membro

Lista = [1, 2, "Geronimo"]

print("Geronimo" not in Lista)  # False por que geronimo está na lista

print(2 in Lista)  #Resultado True

# Operador de Identidade

X = 3
Y = X
Z = 3
print(X is Z)
print(Y is Z)
print(X is not Z)

Lista_a = [1, 2, 3]
Lista_b = Lista_a
Lista_c = [1, 2, 3]

print(Lista_a is Lista_b)
print(Lista_a is Lista_c)  #Mesmo com os mesmos valores não são iguais
print(Lista_c is Lista_b)



