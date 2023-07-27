def faixa_idade(idade):
    if 0 < idade <18:
        print("Menor de idade")
    elif idade in range(18,64):
        print("Adulto")
    elif idade in range(65,100):
        print("Melhor idade")
    elif idade >= 100:
        print("Centenário!!")
    else:
        print("Idade Inválida")

if __name__ =="__main__":
    idade = int(input("Idade: "))
    faixa_idade(idade)
