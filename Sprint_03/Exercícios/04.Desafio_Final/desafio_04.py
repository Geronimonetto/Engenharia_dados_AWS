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
    func: A função fica responsável por calcular a quantidade de vezes que o filme se repete
    :param data_clear:
    :return: organized_dic
    """
    cont = 1
    organized_dic = {}
    for valor in data_clear.values():
        if valor[3] in organized_dic.keys():
            organized_dic[valor[3]] = organized_dic.get(valor[3]) + 1
            continue
        organized_dic[valor[3]] = cont
    return organized_dic


def data_verify(organized_dic):
    """
    A função verifica quais os filmes com maior frequência listados em uma lista filtrada
    com os mais frequentes.

    :param organized_dic:
    :return: Filme e quantidade de frequência do filme
    """

    list_frequency = []
    movie_frequency = 0

    for data_types in organized_dic.items():  # Pegando a maior frequência de filmes e o nome do filme
        if data_types[1] >= movie_frequency:
            movie_frequency = data_types[1]
            movie = data_types[0]
            list_frequency.append(movie)
            list_frequency.append(int(movie_frequency))
    if movie_frequency in list_frequency:  # Verificando se existe mais de 1 filme com frequência maior.
        frequency = list_frequency.index(movie_frequency) - 1
        print(
            f"Filme: {list_frequency[frequency]} - Frequência: {movie_frequency} Vezes")


if __name__ == "__main__":
    data_verify(data_organized(data_transform()))
