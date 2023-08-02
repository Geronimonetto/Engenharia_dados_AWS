def data_transform():
    """
    func: Tratamento dos dados via with para limpar e organizar os dados em um dicionário
    :return: data_clear
    """

    with open('actors.csv', 'r', encoding='utf-8') as arquivo:
        for _ in arquivo:
            list_clear = []
            data_clear = {}
            for index, data in enumerate(arquivo):
                data = data.replace(', ', ' ')
                data = data.replace('"', '')
                data = data.rstrip()
                data = data.replace('\n', '')
                data = data.split(',')
                list_clear.append(data)
                if index + 1 == len(list_clear):
                    index_dic = list_clear[index][0]
                    data_clear[index_dic] = list_clear[index][1:]
                else:
                    break
        return data_clear


def data_organized(data_clear):
    """
    func: Verificando os dados e imprimindo na tela o nome do ator e a média de faturamento
    :param data_clear:
    :return: O ator e o Valor da média de faturamento
    """

    for valor in data_clear.items():
        print(f'Ator: {valor[0]:<25} -  Média de faturamento: $ {valor[1][2]:<20}')


if __name__ == "__main__":
    data_organized(data_transform())
