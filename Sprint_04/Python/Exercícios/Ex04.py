def calcular_valor_maximo(operadores,operandos) -> float:
    """
    func: A Função pega os valores que estão em string e transformam em valores eval() serve para essa funcionalidade
    return max(list(mapeando)
    """
    valores = zip(operandos,operadores)
    mapeando = map(lambda x: eval(f'{float(x[0][0])}{x[1]}{float(x[0][1])}'),valores)
    return max(list(mapeando))




if __name__ == "__main__":
    operadores = ['+', '-', '*', '/', '+']
    operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
    print(calcular_valor_maximo(operadores,operandos))
