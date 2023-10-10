import boto3
import json
import requests

def lambda_handler(event, context):
    pass

def count_page() -> list:
    """
    :func: A função trata de busca a quantidade total de páginas da requisição para que
    a função run_data percorra os dados das páginas.

    :return: dados
    """
    url = f'https://api.themoviedb.org/3/discover/movie?page=1&api_key={api_key}&with_genres={gender}'  # URL da 1° página
    response = requests.get(url).json()
    dados = [dados for dados in range(1, response.get('total_pages') + 1)]  # Lista com a quantidade de páginas
    return dados
    
    
def send_data(json_filename: str, type_gender_func: str, number_file: int) -> None:
    """
    :func: A função recebe os dados do armazenamento temporário do lambda e envia para o S3 particionado com 100 
    registros cada.
    :param json_filename: 
    :param type_gender_func: 
    :param number_file: 
    :return: None
    """
    bucket_name = 'data-lake-desafio-final'
    session = boto3.Session(
        aws_access_key_id='AKIAZYAXJ7CO3HYOHO6D',
        aws_secret_access_key='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'
    )
    s3 = session.client('s3')  # Usando o S3 para enviar os dados para o Bucket
    s3.upload_file(json_filename, bucket_name,
                   f"Raw/TMDB/JSON/Movies/2023/10/09/{type_gender_func}/data_{number_file}.json")


def run_data(page_number: list) -> None:
    """
    :func: A função trata de receber como parâmetro a função count_page que tem como argumento uma lista com a
    quantidade de páginas para que percorra a quantidade de páginas modificando a URL da API.
    :param page_number: count_page()
    :return: None
    """
    movies = []
    number_file = 1

    for count in page_number:
        url = f'https://api.themoviedb.org/3/discover/movie?page={count}&api_key={api_key}&with_genres={gender}'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            if 'results' in data:
                movies.extend(data['results'])
                if len(movies) == 100:
                    # Criando arquivo com 100 registos para enviar pro S3
                    json_filename = f"/tmp/data_{number_file}.json"
                    with open(json_filename, 'w', encoding='utf-8') as data_movies:
                        json.dump(movies, data_movies, indent=5)

                    # # Enviado arquivo para o S3
                    send_data(json_filename, type_gender, number_file)

                    # Limpando lista
                    number_file += 1
                    movies.clear()
        else:
            break



gender = 27
type_gender = 'Terror'
api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
run_data(count_page())

# Código executado e finalizado em 1 min e 50 segundos