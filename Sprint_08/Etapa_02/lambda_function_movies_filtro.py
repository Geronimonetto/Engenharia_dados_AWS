import json
import pandas as pd
import boto3
import requests


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
    """
    func: A Função trata-se de uma função parametro do AWS Lambda, porém o código em si restante trata-se de
    transformar os dados buscados no S3 em um dataframe para combinar com os dados da API do TMDB
    Parameters
    ----------
    event
    context

    Returns
    -------

    """
    dados = []  # Lista para adicionar os dados que vão para o json
    n_file = 1  # Numero para ordenar o nome dos arquivos

    session = boto3.Session(
        aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
        aws_secret_access_key='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'
    )

    s3_client = session.client('s3')

    bucket_name = 'data-lake-desafio-final'
    s3_file_name = 'Raw/Local/CSV/Movies/2023/09/26/movies.csv'

    try:
        genero = 'Horror'

        # Setando o objeto do bucket S3 que queremos buscar
        objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)

        # Transformando o objeto setado do S3 em um dataframe
        df = pd.read_csv(objeto['Body'], sep='|', na_values=[r'\N'], dtype={'NomeDaColuna': str})
        horror_movies = df[df['genero'] == genero]

        # Removendo filmes duplicados com base em uma coluna-chave, por exemplo, a coluna 'id'
        horror_movies = horror_movies.drop_duplicates(subset='id')

        # Buscando os id do dataframe por genero e colocando em uma lista para iterar
        movies = horror_movies['id'].tolist()

        api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
        for id_movie in movies:
            url = f'https://api.themoviedb.org/3/movie/{id_movie}?api_key={api_key}'
            response = requests.get(url)
            data = response.json()

            dados.append(data)

            if len(dados) == 100:
                # Fazendo upload dos dados diretamente para o S3
                s3_key = f'Raw/TMDB/JSON/Movies/2023/10/13/{genero}_filtro/dados{n_file}.json'
                upload_to_s3(dados, bucket_name, s3_key)
                n_file += 1
                dados.clear()

        # Fazendo upload de qualquer dado restante
        if dados:
            s3_key = f'Raw/TMDB/JSON/Movies/2023/10/13/{genero}_filtro/dados{n_file}.json'
            upload_to_s3(dados, bucket_name, s3_key)
        else:
            print(f"Nenhum dado a ser enviado para o S3.")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'JSON enviado para o S3'
    }