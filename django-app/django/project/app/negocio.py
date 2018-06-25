from random import randint
from .models import Jogada

class Negocio:

    def __init__(self):
        print('iniciou negocio')
        self.qtdLinhas = 5
        self.minas = self.colocaMinas(self.qtdLinhas)
        self.mapaQuantidades = []
        self.maximoJogadas = self.qtdLinhas*self.qtdLinhas-len(self.minas)

    def colocaMinas(self, qtdLinhas):
        minas = []
        qtdMinas = randint(int((qtdLinhas*qtdLinhas)/5),int((qtdLinhas*qtdLinhas)/3))
        for i in range(qtdMinas):
            linha = randint(0,qtdLinhas-1)
            coluna = randint(0,qtdLinhas-1)
            if ([linha,coluna] in minas):
                qtdMinas += 1
            else:
                minas.append([linha,coluna])
        return minas

    def verificaBomba(self, posicao,minas):
        if (posicao[0]>=0 and posicao[1]>=0) and (posicao[0]<qtdLinhas and posicao[1]<qtdLinhas):
            if (posicao in minas):
                return True
            else:
                return False
