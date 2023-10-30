import json
import pandas as pd
import boto3
import requests

def pages_gener():
    dados = []
    url = f'https://api.themoviedb.org/3/discover/movie?api_key=ea33ae145ce37250f8ab09b9583b7a7f&with_genres=27,9648'
    response = requests.get(url)
    data = response.json()
    total_pages = data['total_pages']
    for valor in range(1, total_pages + 1):
        url = f"https://api.themoviedb.org/3/discover/movie?page={valor}&api_key=ea33ae145ce37250f8ab09b9583b7a7f&with_genres=27,9648"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            resultados = data["results"]
            ids = [filme["id"] for filme in resultados]
            dados.extend(ids)
        else:
            continue
    return dados

def process_data(list_id):
    """
    func: A função recebe um objeto do S3 da AWS e filtra os dados de acordo com os generos solicitados
    Parameters
    ----------
    event
    context

    Returns
    -------

    """
    s3 = boto3.client('s3',
        aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
        aws_secret_access_key='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'
    )

    bucket_name = 'data-lake-desafio-final'
    s3_file_name = 'Raw/Local/CSV/Movies/2023/09/26/movies.csv'

    try:
        # Gêneros desejados
        generos = ['Horror', 'Mystery']

        # Obter objeto do bucket S3
        objeto = s3.get_object(Bucket=bucket_name, Key=s3_file_name)

        # Ler arquivo CSV diretamente do objeto do S3 e criar DataFrame
        df = pd.read_csv(objeto['Body'], sep='|', na_values=[r'\N'], dtype={'NomeDaColuna': str})

        # Filtrar filmes por gênero
        all_movies = df[df['genero'].isin(generos)].drop_duplicates()

        # Obter IDs únicos dos filmes
        lista_ids_unicos = all_movies['id'].unique().tolist()
        list_id.extend(lista_ids_unicos)
        api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
        dados = []  # Lista para adicionar os dados que vão para o JSON
        n_file = 1  # Número para ordenar o nome dos arquivos

        for id_movie in list_id:
            url = f'https://api.themoviedb.org/3/movie/{id_movie}?api_key={api_key}&language=en-US&append_to_response=credits'  # API
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                dados.append(data)

                if len(dados) == 100:

                    # Transformando a lista 'dados' em um objeto JSON

                    json_file = json.dumps(dados, indent=4)
                    json_clear = json_file[1:-1].replace("\n", "")
                    # Fazendo upload dos dados diretamente para o S3
                    s3_key = f'Raw/TMDB/JSON/Movies/2023/10/13/HorrorMystery2/dados{n_file}.json'
                    s3.put_object(Bucket = bucket_name,Key= s3_key,Body = json_clear )
                    n_file += 1
                    dados.clear()
                    break
                else:
                    continue
                # Fazendo upload de qualquer dado restante
        if dados:
            json_file = json.dumps(dados, indent=4)
            json_clear = json_file[1:-1].replace("\n", "")
            # Fazendo upload dos dados diretamente para o S3
            s3_key = f'Raw/TMDB/JSON/Movies/2023/10/13/HorrorMystery2/dados{n_file}.json'
            s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_clear)
            n_file += 1
            dados.clear()
        else:
            print(f"Nenhum dado a ser enviado para o S3.")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'JSON enviado para o S3'
    }
process_data(pages_gener())