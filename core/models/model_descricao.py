from django.db import models

class Descricao(models.Model):

    class Meta:
        verbose_name = ('descricao')
        verbose_name_plural = ('descricoes')

    class Tipo(models.IntegerChoices):
        DISCIPLINA = 1
        ANTECENDENTE = 2
        QUALIDADE = 3
        DEFEITO = 4

    titulo = models.CharField(max_length=150, null=True, blank=True)
    tipo = models.IntegerField(choices=Tipo.choices)
    nivel = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.titulo + " | " + self.nivel

