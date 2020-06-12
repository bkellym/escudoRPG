from django.shortcuts import render, get_object_or_404, redirect
from core.models import *

def listar_mesas(request, template_name="core/listar_mesas.html"):
    mesas = Mesa.objects.all()

    return render(request, template_name, {'mesas': mesas})