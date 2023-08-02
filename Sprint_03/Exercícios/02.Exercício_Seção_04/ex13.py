"""

Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento.
Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.


Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada
elemento.

"""

lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def exp(lista):
    """
    func: Função para calcular números de uma lista com expoente 2
    :param lista:
    :return:
    """
    return lista ** 2

def my_map(list, f):
    """
    func: Função que recebe uma lista para calcular o expoente 2
    :param list:
    :param f:
    :return: [f(x) for x in list]

    """

    return [f(x) for x in list]


verificador = my_map(lista_teste, exp)
print(verificador)

