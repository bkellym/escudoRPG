from django.db import models

SOMA = '+'
SUBTRACAO = '-'

class Ficha(models.Model):
    id_personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)

    forca_vontade = models.IntegerField(null=False, default=0)
    forca_vontade_max = models.IntegerField(null=False, default=0)
    pontos_sangue = models.IntegerField(null=False, default=0)
    pontos_sangue_max = models.IntegerField(null=False, default=0)
    vitalidade = models.IntegerField(null=False, default=0)
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

    ############### Habilidades ###############
    # Talentos
    prontidao = models.IntegerField(null=True, blank=False, default=0)
    esportes = models.IntegerField(null=True, blank=False, default=0)
    briga = models.IntegerField(null=True, blank=False, default=0)
    esquiva = models.IntegerField(null=True, blank=False, default=0)
    empatia = models.IntegerField(null=True, blank=False, default=0)
    expressao = models.IntegerField(null=True, blank=False, default=0)
    intimidacao = models.IntegerField(null=True, blank=False, default=0)
    lideranca = models.IntegerField(null=True, blank=False, default=0)
    manha = models.IntegerField(null=True, blank=False, default=0)
    labia = models.IntegerField(null=True, blank=False, default=0)
    
    # Perícias
    empatia_animais = models.IntegerField(null=True, blank=False, default=0)
    oficios = models.IntegerField(null=True, blank=False, default=0)
    conducao = models.IntegerField(null=True, blank=False, default=0)
    etiqueta = models.IntegerField(null=True, blank=False, default=0)
    armas_fogo = models.IntegerField(null=True, blank=False, default=0)
    armas_branca = models.IntegerField(null=True, blank=False, default=0)
    performance = models.IntegerField(null=True, blank=False, default=0)
    seguranca = models.IntegerField(null=True, blank=False, default=0)
    furtividade = models.IntegerField(null=True, blank=False, default=0)
    sobrevivencia = models.IntegerField(null=True, blank=False, default=0)

    # Conhecimentos
    academicos = models.IntegerField(null=True, blank=False, default=0)
    computador = models.IntegerField(null=True, blank=False, default=0)
    financas = models.IntegerField(null=True, blank=False, default=0)
    investigacao = models.IntegerField(null=True, blank=False, default=0)
    direito = models.IntegerField(null=True, blank=False, default=0)
    linguistica = models.IntegerField(null=True, blank=False, default=0)
    medicina = models.IntegerField(null=True, blank=False, default=0)
    ocultismo = models.IntegerField(null=True, blank=False, default=0)
    politico = models.IntegerField(null=True, blank=False, default=0)
    ciencia = models.IntegerField(null=True, blank=False, default=0)

    ############### Virtudes ###############
    defesa = models.IntegerField(null=True, blank=True)
    iniciativa = models.IntegerField(null=True, blank=True)
    deslocamento = models.IntegerField(null=True, blank=True)
    consciencia = models.IntegerField(null=True, blank=True)
    autocontrole = models.IntegerField(null=True, blank=True)
    coragem = models.IntegerField(null=True, blank=True)
    humanidade = models.IntegerField(null=True, blank=True)


    def calculaPorcentagens(self):
        retorno = {}

        retorno['vitalidade'] = 100 * (self.vitalidade / self.vitalidade_max)
        retorno['sangue'] = 100 * (self.pontos_sangue / self.pontos_sangue_max)
        retorno['vontade'] = 100 * (self.forca_vontade / self.forca_vontade_max)

        return retorno

    def vitalidade_update(self, valor, operacao):
        valor = int(valor)

        if operacao == SOMA:
            vitalidade_nova = self.vitalidade + valor
        if operacao == SUBTRACAO:
            vitalidade_nova = self.vitalidade - valor

        if 0 <= vitalidade_nova <= self.vitalidade_max:
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