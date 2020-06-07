from django.urls import path
from . import views

urlpatterns = [
    path('ficha/<int:pk>/', views.ficha, name='ficha'),
    path('ficha_cthulhu/<int:pk>/', views.ficha_cthulhu, name='ficha_cthulhu'),
    path('subir_nivel/<int:pk>/', views.ficha_update, name='subir_nivel'),
    path('check_campo/', views.check_campo, name='check_campo'),
    path('check_campo_cthulhu/', views.check_campo_cthulhu, name='check_campo_cthulhu'),
    path('upar_habilidade/', views.upar_habilidade, name='upar_habilidade'),
    path('upar_virtude/', views.upar_virtude, name='upar_virtude'),
    path('aumenta_vida/<int:pk>', views.aumenta_vida, name='aumenta_vida'),
    path('diminui_vida/<int:pk>', views.diminui_vida, name='diminui_vida'),
    path('aumenta_sangue/<int:pk>', views.aumenta_sangue, name='aumenta_sangue'),
    path('diminui_sangue/<int:pk>', views.diminui_sangue, name='diminui_sangue'),
    path('aumenta_p_vontade/<int:pk>', views.aumenta_p_vontade, name='aumenta_p_vontade'),
    path('diminui_p_vontade/<int:pk>', views.diminui_p_vontade, name='diminui_p_vontade'),
    path('aumenta_pontos_vida/<int:pk>', views.aumenta_pontos_vida, name='aumenta_pontos_vida'),
    path('diminui_pontos_vida/<int:pk>', views.diminui_pontos_vida, name='diminui_pontos_vida'),
    path('aumenta_sanidade/<int:pk>', views.aumenta_sanidade, name='aumenta_sanidade'),
    path('diminui_sanidade/<int:pk>', views.diminui_sanidade, name='diminui_sanidade'),
]