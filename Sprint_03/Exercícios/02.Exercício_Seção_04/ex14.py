"""

Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros
nomeados e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

"""


def nomes(*args, **kwargs):
    """
     func: recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados
     e imprime o valor de cada parâmetro recebido.
    :param args:
    :param kwargs:
    :return: args, kwargs
    """
    for dados in args:
        print(dados)
    for dados_2 in kwargs.values():
        print(dados_2)


nomes(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
