from django.db import models

class Extra(models.Model):

    class Tipo(models.IntegerChoices):
        DISCIPLINA = 1
        ANTECENDENTE = 2
        QUALIDADE = 3
        DEFEITO = 4
        INVENTARIO = 5

    id_personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)
    tipo = models.IntegerField(choices=Tipo.choices)

