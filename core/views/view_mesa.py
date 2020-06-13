from django.shortcuts import render, get_object_or_404, redirect
from core.models import *

def listar_mesas(request, template_name="core/listar_mesas.html"):
    mesas = Mesa.objects.all()
    return render(request, template_name, {'mesas': mesas})

def listar_personagens_mesa(request, pk, template_name="core/listar_personagens_mesas.html"):
    personagens = Personagem.objects.all().filter(mesa=pk)
    return render(request, template_name, {'personagens': personagens})