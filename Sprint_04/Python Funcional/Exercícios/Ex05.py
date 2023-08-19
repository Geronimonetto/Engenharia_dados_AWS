from statistics import mean

with open('estudantes.csv', 'r', encoding='utf-8') as arquivo:
    mapeando = [x.replace('\n', '').split(',') for x in arquivo]
    for linha in mapeando:
        linha[1:] = [int(nota) for nota in linha[1:]]
        linha[1:] = sorted(linha[1:],reverse=True)  # Ordenando os valores em ordem decrescente
    calculando = map(lambda x: f'Nome: {x[0]} Notas: {x[1:4]} Média: {float(round(mean(x[1:4]), 2))}',
                     mapeando)

    # Ordenar a saída pelo nome do estudante antes de imprimir
    resultado_ordenado = sorted(list(calculando))

    for resultado in resultado_ordenado:
        print(resultado)