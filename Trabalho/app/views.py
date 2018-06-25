from django.shortcuts import render
from .campominado_s import CampoMinadoView
from .forms import JogadaForm
from .models import Jogada
# Create your views here.

VITORIA = "Parabéns!"
COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
FIM_JOGO = "Game Over"

objeto = CampoMinadoView()

def iniciar(request):
    jogo = JogadaForm(request.POST)
    return render(request, 'inicio.html', {'entrada': jogo})


def jogada(request):
    global objeto
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            objeto = CampoMinadoView()
            objeto.novo_jogo(linha, coluna)
            matriz = objeto.retornar_matriz()
    else:
        entrada = JogadaForm()

    mensagem = ''
    return render(request, 'matriz.html', {'entrada': entrada, 'matriz': matriz, 'mensagem': mensagem})


def main(request):
    global objeto
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            mensagem = objeto.jogada(linha - 1, coluna - 1)
            jogadas_restantes = objeto.jogadas_restantes
            if mensagem == VITORIA:
                print("VITORIA ?")
                if jogadas_restantes == 0:
                    print("VITORIA!")
                    matriz = objeto.retornar_matriz
                    return render(request, 'fim.html', {'matriz': matriz, 'mensagem': mensagem})
            elif mensagem == COORDENADAS_INVALIDAS:
                print("COORDENADAS_INVALIDAS")
                matriz = objeto.retornar_matriz
                return render(request, 'matriz.html',
                              {'entrada': entrada, 'matriz': matriz, 'mensagem': mensagem})
            elif mensagem == FIM_JOGO:
                print("FIM_JOGO")
                matriz = objeto.retornar_matriz
                return render(request, 'fim.html', {'matriz': matriz, 'mensagem': mensagem})
            else:
                print("JOGADA")
                matriz = objeto.retornar_matriz
                return render(request, 'matriz.html',{'entrada': entrada, 'matriz': matriz, 'mensagem': mensagem})
