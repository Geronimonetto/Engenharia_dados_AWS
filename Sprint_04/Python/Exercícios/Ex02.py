def conta_vogais(texto:str) -> int:
    letras = "aeiou"
    letras_encontradas = filter(lambda caracteres: caracteres in letras, texto.lower())
    contagem_letras = len(list(letras_encontradas))
    return contagem_letras

if __name__ == "__main__":
    texto = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit "
             "in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
             "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    contagem = conta_vogais(texto)
    print(contagem)