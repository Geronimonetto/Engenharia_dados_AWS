import sys
import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, expr, year, concat_ws, month, lit
from pyspark.sql.types import StructType, StructField, StringType
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = glueContext.create_dynamic_frame.from_options(
"s3",{"paths": [source_file]},format='json')

df = df.toDF()
columns_to_drop = ['adult', 'backdrop_path', 'belongs_to_collection', 'budget', 'overview', 'tagline', 'revenue',
                   'poster_path']
df = df.drop(*columns_to_drop)
desired_columns = ['id', 'imdb_id', 'credits', 'genres', 'homepage', 'original_language', 'original_title',
                   'popularity', 'production_companies', 'production_countries', 'release_date', 'runtime',
                   'spoken_languages', 'status', 'title', 'video', 'vote_average', 'vote_count']
df = df.select(*desired_columns)
df = df.withColumn("genre_1_id", col("genres")[0].getItem("id"))
df = df.withColumn("genre_1_name", col("genres")[0].getItem("name"))
df = df.withColumn("genre_2_id", col("genres")[1].getItem("id"))
df = df.withColumn("genre_2_name", col("genres")[1].getItem("name"))
df = df.withColumn("genre_3_id", col("genres")[2].getItem("id"))
df = df.withColumn("genre_3_name", col("genres")[2].getItem("name"))
df = df.drop('genres')
# Define the desired column order for better alignment
desired_columns = [
    'id', 'imdb_id', 'title', 'original_title', 'original_language', 'release_date',
    'runtime', 'popularity', 'vote_average', 'vote_count',
    'homepage', 'status', 'video',
    'genre_1_id', 'genre_1_name', 'genre_2_id', 'genre_2_name', 'genre_3_id', 'genre_3_name',
    'production_companies', 'production_countries',
    'credits',  # Credits, containing cast and crew, may require further column organization
]
df = df.withColumn("production_companies", explode("production_companies"))
df = df.drop('spoken_languages')
# Reorder the columns
df = df.select(*desired_columns)
df = df.withColumn("credits_cast", explode(col("credits.cast")))
df = df.withColumn("credit_id", col("credits_cast.credit_id"))
df = df.withColumn("gender", col("credits_cast.gender"))
df = df.withColumn("id", col("credits_cast.id"))
df = df.withColumn("known_for_department", col("credits_cast.known_for_department"))
df = df.withColumn("name", col("credits_cast.name"))
df = df.withColumn("order", col("credits_cast.order"))
df = df.withColumn("original_name", col("credits_cast.original_name"))
df = df.withColumn("popularity", col("credits_cast.popularity"))
df = df.withColumn("profile_path", col("credits_cast.profile_path"))
df = df.withColumn("genres_combined", concat_ws(" - ", col("genre_1_name"), col("genre_2_name"), col("genre_3_name")))

df = df.withColumn("production_company_id", col("production_companies.id"))
df = df.withColumn("production_company_name", col("production_companies.name"))
df = df.withColumn("production_company_origin_country", col("production_companies.origin_country"))

df = df.withColumn("production_countries", explode(col("production_countries")))
df = df.withColumn("country_code", col("production_countries.iso_3166_1"))
df = df.withColumn("country_name", col("production_countries.name"))

df = df.drop("homepage", "video", "release_date", "credits_cast", 'status', 'genre_1_id', 'genre_1_name', 'genre_2_id',
             'genre_2_name', 'genre_3_id', 'genre_3_name', 'original_language', 'credits',
             'production_company_origin_country', 'production_companies', 'production_countries', 'profile_path')
# Obter a data de hoje
data_de_hoje = datetime.date.today()

# Extrair o ano, mês e dia da data de hoje
ano_hoje = data_de_hoje.year
mes_hoje = data_de_hoje.month
dia_hoje = data_de_hoje.day

# Adicionar as colunas ao DataFrame
df = df.withColumn("ano_coleta", lit(ano_hoje))
df = df.withColumn("mes_coleta", lit(mes_hoje))
df = df.withColumn("dia_coleta", lit(dia_hoje))
caminho_trusted = "s3://data-lake-desafio-final/Trusted/Movies/"
df.write \
    .option('header', True) \
    .format('parquet') \
    .partitionBy("ano_coleta", "mes_coleta", "dia_coleta") \
    .mode('overwrite') \
    .save(caminho_trusted)

