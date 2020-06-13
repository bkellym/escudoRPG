from math import ceil, floor

from django.shortcuts import render, get_object_or_404, redirect
from core.models import *

SOMA = '+'
SUBTRACAO = '-'

def ficha_cthulhu(request, pk, template_name="core/ficha_cthulhu.html"):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    ficha_cthulhu = Ficha_Cthulhu.objects.get(id_personagem=personagem.pk)
    entidade['ficha'] = ficha_cthulhu
    entidade['porcentagem'] = ficha_cthulhu.calculaPorcentagens()

    habilidades = Habilidade_Cthulhu.objects.all().filter(ficha=ficha_cthulhu.id).order_by('titulo')
    if habilidades.exists():
        total = len(habilidades)

        coluna1 = []
        for i in range (0, floor(total/4)):
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


def aumenta_pontos_vida(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.vida_update(value, SOMA)

    return redirect('/ficha_cthulhu/' + str(pk))


def diminui_pontos_vida(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.vida_update(value, SUBTRACAO)

    return redirect('/ficha_cthulhu/' + str(pk))


def aumenta_sanidade(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.sanidade_update(value, SOMA)

    return redirect('/ficha_cthulhu/' + str(pk))


def diminui_sanidade(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.sanidade_update(value, SUBTRACAO)

    return redirect('/ficha_cthulhu/' + str(pk))


def check_campo_cthulhu(request):
    if request.method == "POST":
        id = request.POST['id']

        habilidade_cthulhu = Habilidade_Cthulhu.objects.get(id=id)

        if habilidade_cthulhu.checked:
            habilidade_cthulhu.checked = False
        else:
            habilidade_cthulhu.checked = True

        habilidade_cthulhu.save()

        return redirect('/ficha_cthulhu/' + str(habilidade_cthulhu.ficha.id_personagem.id))