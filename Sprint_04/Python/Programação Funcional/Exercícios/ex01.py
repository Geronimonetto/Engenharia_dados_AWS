def ler_arquivo():
    with open('number.txt', 'r') as arquivo:
        lista = []
        for valor in arquivo:
            valor = int(valor)
            lista.append(valor)
        return lista


def mapear(func):
    valor = sorted(func,reverse=True)
    return valor[:5]

if __name__ == '__main__':
    resultado = mapear(filter(lambda x: x % 2 ==0,map(lambda x: x, ler_arquivo())))
    print(resultado)
    print(sum(resultado))