import pandas as pd

# Lendo o arquivo CSV
arquivo = pd.read_csv('/actors.csv')  # Certifique-se de que o caminho do arquivo esteja correto

#Transformando em um Dataframe
df = pd.DataFrame(arquivo)

# Ordenando o Dataframe
df2 = df.sort_values(by='#1 Movie')

# Contando os argumentos ordenados
reference = df['#1 Movie'].value_counts(ascending=False)

#Encontrando o maior valor
maior_numero = reference.max()

print(f'filmes frequentes: {reference.index[0]}, total: {maior_numero} vezes')