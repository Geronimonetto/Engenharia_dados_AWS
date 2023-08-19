lista = [1,3,5,7,9]

def mapear(func,lista):
    for valor in lista:
        yield func(valor)

if __name__ == '__main__':
    print(list(mapear(lambda x : x**2, lista)))  # Passando a função lambda para o mapear para transformar ao quadrado.

"""
Outro Método

def mapear(func,lista):
    return (func(elemento) for elemento in lista)
    
    
if __name__=='__main__':
    print(list(mapear(lambda x: x ** 2, lista))


"""


