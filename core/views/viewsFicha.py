from django.shortcuts import render, get_object_or_404
from core.models import *

# Create your views here.
def ficha(request, pk):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    ficha =  Ficha.objects.get(id_personagem = personagem.pk)

    entidade['ficha'] = ficha
    entidade['porcentagem'] = ficha.calculaPorcentagens()

    disciplinas = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=1)
    if disciplinas.exists():
        entidade['disciplinas'] = disciplinas

    antecendentes = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=2)
    if antecendentes.exists():
        entidade['antecendentes'] = antecendentes

    qualidades = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=3)
    if qualidades.exists():
        entidade['qualidades'] = qualidades

    defeitos = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=4)
    if defeitos.exists:
        entidade['defeitos'] = defeitos

    inventario = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=5)
    if inventario.exists():
        entidade['inventario'] = inventario

    entidade['imagem'] = "img/token_" + str(personagem.pk) + ".png"

    return render(request, 'core/ficha.html', {'entidade': entidade})