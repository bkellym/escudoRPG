from django.db import models

SOMA = '+'
SUBTRACAO = '-'


class Ficha_Cthulhu(models.Model):

    class Meta:
        verbose_name = 'ficha_cthulhu'
        verbose_name_plural = 'fichas_cthulhu'

    id_personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)

    pontos_vida = models.IntegerField(null=False, default=0)
    pontos_vida_max = models.IntegerField(null=False, default=0)
    sanidade = models.IntegerField(null=False, default=0)
    sanidade_max = models.IntegerField(null=False, default=0)

    ############### Atributos ###############
    FOR = models.IntegerField(null=True, blank=False, default=1)
    FOR_bom= models.IntegerField(null=True, blank=False, default=1)
    FOR_extremo = models.IntegerField(null=True, blank=False, default=1)
    CON = models.IntegerField(null=True, blank=False, default=1)
    CON_bom = models.IntegerField(null=True, blank=False, default=1)
    CON_extremo = models.IntegerField(null=True, blank=False, default=1)
    TAM = models.IntegerField(null=True, blank=False, default=1)
    TAM_bom = models.IntegerField(null=True, blank=False, default=1)
    TAM_extremo = models.IntegerField(null=True, blank=False, default=1)
    DES = models.IntegerField(null=True, blank=False, default=1)
    DES_bom = models.IntegerField(null=True, blank=False, default=1)
    DES_extremo = models.IntegerField(null=True, blank=False, default=1)
    APA = models.IntegerField(null=True, blank=False, default=1)
    APA_bom = models.IntegerField(null=True, blank=False, default=1)
    APA_extremo = models.IntegerField(null=True, blank=False, default=1)
    EDU = models.IntegerField(null=True, blank=False, default=1)
    EDU_bom = models.IntegerField(null=True, blank=False, default=1)
    EDU_extremo = models.IntegerField(null=True, blank=False, default=1)
    INT = models.IntegerField(null=True, blank=False, default=1)
    INT_bom = models.IntegerField(null=True, blank=False, default=1)
    INT_extremo = models.IntegerField(null=True, blank=False, default=1)
    POD = models.IntegerField(null=True, blank=False, default=1)
    POD_bom = models.IntegerField(null=True, blank=False, default=1)
    POD_extremo = models.IntegerField(null=True, blank=False, default=1)
    taxa_mov = models.IntegerField(null=True, blank=False, default=1)

    def __str__(self):
        return self.id_personagem.nome

    def calcula_porcentagens(self):
        retorno = {'vida': 100 * (self.pontos_vida / self.pontos_vida_max),
                   'sanidade': 100 * (self.sanidade / self.sanidade_max)}
        return retorno

    def vida_update(self, valor, operacao):
        valor = int(valor)

        if operacao == SOMA:
            vida_nova = self.pontos_vida + valor
        if operacao == SUBTRACAO:
            vida_nova = self.pontos_vida - valor

        if 0 <= vida_nova <= self.pontos_vida_max:
            self.pontos_vida = vida_nova
            self.save()

    def sanidade_update(self, valor, operacao):
        valor = int(valor)

        if operacao == SOMA:
            sanidade_nova = self.sanidade + valor
        if operacao == SUBTRACAO:
            sanidade_nova = self.sanidade - valor

        if 0 <= sanidade_nova <= self.sanidade_max:
            self.sanidade = sanidade_nova
            self.save()
