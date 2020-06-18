from django.db import models


class Descricao(models.Model):

    class Meta:
        verbose_name = 'descricao'
        verbose_name_plural = 'descricoes'

    class Tipo(models.IntegerChoices):
        DISCIPLINA = 1
        ANTECENDENTE = 2
        QUALIDADE = 3
        DEFEITO = 4

    titulo = models.CharField(max_length=150, null=True, blank=True)
    tipo = models.IntegerField(choices=Tipo.choices)
    nivel = models.IntegerField(null=False, blank=False, default=0)
    nome = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    observacao = models.TextField(max_length=500, null=True, blank=True)
    sistema = models.TextField(max_length=500, null=True, blank=True)
    teste = models.TextField(max_length=500, null=True, blank=True)
    dificuldade = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.titulo + " | " + str(self.nivel)
