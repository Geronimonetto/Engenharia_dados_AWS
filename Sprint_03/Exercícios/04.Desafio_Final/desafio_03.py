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
    func: Organizando os dados para verificação a média de faturamento por ator/atriz

    :param data_clear:
    :return: O ator com a maior média de faturamento por filme
    """
    organized_list = []
    for valor in data_clear.items():
        organized_list.append(valor[0])
        organized_list.append(valor[1][2].strip())
    return organized_list




def data_verify(organized_list):
    """
    func: Buscando nome e faturamento médio para verificar qual o ator/atriz com maior faturamento
    médio por filme.

    :param organized_list:
    :return: O ator com a maior média de faturamento por filme
    """
    data_actor = []
    max_gross = 0
    nome = ""
    accumulator = 0

    for data_types in organized_list:

        data_types = data_types
        if accumulator % 2 != 0:
            data_types = float(data_types)
            data_actor.append(data_types)
            if data_types > max_gross:
                max_gross = data_types
                nome = data_actor[data_actor.index(data_types) - 1]
        else:
            data_actor.append(data_types)
        accumulator += 1
    print(f"O Ator/Atriz com a maior média de faturamento por filme foi {nome} com $ {max_gross}")



if __name__ == "__main__":
    data_verify(data_organized(data_transform()))
