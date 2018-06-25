from django.db import models
from django.utils import timezone
from . validacao import validate_even

class Jogada(models.Model):
    linha = models.CharField(max_length=1, validators=[validate_even])
    coluna = models.CharField(max_length=1, validators=[validate_even])
    vizinhos = models.CharField(max_length=1, validators=[validate_even], null = True)    
    created_date = models.DateTimeField(default=timezone.now)

# class Mina(models.Model):
#     linha = models.CharField(max_length=1, validators=[validate_even])
#     coluna = models.CharField(max_length=1, validators=[validate_even])