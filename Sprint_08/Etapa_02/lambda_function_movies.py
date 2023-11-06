import json
import pandas as pd
import boto3
import requests
from datetime import date


def lambda_handler(event,context):
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

        api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
        dados = []  # Lista para adicionar os dados que vão para o JSON
        n_file = 1  # Número para ordenar o nome dos arquivos
        for id_movie in lista_ids_unicos:

            url = f'https://api.themoviedb.org/3/movie/{id_movie}?api_key={api_key}&append_to_response=credits'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                data = response.json()
                dados.append(data)
            else:
                continue

            if len(dados) == 100:
                json_file = json.dumps(dados, indent=4)
                # Fazendo upload dos dados diretamente para o S3
                s3_key = f'Raw/TMDB/JSON/Movies/{date.today().year}/{date.today().month}/{date.today().day}/HorrorMystery/dados{n_file}.json'
                s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_file)
                n_file += 1
                dados.clear()

        # Fazendo upload de qualquer dado restante
        if dados:
            json_file = json.dumps(dados, indent=4)
            # Fazendo upload dos dados diretamente para o S3
            s3_key = f'Raw/TMDB/JSON/Series/{date.today().year}/{date.today().month}/{date.today().day}/HorrorMystery/dados{n_file}.json'
            s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_file)
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
