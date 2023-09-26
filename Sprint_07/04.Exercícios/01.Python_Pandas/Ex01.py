import pandas as pd
import numpy as np

# Lendo o arquivo CSV
arquivo = pd.read_csv('/actors.csv')  # Certifique-se de que o caminho do arquivo esteja correto

# Encontrando o maior número de filmes
maior_numero_filmes = np.max(arquivo['Number of Movies'])

# Encontrando o nome do ator com o maior número de filmes
ator_com_mais_filmes = arquivo.loc[arquivo['Number of Movies'] == maior_numero_filmes, 'Actor']

# Imprimindo resultado:
print(f"Nome do ator com o maior número de filmes: {ator_com_mais_filmes.values[0]} com {maior_numero_filmes} filmes")
