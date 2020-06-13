from django.shortcuts import render, get_object_or_404, redirect
from core.models import *


def ficha(request, pk, template_name="core/ficha.html"):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    ficha = Ficha.objects.get(id_personagem=personagem.pk)

    entidade['ficha'] = ficha
    entidade['porcentagem'] = ficha.calculaPorcentagens()

    habilidades = Habilidade.objects.all().filter(ficha=ficha.id)
    if habilidades.exists():
        entidade['habilidades'] = habilidades

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

    descricoes = []
    descricoes_temp = Descricao.objects.all().filter()
    for disciplina in disciplinas:
        for descricao in descricoes_temp:
            if int(descricao.nivel) <= int(disciplina.valor) and int(descricao.tipo == disciplina.tipo)\
                    and disciplina.titulo.lower() == descricao.titulo.lower():
                descricoes.append(descricao)

    for qualidade in qualidades:
        for descricao in descricoes_temp:
            if int(descricao.tipo == qualidade.tipo) and qualidade.titulo.lower() == descricao.titulo.lower():
                descricoes.append(descricao)

    for defeito in defeitos:
        for descricao in descricoes_temp:
            if int(descricao.tipo == defeito.tipo) and defeito.titulo.lower() == descricao.titulo.lower():
                descricoes.append(descricao)

    entidade['descricoes'] = descricoes

    entidade['imagem'] = "img/token_" + str(personagem.pk) + ".png"

    return render(request, template_name, {'entidade': entidade})


def ficha_update(request, pk, template_name="core/ficha_atualizacao.html"):
    entidade = {}
    personagem = get_object_or_404(Personagem, pk=pk)

    entidade['personagem'] = personagem
    ficha = Ficha.objects.get(id_personagem=personagem.pk)

    entidade['ficha'] = ficha
    entidade['porcentagem'] = ficha.calculaPorcentagens()
    entidade['custo'] = ficha.calculaCustos()

    habilidades = Habilidade.objects.all().filter(ficha=ficha.id)
    if habilidades.exists():
        entidade['habilidades'] = habilidades

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

    return render(request, template_name, {'entidade': entidade})