from django.shortcuts import render, get_object_or_404, redirect
from core.models import *

SOMA = '+'
SUBTRACAO = '-'


def check_campo(request):
    if request.method == "POST":
        id = request.POST['id']

        habilidade = Habilidade.objects.get(id=id)

        if habilidade.checked:
            habilidade.checked = False
        else:
            habilidade.checked = True

        habilidade.save()

        return redirect('/ficha/' + str(habilidade.ficha.id_personagem.id))

def upar_habilidade(request):
    if request.method == "POST":
        id = request.POST['id']
        habilidade = Habilidade.objects.get(id=id)
        ficha = Ficha.objects.get(id=habilidade.ficha.id)

        if habilidade.valor == 0:
            custo_xp = 3
        else:
            custo_xp = habilidade.valor * 2
            if habilidade.valor >= 4:
                custo_xp = custo_xp * 2

        if ficha.experiencia - custo_xp >= 0:
            habilidade.valor = habilidade.valor + 1
            habilidade.checked = False
            ficha.experiencia = ficha.experiencia - custo_xp
            habilidade.save()
            ficha.save()

        return redirect('/subir_nivel/' + str(habilidade.ficha.id_personagem.id))

def upar_virtude(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        campo = request.POST['campo']
        ficha = get_object_or_404(Ficha, id=id)

        if campo == "consciencia":
            custo = ficha.consciencia * 2
            if ficha.consciencia >= 4:
                custo = custo * 2

            ficha.consciencia = ficha.consciencia + 1

        if campo == "autocontrole":
            custo = ficha.autocontrole * 2
            if ficha.autocontrole >= 4:
                custo = custo * 2

            ficha.autocontrole = ficha.autocontrole + 1
            ficha.iniciativa = ficha.destreza + ficha.autocontrole
            ficha.forca_vontade_max = ficha.percepcao + ficha.autocontrole

        if campo == "coragem":
            custo = ficha.coragem * 2
            if ficha.coragem >= 4:
                custo = custo * 2

            ficha.coragem = ficha.coragem + 1

        if ficha.experiencia - custo >= 0:
            ficha.experiencia = ficha.experiencia - custo
            ficha.save()

        return redirect('/subir_nivel/' + str(ficha.id_personagem.id))

def aumenta_vida(request, pk):
    ficha: Ficha = get_object_or_404(Ficha, id_personagem = pk)
    value = int(request.GET.get('value'))

    ficha.vitalidade_update(value, SOMA)

    return redirect('/ficha/' + str(pk))

def diminui_vida(request, pk):
    ficha: Ficha = get_object_or_404(Ficha, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha.vitalidade_update(value, SUBTRACAO)
    return redirect('/ficha/' + str(pk))


def aumenta_sangue(request, pk):
    ficha: Ficha = get_object_or_404(Ficha, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha.sangue_update(value, SOMA)
    return redirect('/ficha/' + str(pk))


def diminui_sangue(request, pk):
    ficha: Ficha = get_object_or_404(Ficha, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha.sangue_update(value, SUBTRACAO)
    return redirect('/ficha/' + str(pk))


def aumenta_p_vontade(request, pk):
    ficha: Ficha = get_object_or_404(Ficha, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha.vontade_update(value, SOMA)
    return redirect('/ficha/' + str(pk))


def diminui_p_vontade(request, pk):
    ficha: Ficha = get_object_or_404(Ficha, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha.vontade_update(value, SUBTRACAO)
    return redirect('/ficha/' + str(pk))
