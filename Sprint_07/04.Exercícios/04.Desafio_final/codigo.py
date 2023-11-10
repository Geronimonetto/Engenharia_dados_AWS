import boto3
from datetime import date
session = boto3.Session(
    aws_access_key_id='AKIAZYAXJ7CO2LO2CJG2',
    aws_secret_access_key='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'
)

s3 = session.resource('s3')
bucket_name = 'data-lake-desafio-final'

# Enviando o arquivo 'movies.csv'
s3.Bucket(bucket_name).upload_file('movies.csv', f'Raw/teste/CSV/Movies/{date.today().year}/{date.today().month}/{date.today().day}/movies.csv')

# Enviando o arquivo 'series.csv'
s3.Bucket(bucket_name).upload_file('series.csv', f'Raw/teste/CSV/Series/{date.today().year}/{date.today().month}/{date.today().day}/series.csv')

print("Arquivos enviados com sucesso!")