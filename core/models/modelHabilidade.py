from django.db import models


class Habilidade(models.Model):

    class Tipo(models.IntegerChoices):
        TALENTO = 1
        PERICIA = 2
        CONHECIMENTO = 3

    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    tipo = models.IntegerField(choices=Tipo.choices)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=False, default=0)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.ficha.id_personagem.nome + " | " + self.titulo