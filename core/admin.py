from django.contrib import admin
from .models import personagem_vampiro
from .models import ficha_vampiro

# Register your models here.
admin.site.register(personagem_vampiro)
admin.site.register(ficha_vampiro)