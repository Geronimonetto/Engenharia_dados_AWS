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
    func: Organiza os dados para verificação da quantidade de filmes

    :param data_clear:
    :return: organized_list
    """

    organized_list = []
    for valor in data_clear.items():
        organized_list.append(valor[0])
        organized_list.append(valor[1][1])
    return organized_list


def data_verify(organized_list):
    """
    func: Pegandos a quantidade de filmes do ator e o nome para verificar qual a maior quantidade de
    filmes por ator.

    :param organized_list:
    :return: O ator com maior número de filmes
    """

    data_actor = []
    quantity_movie = 0
    nome = ""

    for data_types in organized_list:
        if data_types.isnumeric():
            data_types = int(data_types)
            data_actor.append(data_types)
            if data_types > quantity_movie:
                quantity_movie = data_types
                nome = data_actor[data_actor.index(data_types) - 1]

        else:
            data_actor.append(data_types)

    return f"O Ator com maior número de filmes foi {nome} com {quantity_movie} Filmes"


if __name__ == "__main__":
    print(data_verify(data_organized(data_transform())))
