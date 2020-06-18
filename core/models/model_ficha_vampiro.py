from django.db import models

SOMA = '+'
SUBTRACAO = '-'


class Ficha_Vampiro(models.Model):
    class Meta:
        verbose_name = ('ficha')
        verbose_name_plural = ('fichas')

    id_personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)

    forca_vontade = models.IntegerField(null=False, default=0)
    forca_vontade_max = models.IntegerField(null=False, default=0)
    pontos_sangue = models.IntegerField(null=False, default=0)
    pontos_sangue_max = models.IntegerField(null=False, default=0)
    vitalidade = models.IntegerField(null=False, default=0)
    dano_agravado = models.IntegerField(null=False, default=0)
    vitalidade_max = models.IntegerField(null=False, default=0)
    experiencia = models.IntegerField(null=False, default=0)

    ############### Atributos ###############
    # Físicos
    forca = models.IntegerField(null=True, blank=False, default=1)
    destreza = models.IntegerField(null=True, blank=False, default=1)
    vigor = models.IntegerField(null=True, blank=False, default=1)
    # Sociais
    carisma = models.IntegerField(null=True, blank=False, default=1)
    manipulacao = models.IntegerField(null=True, blank=False, default=1)
    aparencia = models.IntegerField(null=True, blank=False, default=1)
    # Mentais
    percepcao = models.IntegerField(null=True, blank=False, default=1)
    inteligencia = models.IntegerField(null=True, blank=False, default=1)
    raciocinio = models.IntegerField(null=True, blank=False, default=1)

    ############### Virtudes ###############
    defesa = models.IntegerField(null=True, blank=True)
    iniciativa = models.IntegerField(null=True, blank=True)
    deslocamento = models.IntegerField(null=True, blank=True)
    consciencia = models.IntegerField(null=True, blank=True)
    autocontrole = models.IntegerField(null=True, blank=True)
    coragem = models.IntegerField(null=True, blank=True)
    humanidade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id_personagem.nome

    def calcula_custos(self):
        retorno = {}

        if self.consciencia < 4:
            consciencia = self.consciencia * 2
        else:
            consciencia = self.consciencia * 4
        retorno['consciencia'] = consciencia

        if self.autocontrole < 4:
            autocontrole = self.autocontrole * 2
        else:
            autocontrole = self.autocontrole * 4
        retorno['autocontrole'] = autocontrole

        if self.consciencia < 4:
            coragem = self.coragem * 2
        else:
            coragem = self.coragem * 4
        retorno['coragem'] = coragem

        return retorno

    def calcula_porcentagens(self):
        retorno = {'vitalidade': 100 * (self.vitalidade / self.vitalidade_max),
                   'dano_agravado': 100 * (self.dano_agravado / self.vitalidade_max),
                   'sangue': 100 * (self.pontos_sangue / self.pontos_sangue_max),
                   'vontade': 100 * (self.forca_vontade / self.forca_vontade_max)}

        return retorno

    def vitalidade_update(self, valor, operacao):
        valor = int(valor)

        if operacao == SOMA:
            vitalidade_nova = self.vitalidade + valor
        if operacao == SUBTRACAO:
            vitalidade_nova = self.vitalidade - valor

        if 0 <= vitalidade_nova <= (self.vitalidade_max - self.dano_agravado):
            self.vitalidade = vitalidade_nova
            self.save()

    def sangue_update(self, valor, operacao):
        valor = int(valor)

        if operacao == SOMA:
            sangue_novo = self.pontos_sangue + valor
        if operacao == SUBTRACAO:
            sangue_novo = self.pontos_sangue - valor

        if 0 <= sangue_novo <= self.pontos_sangue_max:
            self.pontos_sangue = sangue_novo
            self.save()

    def vontade_update(self, valor, operacao):
        valor = int(valor)

        if operacao == SOMA:
            vontade_nova = self.forca_vontade + valor
        if operacao == SUBTRACAO:
            vontade_nova = self.forca_vontade - valor

        if 0 <= vontade_nova <= self.forca_vontade_max:
            self.forca_vontade = vontade_nova
            self.save()
