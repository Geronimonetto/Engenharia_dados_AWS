"""

Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a habilidade de voar e emitir som, porém,
tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console.


Imprima no console exatamente assim:

Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu

"""
from abc import ABC


class Passaro(ABC):
    def tipo_passaro(self, animal):
        pass

    def voar(self):
        pass

    def emitir_som(self, som):
        pass


class Pato(Passaro):
    def tipo_passaro(self, animal):
        print(f"{animal}")

    def voar(self):
        print("Voando...")

    def emitir_som(self, som):
        print(f"{som}")


class Pardal(Passaro):
    def tipo_passaro(self, animal):
        print(f"{animal}")

    def voar(self):
        print("Voando...")

    def emitir_som(self, som):
        print(f"{som}")


Patinho = Pato()
Pardal = Pardal()
Patinho.tipo_passaro("Pato")
Patinho.voar()
Patinho.emitir_som("Quack Quack")
Pardal.tipo_passaro("Pardal")
Pardal.voar()
Pardal.emitir_som("Piu Piu")
