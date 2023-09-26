import boto3

session = boto3.Session(
    aws_access_key_id='AKIAZYAXJ7CO3HYOHO6D',
    aws_secret_access_key='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'
)

s3 = session.resource('s3')
bucket_name = 'data-lake-desafio-final'

# Enviando o arquivo 'movies.csv'
s3.Bucket(bucket_name).upload_file('movies.csv', 'Raw/Local/CSV/Movies/2023/09/26/movies.csv')

# Enviando o arquivo 'series.csv'
s3.Bucket(bucket_name).upload_file('series.csv', 'Raw/Local/CSV/Series/2023/09/26/series.csv')

print("Arquivos enviados com sucesso!")