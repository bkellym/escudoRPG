from math import floor

from django.shortcuts import render, get_object_or_404
from core.models import *

SOMA = '+'
SUBTRACAO = '-'


def ficha_cthulhu(request, pk, template_name="core/ficha_cthulhu.html"):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    ficha_cthulhu: Ficha_Cthulhu = Ficha_Cthulhu.objects.get(id_personagem=personagem.pk)
    entidade['ficha'] = ficha_cthulhu
    entidade['porcentagem'] = ficha_cthulhu.calcula_porcentagens()

    habilidades = Habilidade_Cthulhu.objects.all().filter(ficha=ficha_cthulhu.pk).order_by('titulo')
    if habilidades.exists():
        total = len(habilidades)

        coluna1 = []
        for i in range(0, floor(total/4)):
            coluna1.append(habilidades[i])

        coluna2 = []
        for i in range(floor(total / 4), 2 * floor(total / 4)):
            coluna2.append(habilidades[i])

        coluna3 = []
        for i in range(2 * floor(total / 4), 3 * floor(total / 4)):
            coluna3.append(habilidades[i])

        coluna4 = []
        for i in range(3 * floor(total / 4), total):
            coluna4.append(habilidades[i])

        colunas = [coluna1, coluna2, coluna3, coluna4]

        entidade['colunas'] = colunas
        entidade['habilidades'] = habilidades

    return render(request, template_name, {'entidade': entidade})


def ficha_cthulhu_upar(request, pk, template_name="core/ficha_cthulhu_upar.html"):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    ficha_cthulhu: Ficha_Cthulhu = Ficha_Cthulhu.objects.get(id_personagem=personagem.pk)
    entidade['ficha'] = ficha_cthulhu
    entidade['porcentagem'] = ficha_cthulhu.calcula_porcentagens()

    habilidades = Habilidade_Cthulhu.objects.all().filter(ficha=ficha_cthulhu.pk).order_by('titulo')
    if habilidades.exists():
        total = len(habilidades)

        coluna1 = []
        for i in range(0, floor(total/4)):
            coluna1.append(habilidades[i])

        coluna2 = []
        for i in range(floor(total / 4), 2 * floor(total / 4)):
            coluna2.append(habilidades[i])

        coluna3 = []
        for i in range(2 * floor(total / 4), 3 * floor(total / 4)):
            coluna3.append(habilidades[i])

        coluna4 = []
        for i in range(3 * floor(total / 4), total):
            coluna4.append(habilidades[i])

        colunas = [coluna1, coluna2, coluna3, coluna4]

        entidade['colunas'] = colunas
        entidade['habilidades'] = habilidades

    return render(request, template_name, {'entidade': entidade})
