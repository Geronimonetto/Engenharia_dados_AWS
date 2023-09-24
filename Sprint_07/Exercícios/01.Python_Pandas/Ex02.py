import pandas as pd
import numpy as np

# Lendo o arquivo CSV
arquivo = pd.read_csv('/actors.csv')  # Certifique-se de que o caminho do arquivo esteja correto

# Encontrando o maior número de filmes
media_numero_Filmes = np.mean(arquivo['Number of Movies'])

# Imprimindo resultado
print(f'Média de filmes: {media_numero_Filmes}')