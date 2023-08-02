"""
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:

Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!


import random
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática

mediana
media
valor_minimo
valor_maximo

"""

import random
from statistics import median

random_list = random.sample(range(500), 50)

mediana = median(random_list)
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
