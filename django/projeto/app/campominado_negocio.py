from random import randint
from ast import literal_eval
import os.path
import sys

class CampoMinadoNegocio:

    def __init__(self):
        self.__bombas = None
        self.criar_novo_jogo()

    def criar_novo_jogo(self):
        self.__bombas = []
        self.__gerar_bombas()
        
    def vitoria(self):
        var = False
        if self.__contador == 20:
            var = True
            self.__contador = 0
            self.__deletar_arquivo()
        return var

    def tem_bomba(self, tupla):
        var = False
        if tupla in self.__bombas:
            var = True
        return var
        
    def bombas_vizinhas(self, tupla):
        linha = tupla[0]
        coluna = tupla[1]
        lista = []
        lista.append((linha-1,coluna-1))
        lista.append((linha-1,coluna))
        lista.append((linha-1,coluna+1))
        lista.append((linha,coluna-1))
        lista.append((linha,coluna+1))
        lista.append((linha+1,coluna-1))
        lista.append((linha+1,coluna))
        lista.append((linha+1,coluna+1))
        qtd_bombas = [i for i in self.__bombas if i in lista]
        return int(len(qtd_bombas))
        
    def __gerar_bombas(self):
        while(len(self.__bombas) < 5):
            linha = randint(1,5)
            coluna = randint(1,5)
            tupla = (linha,coluna)
            if tupla not in self.__bombas:
                self.__bombas.append(tupla)

if __name__ == "__main__":
    try:
        pass
    except:
        for val in sys.exc_info():
            print(val)
    
