import json
import pandas as pd
import boto3
import requests
import os

def upload_to_s3(data, bucket_name, s3_key):
    session = boto3.Session(
        aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
        aws_secret_access_key='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'
    )

    s3_client = session.client('s3')

    try:
        # Converter os dados JSON em uma string
        json_data = json.dumps(data, ensure_ascii=False)

        # Enviar os dados JSON diretamente para o S3
        s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=json_data)
    except Exception as e:
        print(f"Erro ao enviar os dados para o S3: {str(e)}")

def lambda_handler(event, context):
    dados = []
    n_file = 1
    session = boto3.Session(
        aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
        aws_secret_access_key='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'
    )

    s3_client = session.client('s3')

    bucket_name = 'data-lake-desafio-final'
    s3_file_name = 'Raw/Local/CSV/Series/2023/09/26/series.csv'

    try:
        genero = 'Mystery'
        objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
        df = pd.read_csv(objeto['Body'], sep='|', na_values=[r'\N'], encoding='utf-8', dtype={'NomeDaColuna': str})
        horror_movies = df[df['genero'] == genero]

        # Remover filmes duplicados com base em uma coluna-chave, por exemplo, a coluna 'id'
        horror_movies = horror_movies.drop_duplicates(subset='id')

        # Converta os dados do DataFrame para JSON
        movies = horror_movies['tituloPincipal'].tolist()

        api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
        for id_movie in movies:
            url = f'https://api.themoviedb.org/3/search/tv?api_key={api_key}&query={id_movie}'
            response = requests.get(url)
            data = response.json()

            matching_row = horror_movies[horror_movies.iloc[:, 1] == id_movie]

            print(f"id_movie: {id_movie}")
            print(f"matching_row: {matching_row}")

            if not matching_row.empty:
                matching_data = matching_row.iloc[0].to_dict()
                matching_data.update(data['results'][0])
                dados.append(matching_data)

            if len(dados) == 100:
                # Fazer upload dos dados diretamente para o S3
                s3_key = f'Raw/TMDB/JSON/Series/2023/10/13/{genero}/dados{n_file}.json'
                upload_to_s3(dados, bucket_name, s3_key)
                n_file += 1
                dados.clear()

        # Fazer upload de qualquer dado restante
        if dados:
            s3_key = f'Raw/TMDB/JSON/Series/2023/10/13/{genero}/dados{n_file}.json'
            upload_to_s3(dados, bucket_name, s3_key)
        else:
            print(f"Nenhum dado a ser enviado para o S3.")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'JSON enviado para o S3'
    }

