import hashlib

while True:

    recebendo_hash = hashlib.sha256()

    palavra = input("Digite uma palavra e descubra sua hash: ")

    recebendo_hash.update(palavra.encode())
    recebendo_hash.digest()
    
    print(recebendo_hash.hexdigest())

    Saida = input("Deseja sair [S]im ou [Não]: ").upper()
    if Saida =="S":
        break
    else:
        continue