from random import randint
from .models import Jogada

class Negocio:

    def __init__(self):
        print('iniciou negocio')
        self.iniciarJogo()
        
    def iniciarJogo(self):
        self.qtdLinhas = 5
        self.minas = self.colocaMinas(self.qtdLinhas)
        self.mapaQuantidades = []
        self.maximoJogadas = self.qtdLinhas*self.qtdLinhas-len(self.minas)
        self.jogadas = 0

    def colocaMinas(self, qtdLinhas):
        minas = []
        qtdMinas = randint(int((qtdLinhas*qtdLinhas)/5),int((qtdLinhas*qtdLinhas)/3))
        for i in range(qtdMinas):
            linha = randint(1,qtdLinhas)
            coluna = randint(1,qtdLinhas)
            if ([linha,coluna] in minas):
                qtdMinas += 1
            else:
                minas.append([linha,coluna])
                # mina = Mina(linha=linha,coluna=coluna)
                # mina.save()
                # print(Mina.objects.all())
        print(minas)
        return minas

    def verificaBomba(self, linha, coluna):
        posicao = [int(linha),int(coluna)]
        if (posicao in self.minas):
            return True
        else:
            return False

    def verificaVizinhos(self, linha, coluna): 
        qtdMinas = 0
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if self.verificaBomba(int(linha)+y,int(coluna)+x):
                    qtdMinas += 1
        return qtdMinas