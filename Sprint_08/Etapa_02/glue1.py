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


df = spark.read.option("multiline", "true").parquet(source_file)

data_de_hoje = datetime.date.today()

# Extrair o ano, mês e dia da data de hoje
ano_hoje = data_de_hoje.year
mes_hoje = data_de_hoje.month
dia_hoje = data_de_hoje.day

# Adicionar as colunas ao DataFrame
df = df.withColumn("ano_coleta", lit(ano_hoje))
df = df.withColumn("mes_coleta", lit(mes_hoje))
df = df.withColumn("dia_coleta", lit(dia_hoje))

df = df.drop("homepage", "video", "credits_cast", 'status',"genres","imdb_id","adult","backdrop_path","belongs_to_collection","budget","poster_path","overview","tagline",
              'original_language', 'credits', 'production_companies', 'production_countries', 'profile_path',"spoken_languages","tagline",'id_companhia_producao','original_title', 'release_date')

df.write \
    .option('header', True) \
    .format('parquet') \
    .partitionBy("ano_coleta", "mes_coleta", "dia_coleta") \
    .mode('overwrite') \
    .save(target_path)


