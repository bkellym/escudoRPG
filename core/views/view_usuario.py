from math import floor
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from core.models import *

def cadastrar_usuario(request, template_name="core/cadastro_usuario.html"):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        teste_usuario = User.objects.all().filter(username=username)
        if teste_usuario.exists():
            messages.error(request, 'Nome de usuário já está sendo utilizado')
            return redirect('/usuario/cadastro')

        teste_usuario = User.objects.all().filter(email=email)
        if teste_usuario.exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('/usuario/cadastro')

        if password != confirm_password:
            messages.error(request, 'Senhas não correspondem, tente novamente')
            return redirect('/usuario/cadastro')

        User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        email=email, password=password)

        return redirect('/')
    else:
        return render(request, template_name)


def login_usuario(request, template_name="core/login.html"):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    else:
        return render(request, template_name)


def esqueceu_senha(request, template_name="core/esqueceu_senha.html"):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['confirm_email']
    else:
        return render(request, template_name)