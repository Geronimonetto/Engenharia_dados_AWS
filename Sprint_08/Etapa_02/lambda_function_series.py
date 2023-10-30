import json
import pandas as pd
import boto3
import requests


def lambda_handler():
    s3 = boto3.client('s3',
                      aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
                      aws_secret_access_key='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'
                      )

    bucket_name = 'data-lake-desafio-final'
    s3_file_name = 'Raw/Local/CSV/Series/2023/09/26/series.csv'

    try:
        genero1 = 'Horror'
        genero2 = 'Mystery'
        # Setando o objeto do bucket S3 que queremos buscar
        objeto = s3.get_object(Bucket=bucket_name, Key=s3_file_name)

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
                    pesquisa = data['tv_results'][0]['id']
                    url = f'https://api.themoviedb.org/3/tv/{pesquisa}?api_key=ea33ae145ce37250f8ab09b9583b7a7f&append_response=credits'
                    response_credits = requests.get(url)
                    if response_credits.status_code == 200:
                        data_credits = response_credits.json()
                        dados.append(data_credits)
                    else:
                        continue

                if len(dados) == 100:
                    json_file = json.dumps(dados, indent=4)
                    json_clear = json_file[1:-1].replace("\n", "")
                    # Fazendo upload dos dados diretamente para o S3
                    s3_key = f'Raw/TMDB/JSON/Series/2023/10/13/HorrorMystery/dados{n_file}.json'
                    s3.put_object(Bucket=bucket_name, Key=s3_key, Body=json_clear)
                    n_file += 1
                    dados.clear()

        # Fazendo upload de qualquer dado restante
        if dados:
            json_file = json.dumps(dados, indent=4)
            json_clear = json_file[1:-1].replace("\n", "")
            # Fazendo upload dos dados diretamente para o S3
            s3_key = f'Raw/TMDB/JSON/Series/2023/10/13/HorrorMystery/dados{n_file}.json'
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

lambda_handler()