nome = ['Geronimo', 'Eunice', 'Caio']
sobrenome = ['Morais', 'Marinho', 'Lima']
juntos = list(zip(nome, sobrenome))
# juntos = tuple(zip(nome, sobrenome))  # Transformando em tuplas Obtém o resultado parecido com o das listas
# juntos = dict(zip(nome,sobrenome))  #Transformando em dicionário  Resultado - Geronimo: Morais, Eunice: Marinho

print(juntos)  # Juntando primeiros valores de cada lista


def dobro(x):
    return x*2

def quadrado(x):
    return x ** 2

if __name__=="__main__":
    d = dobro  # Podemos armazenar assim
    print(d(5))
    q = quadrado  # Podemos armazenar assim
    print(q(2))

    funcs = [dobro, quadrado]*5
    # Retorna alternadamente o dobro ou quadrado nos números de 1 a 10
    for func, numero in zip(funcs, range(1,11)):
        print(f'O {func.__name__} de {numero} é {func(numero)} ')
