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
