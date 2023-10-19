import json
import pandas as pd
import boto3
import requests
from concurrent.futures import ThreadPoolExecutor


def upload_to_s3(data: list, bucket_name: str, s3_key: str) -> None:
    """
    func: A função trata de enviar os arquivos diretamente para o bucket do S3 sem precisar armazenar em memória
    temporária.

    Parameters
    ----------
    data
    bucket_name
    s3_key

    Returns
    -------

    """
    # Setando as chaves de acesso para permitir acesso ao bucket S3
    session = boto3.Session(
        aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
        aws_secret_access_key='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'
    )

    # Indicando qual serviço queremos utilizar
    s3_client = session.client('s3')

    try:
        # Convertendo os dados JSON em uma string
        json_data = json.dumps(data, ensure_ascii=False)

        # Enviando os dados JSON diretamente para o S3
        s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=json_data)

    except Exception as e:
        print(f"Erro ao enviar os dados para o S3: {str(e)}")


def lambda_handler(event, context):
    session = boto3.Session(
        aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
        aws_secret_access_key='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'
    )

    s3_client = session.client('s3')

    bucket_name = 'data-lake-desafio-final'
    s3_file_name = 'Raw/Local/CSV/Series/2023/09/26/series.csv'

    try:
        genero1 = 'Horror'
        genero2 = 'Mystery'
        # Setando o objeto do bucket S3 que queremos buscar
        objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)

        # Transformando o objeto setado do S3 em um dataframe
        df = pd.read_csv(objeto['Body'], sep='|', na_values=[r'\N'], dtype={'NomeDaColuna': str})

        # Dataframe com filmes de Horror
        movies_horror = df[df['genero'].str.contains(genero1, case=True, na=False)]

        # Dataframe com filmes de misterio
        movies_mystery = df[df['genero'].str.contains(genero2, case=True, na=False)]

        # Unindo os 2 Dataframes
        all_movies = pd.concat([movies_horror, movies_mystery])

        # Removendo valores duplicados
        all_movies_no_duplicates = all_movies.drop_duplicates()

        # Buscando id dos filmes no Dataframe
        lista_ids = all_movies_no_duplicates['id'].tolist()

        # Convertendo a lista de id para set, para remover duplicados
        conjunto_ids = set(lista_ids)

        # Convertendo em lista para iterar
        lista_ids_unicos = list(conjunto_ids)

        api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
        dados = []  # Lista para adicionar os dados que vão para o JSON
        n_file = 1  # Número para ordenar o nome dos arquivos

        for id_movie in lista_ids_unicos:
            url = f'https://api.themoviedb.org/3/find/{id_movie}?api_key={api_key}&external_source=imdb_id'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                data = response.json()

                if len(data['tv_results']) == 0:
                    if len(data['movie_results']) > 0:
                        dados.append(data['movie_results'][0])
                    else:
                        continue
                else:
                    dados.append(data['tv_results'][0])

                if len(dados) == 100:
                    # Fazendo upload dos dados diretamente para o S3
                    s3_key = f'Raw/TMDB/JSON/Series/2023/10/13/Horror-Mystery/dados{n_file}.json'
                    upload_to_s3(dados, bucket_name, s3_key)
                    n_file += 1
                    dados.clear()

        # Fazendo upload de qualquer dado restante
        if dados:
            s3_key = f'Raw/TMDB/JSON/Series/2023/10/13/Horror-Mystery/dados{n_file}.json'
            upload_to_s3(dados, bucket_name, s3_key)
        else:
            print(f"Nenhum dado a ser enviado para o S3.")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'JSON enviado para o S3'
    }

