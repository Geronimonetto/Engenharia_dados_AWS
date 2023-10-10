import requests
import pandas as pd
import json
from IPython.display import display

api_key = "ea33ae145ce37250f8ab09b9583b7a7f"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"


class BuscaFilmes:

    def __init__(self, url: str) -> None:
        self.url = url
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.filmes = []

    def pegando_dados(self):
        for movie in self.data['results']:
            df = {'Titulo': movie['title'],
                  'Data de lançamento': movie['release_date'],
                  'Visão geral': movie['overview'],
                  'Votos': movie['vote_count'],
                  'Média de votos:': movie['vote_average']}
            self.filmes.append(df)
            with open("filmes_gerais.json", "w") as arquivo:
                json.dump(self.data, arquivo, indent=4)

    def imprimindo_dados(self):
        df = pd.DataFrame(self.filmes)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        display(df)

    def run(self):
        self.pegando_dados()
        self.imprimindo_dados()


if __name__ == "__main__":
    buscador_filmes = Busca_Filmes(url)
    buscador_filmes.run()
