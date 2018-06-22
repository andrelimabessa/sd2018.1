from django import forms
from .models import Jogada

class JogadaForm(forms.ModelForm):
    
    linha = forms.IntegerField(label='Linha')
    coluna = forms.IntegerField(label='Coluna')