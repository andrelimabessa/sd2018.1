from django.shortcuts import render
from .campo_minado_negocio import CampoMinado
from .forms import JogadaForm
from .models import Jogada

COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
JOGADA_SEGURA = "Jogada Segura"
GAME_OVER = "Game Over"

campo_minado = CampoMinado()

def iniciar(request):
    jogo = JogadaForm(request.POST)
    return render(request, 'inicio_jogo.html', {'entrada': jogo})

def efetuar_jogada(request):
    global campo_minado
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            campo_minado = CampoMinado()
            campo_minado.criar_novo_jogo(linha, coluna)
            campo = campo_minado.retornar_campo()
    else:
        entrada = JogadaForm()

    mensagem = ''
    return render(request, 'campo.html', {'entrada': entrada, 'campo': campo, 'mensagem': mensagem})

def principal(request):
    global campo_minado
    if request.method == 'POST':
        entrada = JogadaForm(request.POST)
        if entrada.is_valid():
            linha = entrada.cleaned_data['linha']
            coluna = entrada.cleaned_data['coluna']
            mensagem = campo_minado.jogada(linha - 1, coluna - 1)
            jogadas_restantes = campo_minado.jogadas_restantes
            if mensagem == VITORIA:
                print("VITORIA ?")
                if jogadas_restantes == 0:
                    print("VITORIA!")
                    campo = campo_minado.retornar_campo
                    return render(request, 'fim.html', {'campo': campo, 'mensagem': mensagem})
            elif mensagem == COORDENADAS_INVALIDAS:
                print("COORDENADAS_INVALIDAS")
                campo = campo_minado.retornar_campo
                return render(request, 'campo.html',
                              {'entrada': entrada, 'campo': campo, 'mensagem': mensagem})
            elif mensagem == FIM_JOGO:
                print("FIM_JOGO")
                campo = campo_minado.retornar_campo
                return render(request, 'final_jogo.html', {'campo': campo, 'mensagem': mensagem})
            else:
                print("JOGADA")
                campo = campo_minado.retornar_campo
                return render(request, 'campo.html',
                              {'entrada': entrada, 'campo': campo, 'mensagem': mensagem})

