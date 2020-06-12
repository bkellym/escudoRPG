from django.db import models


class Habilidade_Cthulhu(models.Model):

    class Meta:
        verbose_name = ('habilidade_cthulhu')
        verbose_name_plural = ('habilidades_cthulhu')
        ordering = ['titulo']

    class Coluna(models.IntegerChoices):
        COLUNA_1 = 1
        COLUNA_2 = 2
        COLUNA_3 = 3
        COLUNA_4 = 4

    ficha = models.ForeignKey('Ficha_Cthulhu', on_delete=models.CASCADE)
    coluna = models.IntegerField(choices=Coluna.choices, default=1)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    normal = models.IntegerField(null=True, blank=False, default=0)
    bom = models.IntegerField(null=True, blank=False, default=0)
    extremo = models.IntegerField(null=True, blank=False, default=0)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.ficha.id_personagem.nome + " | " + self.titulo