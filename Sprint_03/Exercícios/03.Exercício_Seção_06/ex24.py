"""
class Ordenadora:

    def __init__(self,listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        return list(self.listaBaguncada)


    def ordenacaoDecrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada,reverse=True)
        return list(self.listaBaguncada)



Crescente = Ordenadora([3,4,2,1,5])
print(Crescente.ordenacaoCrescente())
print(Crescente.ordenacaoDecrescente())

"""

class Ordenadora:

    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        return list(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada, reverse=True)
        print(self.listaBaguncada)


Crescente = Ordenadora([3, 4, 2, 1, 5])
print(Crescente.ordenacaoCrescente())
