from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages

from .forms import JogadaForm
from .models import Jogada
from .negocio import Negocio

negocio = Negocio()
Jogada.objects.all().delete()

def post_list(request):
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            jogada.created_date = timezone.now()
            try:
                Jogada.objects.get(linha=jogada.linha,coluna=jogada.coluna)
            except:
                if negocio.verificaBomba(jogada.linha,jogada.coluna):
                    Jogada.objects.all().delete()
                    negocio.iniciarJogo()
                    return render(request, 'inicio.html', { 'perdeu': True })
                else:
                    jogada.vizinhos = negocio.verificaVizinhos(jogada.linha,jogada.coluna)
                    jogada.save()   
    else:
        form = JogadaForm()

    jogadas = Jogada.objects.all()

    return render(request, 'post_list.html', {'form': form, 'jogadas':jogadas})

def iniciar(request):
    if request.method == "GET":
         return render(request, 'inicio.html', { 'perdeu': False })