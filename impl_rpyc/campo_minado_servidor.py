from random import randint
from ast import literal_eval
import os.path
import rpyc
from rpyc.utils.server import ThreadedServer
import sys

class CampoMinadoServidor(rpyc.Service):

    class exposed_CampoMinadoServidorImpl(object):
        def __init__(self):
            self.PATH = '../save/bombas.save'
            self.__contador = None
            self.__bombas = None
            self. __arquivo = None

        def exposed_criar_novo_jogo(self):
            self.__bombas = []
            self.__gerar_bombas()
            self.__criar_save()
            self.__contador = -1

        def exposed_carregar_partida(self):
            var = self.__carregar_partida()
            self.__contador = 0
            self.__criar_save()
            return var
        
        def exposed_realizar_jogada(self, tupla):
            result = self.__tem_bomba(tupla)
            if result:
                var = "sim"
                self.__contador = 0
            else:
                self.__salvar_jogada(tupla)
                var = self.__bombas_vizinhas(tupla)
            return var
        
        def exposed_save_existe(self):
            var = False
            if os.path.isfile(self.PATH):
                var = True
            return var
        
        def exposed_incrementar_jogada(self):
            self.__contador = self.__contador + 1
            return str(self.__contador)
        
        def exposed_vitoria(self):
            var = False
            if self.__contador == 40:
                var = True
                self.__contador = 0
                self.__deletar_arquivo()
            return var
        
        def __carregar_partida(self):
            arq = open(self.PATH, 'r')
            linha = arq.readline() # primeira linha recupera as bombas
            self.__bombas = literal_eval(linha)
            return arq.readline() # segunda linha recupera os botoes clicados
        
        def __gerar_bombas(self):
            while(len(self.__bombas) < 14):
                linha = randint(0,5)
                coluna = randint(0,8)
                tupla = (linha,coluna)
                if tupla not in self.__bombas:
                    self.__bombas.append(tupla)

        def __tem_bomba(self, tupla):
            var = False
            if tupla in self.__bombas:
                var = True
                self.__deletar_arquivo()
            return var
        
        def __bombas_vizinhas(self, tupla):
            lista = []
            lista.append((tupla[0]-1,tupla[1]-1))
            lista.append((tupla[0]-1,tupla[1]))
            lista.append((tupla[0]-1,tupla[1]+1))
            lista.append((tupla[0],tupla[1]-1))
            lista.append((tupla[0],tupla[1]+1))
            lista.append((tupla[0]+1,tupla[1]-1))
            lista.append((tupla[0]+1,tupla[1]))
            lista.append((tupla[0]+1,tupla[1]+1))
            qtd_bombas = [i for i in self.__bombas if i in lista]
            return str(len(qtd_bombas))

        def __criar_save(self):
            self.__arquivo = open(self.PATH, 'w+')
            texto = str(self.__bombas)
            self.__arquivo.writelines(texto+"\n")
            self.__arquivo.close()
        
        def __salvar_jogada(self, tupla):
            self.__arquivo = open(self.PATH, 'a')
            texto = "button"+str(tupla[0])+str(tupla[1])+"_click,"
            self.__arquivo.writelines(texto)
            self.__arquivo.close()
        
        def __deletar_arquivo(self):
            self.__arquivo.close()
            os.remove(self.PATH)

if __name__ == "__main__":
    try:
        thread = ThreadedServer(CampoMinadoServidor, port=18861)
        thread.start()
        
    except:
        for val in sys.exc_info():
            print(val)
    
