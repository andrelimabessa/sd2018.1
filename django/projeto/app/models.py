from django.db import models
from django.utils import timezone
from . validacao import validate_even

class Jogada(models.Model):
    linha = models.CharField(max_length=1, validators=[validate_even])
    coluna = models.CharField(max_length=1, validators=[validate_even])
    vizinhos = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)