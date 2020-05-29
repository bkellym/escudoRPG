from django.db import models

# Create your models here.
class Personagem(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(null=True, blank=True)
    natureza = models.CharField(max_length=150, null=True, blank=True)
    comportamento = models.CharField(max_length=150, null=True, blank=True)
    cla = models.CharField(max_length=100, null=True, blank=True)
    ocupacao = models.CharField(max_length=100, null=True, blank=True)
    senhor = models.CharField(max_length=150, null=True, blank=True)
    conceito = models.CharField(max_length=150, null=True, blank=True)

class Ficha(models.Model):
    id_personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)

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
    academicos = models.IntegerField(null=True, blank=False, default=0)
    # Conhecimentos
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
    forca_vontade = models.IntegerField(null=True, blank=True)
    forca_vontade_max = models.IntegerField(null=True, blank=True)
    pontos_sangue = models.IntegerField(null=True, blank=True)
    pontos_sangue_max = models.IntegerField(null=True, blank=True)
    vitalidade = models.IntegerField(null=True, blank=True)
    vitalidade_max = models.IntegerField(null=True, blank=True)

class Extra(models.Model):

    class Tipo(models.IntegerChoices):
        DISCIPLINA = 1
        ANTECENDENTE = 2
        QUALIDADE = 3
        DEFEITO = 4

    id_personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)
    tipo = models.IntegerField(choices=Tipo.choices)
