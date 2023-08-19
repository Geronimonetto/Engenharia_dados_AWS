from functools import reduce

def calcula_saldo(lancamentos) -> float:
    """
    func: A Função pega os valores de crédito e débito e soma quando o valor for crédito e subtrai quando o valor for débito
    return saldo
    """
    mapeando = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)  # Transformando os dados de Debito em negativo
    saldo = reduce(lambda soma, x: soma + x, mapeando, 0)
    return saldo
    
if __name__ == "__main__":
    lancamentos = [
        (200, 'D'),
        (300, 'C'),
        (100, 'C')
    ]
    saldo_final = calcula_saldo(lancamentos)
    print(saldo_final)
