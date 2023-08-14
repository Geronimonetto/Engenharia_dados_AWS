def conta_vogais(texto:str) -> int:
    vogais = "aeiouAEIOU"
    vogais_presentes = filter(lambda char: char in vogais, texto)
    numero_vogais = len(list(vogais_presentes))

    return numero_vogais

texto = "Olá, esta é uma string de exemplo com algumas vogais."
resultado = conta_vogais(texto)
print(resultado)