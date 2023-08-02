"""
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes
iguais. Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def dividindo_lista(lista_valores, contador):
    quadrante_inicial = 0
    for i in range(contador):
        quadrante_final = quadrante_inicial + len(lista_valores[i::contador])
        yield lista_valores[quadrante_inicial:quadrante_final]
        quadrante_inicial = quadrante_final


dividir = list(dividindo_lista(lista, 3))
print(*dividir)
