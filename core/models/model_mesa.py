from django.db import models

class Mesa(models.Model):

    class Meta:
        verbose_name = ('mesa')
        verbose_name_plural = ('mesas')
        ordering = ['titulo']


    class Sistema(models.IntegerChoices):
        TALENTO = 1
        PERICIA = 2
        CONHECIMENTO = 3

    titulo = models.CharField(max_length=200)
    sistema = models.IntegerField(choices=Sistema.choices, null=False)
    mestre = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo