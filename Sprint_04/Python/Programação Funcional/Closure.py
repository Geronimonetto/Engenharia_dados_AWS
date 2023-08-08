def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == "__main__":
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)

    print(f'O Dobro de 7 = {dobro(7)}')
    print(f'O Triplo de 7 = {triplo(7)}')
    