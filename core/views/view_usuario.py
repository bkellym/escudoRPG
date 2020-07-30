from math import floor

from django.shortcuts import render, get_object_or_404
from core.models import *

def tela_cadastro_usuario(request, template_name="core/cadastro_usuario.html"):
    return render(request, template_name)

#def cadastrar_usuario(request):
#    if request.method == "POST":
