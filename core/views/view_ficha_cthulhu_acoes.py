from math import ceil

from django.shortcuts import render, get_object_or_404, redirect
from core.models import *

SOMA = '+'
SUBTRACAO = '-'


def aumenta_pontos_vida(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.vida_update(value, SOMA)

    return redirect('/cthulhu/ficha/' + str(pk))


def diminui_pontos_vida(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.vida_update(value, SUBTRACAO)

    return redirect('/cthulhu/ficha/' + str(pk))


def aumenta_sanidade(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.sanidade_update(value, SOMA)

    return redirect('/cthulhu/ficha/' + str(pk))


def diminui_sanidade(request, pk):
    ficha_cthulhu: Ficha_Cthulhu = get_object_or_404(Ficha_Cthulhu, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_cthulhu.sanidade_update(value, SUBTRACAO)

    return redirect('/cthulhu/ficha/' + str(pk))


def check_campo_cthulhu(request):
    if request.method == "POST":
        id = request.POST['id']

        habilidade_cthulhu = Habilidade_Cthulhu.objects.get(id=id)

        if habilidade_cthulhu.checked:
            habilidade_cthulhu.checked = False
        else:
            habilidade_cthulhu.checked = True

        habilidade_cthulhu.save()

        return redirect('/cthulhu/ficha/' + str(habilidade_cthulhu.ficha.id_personagem.id))


def desmarcar(request, id):
    habilidade_cthulhu = get_object_or_404(Habilidade_Cthulhu, id=id)
    habilidade_cthulhu.checked = False
    habilidade_cthulhu.save()

    return redirect('/cthulhu/subir_nivel/' + str(habilidade_cthulhu.ficha.id_personagem.id))

def subir_nivel_habilidade(request):
    if request.method == "POST":
        id = request.POST['id']
        value = int(request.POST['value'])

        habilidade_cthulhu = Habilidade_Cthulhu.objects.get(id=id)
        habilidade_cthulhu.normal = habilidade_cthulhu.normal + value
        habilidade_cthulhu.bom = ceil(habilidade_cthulhu.normal/2)
        habilidade_cthulhu.extremo = ceil(habilidade_cthulhu.normal/5)
        habilidade_cthulhu.checked = False
        habilidade_cthulhu.save()

        return redirect('/cthulhu/subir_nivel/' + str(habilidade_cthulhu.ficha.id_personagem.id))