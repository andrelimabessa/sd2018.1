# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from forms import JogadaForm
from models import Jogada
from minefield import CampoMinado
from minefield import COORDENADAS_INVALIDAS
from minefield import GAME_OVER
from minefield import JOGADA_SEGURA

from django.shortcuts import render

game = CampoMinado()
game.criar_novo_jogo(4, 4)

def post_list(request):
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            jogada.created_date = timezone.now()
            linha = form.cleaned_data.get('linha')
            coluna = form.cleaned_data.get('coluna')

            if (game.jogada(linha, coluna) == GAME_OVER):
                status = GAME_OVER
                Jogada.objects.all().delete()
                game.criar_novo_jogo(4, 4)
            else:
                status = JOGADA_SEGURA
                jogada.save()
            
    else:
        form = JogadaForm()
        status = ''
    
    restante = game.contagem_jogadas()
    if restante == 0:
        status = "Você venceu !"
        game.criar_novo_jogo(4, 4)
    tabuleiro = game.get_tabuleiro()

    return render(request, 'post_list.html', {'form': form, 'tabuleiro': tabuleiro, 'status': status, 'restante': restante })