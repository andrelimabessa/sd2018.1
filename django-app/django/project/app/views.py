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
                jogada.save()   
    else:
        form = JogadaForm()

    jogadas = Jogada.objects.all()

    return render(request, 'post_list.html', {'form': form, 'jogadas':jogadas})

# def post_list(request):
#     if request.method == "POST":
#         form = JogadaForm(request.POST)
#         if form.is_valid():
#             jogada = form.save(commit=False)
#             jogada.created_date = timezone.now()
#             tupla = (int(jogada.linha), int(jogada.coluna))
#             jogada.vizinhos = int(negocio.bombas_vizinhas(tupla))
#             if negocio.tem_bomba(tupla):
#                 messages.success(request, 'Acertou uma bomba!', extra_tags='alert')
#                 Jogada.objects.all().delete()
#                 negocio.criar_novo_jogo()
#             elif negocio.get_contador() == 20:
#                 messages.success(request, 'Você venceu!', extra_tags='alert')
#                 Jogada.objects.all().delete()
#                 negocio.criar_novo_jogo()
#             else:
#                 jogada.save()
#     else:
#         form = JogadaForm()

#     jogadas = Jogada.objects.all()

#     return render(request, 'post_list.html', {'form': form, 'jogadas':jogadas})