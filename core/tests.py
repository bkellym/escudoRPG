from django.test import TestCase
from .models import *


class FichaVampiroTest(TestCase):
    def setUp(self) -> None:
        Personagem.objects.create(nome="Lillian")
        personagem: Personagem = Personagem.objects.get(nome="Lillian")
        Ficha_Vampiro.objects.create(id_personagem=personagem)
        ficha: Ficha_Vampiro = Ficha_Vampiro.objects.get(id_personagem=personagem)
        ficha.forca_vontade = 4
        ficha.forca_vontade_max = 4
        ficha.pontos_sangue = 10
        ficha.pontos_sangue_max = 10
        ficha.vitalidade = 8
        ficha.dano_agravado = 0
        ficha.vitalidade_max = 8
        ficha.save()

    def test_calcula_procentagem_100(self):
        ''' Testando se retorna todos os calculos 100% '''
        personagem: Personagem = Personagem.objects.get(nome="Lillian")
        ficha:      Ficha_Vampiro = Ficha_Vampiro.objects.get(id_personagem=personagem)

        self.assertEqual(ficha.calcula_porcentagens(),
                         {'vitalidade': 100, 'dano_agravado': 0, 'sangue': 100, 'vontade': 100})
