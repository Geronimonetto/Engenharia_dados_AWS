def pares_ate(n: int):
    """
    func: A função verifica os números pares pulando de 2 em 2 sempre somando 
    ao n até o número desejado e roda com o generator
    return: yield num
    """
    for num in range(2, n + 1, 2):
        yield num


n = 14
pares_generator = pares_ate(n)
for pares in pares_generator:
    print(pares)