from django.shortcuts import render
from django.utils import timezone
from .models import Jogada
from .forms import JogadaForm

# Create your views here.
def post_list(request):
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            jogada.created_date = timezone.now()
            jogada.save()
    else:
        form = JogadaForm()

    jogadas = Jogada.objects.all()

    return render(request, 'app/post_list.html', {'form': form, 'jogadas':jogadas})