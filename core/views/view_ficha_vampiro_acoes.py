from django.shortcuts import get_object_or_404, redirect
from core.models import *

SOMA: str = '+'
SUBTRACAO: str = '-'


def check_campo(request):
    if request.method == "POST":
        id = request.POST['id']
        habilidade = Habilidade.objects.get(id=id)

        if habilidade.checked:
            habilidade.checked = False
        else:
            habilidade.checked = True
        habilidade.save()

        return redirect('/vampiro/ficha/' + str(habilidade.ficha.id_personagem.id))


def upar_habilidade(request):
    if request.method == "POST":
        id = request.POST['id']
        habilidade = Habilidade.objects.get(id=id)
        ficha = Ficha_Vampiro.objects.get(id=habilidade.ficha.id)

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

        return redirect('/vampiro/subir_nivel/' + str(habilidade.ficha.id_personagem.id))


def upar_virtude(request):
    if request.method == "POST":
        id = int(request.POST['id'])
        campo = request.POST['campo']
        ficha_vampiro = get_object_or_404(Ficha_Vampiro, id=id)

        if campo == "consciencia":
            custo = ficha_vampiro.consciencia * 2
            if ficha_vampiro.consciencia >= 4:
                custo = custo * 2

            ficha_vampiro.consciencia = ficha_vampiro.consciencia + 1

        if campo == "autocontrole":
            custo = ficha_vampiro.autocontrole * 2
            if ficha_vampiro.autocontrole >= 4:
                custo = custo * 2

            ficha_vampiro.autocontrole = ficha_vampiro.autocontrole + 1
            ficha_vampiro.iniciativa = ficha_vampiro.destreza + ficha_vampiro.autocontrole
            ficha_vampiro.forca_vontade_max = ficha_vampiro.percepcao + ficha_vampiro.autocontrole

        if campo == "coragem":
            custo = ficha_vampiro.coragem * 2
            if ficha_vampiro.coragem >= 4:
                custo = custo * 2

            ficha_vampiro.coragem = ficha_vampiro.coragem + 1

        if 0 <= ficha_vampiro.experiencia - custo:
            ficha_vampiro.experiencia = ficha_vampiro.experiencia - custo
            ficha_vampiro.save()

        return redirect('/vampiro/subir_nivel/' + str(ficha_vampiro.id_personagem.id))


def aumenta_vida(request, pk):
    ficha_vampiro: Ficha_Vampiro = get_object_or_404(Ficha_Vampiro, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_vampiro.vitalidade_update(value, SOMA)

    return redirect('/vampiro/ficha/' + str(pk))


def diminui_vida(request, pk):
    ficha_vampiro: Ficha_Vampiro = get_object_or_404(Ficha_Vampiro, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_vampiro.vitalidade_update(value, SUBTRACAO)
    return redirect('/vampiro/ficha/' + str(pk))


def aumenta_sangue(request, pk):
    ficha_vampiro: Ficha_Vampiro = get_object_or_404(Ficha_Vampiro, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_vampiro.sangue_update(value, SOMA)
    return redirect('/vampiro/ficha/' + str(pk))


def diminui_sangue(request, pk):
    ficha_vampiro: Ficha_Vampiro = get_object_or_404(Ficha_Vampiro, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_vampiro.sangue_update(value, SUBTRACAO)
    return redirect('/vampiro/ficha/' + str(pk))


def aumenta_p_vontade(request, pk):
    ficha_vampiro: Ficha_Vampiro = get_object_or_404(Ficha_Vampiro, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_vampiro.vontade_update(value, SOMA)
    return redirect('/vampiro/ficha/' + str(pk))


def diminui_p_vontade(request, pk):
    ficha_vampiro: Ficha_Vampiro = get_object_or_404(Ficha_Vampiro, id_personagem=pk)
    value = int(request.GET.get('value'))

    ficha_vampiro.vontade_update(value, SUBTRACAO)
    return redirect('/vampiro/ficha/' + str(pk))
