from Func_First_Class import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))  # Recebendo função de outra função

if __name__ =="__main__":
    processar('Dobros de 1 a 10', range(1,11),dobro)
    processar('Quadrados de 1 a 10',range(1,11),quadrado)