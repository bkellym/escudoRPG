from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(null=True, blank=True)
    natureza = models.CharField(max_length=150, null=True, blank=True)
    comportamento = models.CharField(max_length=150, null=True, blank=True)
    cla = models.CharField(max_length=100, null=True, blank=True)
    ocupacao = models.CharField(max_length=100, null=True, blank=True)
    senhor = models.CharField(max_length=150, null=True, blank=True)
    conceito = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nome