from django.shortcuts import render, get_object_or_404
from core.models import personagem_vampiro, ficha_vampiro

# Create your views here.
def ficha(request, pk):
    personagem = get_object_or_404(personagem_vampiro, pk=pk)
    ficha = ficha_vampiro.objects.get(id_personagem = personagem.pk)
    return render(request, 'core/ficha.html', {'ficha': ficha, 'personagem': personagem})