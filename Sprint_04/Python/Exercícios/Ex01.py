def ler_arquivo():
    """
    func: A Função Transforma os dados da forma necessária.
    """
    with open('number.txt', 'r') as arquivo:
        lista = []
        for valor in arquivo:
            valor = int(valor)
            lista.append(valor)
        return lista  


def mapear(func):
    """
    func: A função inverte os valores em ordem decrescente até o 5 parâmetro
    return valor[:5]
    """
    valor = sorted(func,reverse=True)
    return valor[:5]

# if __name__ == '__main__': # Não funciona
resultado = mapear(filter(lambda x: x % 2 ==0,map(lambda x: x, ler_arquivo())))
print(resultado)
print(sum(resultado))