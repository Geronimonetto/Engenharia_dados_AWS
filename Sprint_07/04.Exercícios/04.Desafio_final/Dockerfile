# Usando a imagem do Python 3.11 como base
FROM python:3.11

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos do diretório local para o diretório de trabalho no container
COPY . /app

# Instalando a biblioteca boto3
RUN pip install boto3


# Comando para executar script Python
CMD ["python", "codigo.py"]