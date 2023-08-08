lista = ['Vermelho','laranja','amarelo','verde','azul','índigo','violeta']



def cores_arco_iris(list):
    for v in list:
        yield v  # Armazena na memória de cada vez.

if __name__ == '__main__':
    gerador = cores_arco_iris(lista)
    # while True:
    #     print(next(cores_arco_iris(lista)))

    for v in gerador: 
        print(v)





