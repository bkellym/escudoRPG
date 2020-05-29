from django.shortcuts import render, get_object_or_404
from core.models import *

# Create your views here.
def ficha(request, pk):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    entidade['ficha'] = Ficha.objects.get(id_personagem = personagem.pk)
    entidade['disciplinas'] = Extra.objects.all().filter(id_personagem = personagem.pk, tipo = 1)
    entidade['qualidades'] = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=3)
    entidade['defeitos'] = Extra.objects.all().filter(id_personagem=personagem.pk, tipo=4)

    return render(request, 'core/ficha.html', {'entidade': entidade})