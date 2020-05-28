from django.shortcuts import render
from core.models import ficha_vampiro

# Create your views here.
def ficha(request):
    ficha = ficha_vampiro.objects.all()
    return render(request, 'core/ficha.html', {'ficha': ficha})