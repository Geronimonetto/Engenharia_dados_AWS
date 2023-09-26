import pandas as pd
import numpy as np

# Lendo o arquivo CSV
arquivo = pd.read_csv('/actors.csv')  # Certifique-se de que o caminho do arquivo esteja correto

# Encontrando o maior número de filmes
media_numero_Filmes = np.mean(arquivo['Average per Movie'].max())

#Localizando o ator com maior média por filme
ator_com_maior_media_por_filme = arquivo.loc[arquivo['Average per Movie'] == media_numero_Filmes, 'Actor']

# Imprimindo resultado
print(f'Ator com maior Média: {ator_com_maior_media_por_filme.values[0]}, Média por filme: {media_numero_Filmes}')