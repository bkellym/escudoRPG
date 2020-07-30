from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_mesas, name='listar_mesas'),
    path('personagens/<int:pk>', views.listar_personagens_mesa, name='personagens'),
    path('usuario/cadastro', views.tela_cadastro_usuario, name='cadastro_usuario'),

    path('cthulhu/ficha/<int:pk>/', views.ficha_cthulhu, name='ficha_cthulhu'),
    path('cthulhu/desmarcar/<int:id>/', views.desmarcar, name='desmarcar'),
    path('cthulhu/check_campo/', views.check_campo_cthulhu, name='check_campo_cthulhu'),
    path('cthulhu/subir_nivel/<int:pk>/', views.ficha_cthulhu_upar, name='subir_nivel_cthulhu'),
    path('cthulhu/subir_nivel_habilidade/', views.subir_nivel_habilidade, name='subir_nivel_habilidade'),
    path('cthulhu/aumenta_sanidade/<int:pk>', views.aumenta_sanidade, name='aumenta_sanidade'),
    path('cthulhu/diminui_sanidade/<int:pk>', views.diminui_sanidade, name='diminui_sanidade'),
    path('cthulhu/aumenta_pontos_vida/<int:pk>', views.aumenta_pontos_vida, name='aumenta_pontos_vida'),
    path('cthulhu/diminui_pontos_vida/<int:pk>', views.diminui_pontos_vida, name='diminui_pontos_vida'),

    path('vampiro/ficha/<int:pk>/', views.ficha_vampiro, name='ficha'),
    path('vampiro/check_campo/', views.check_campo, name='check_campo'),
    path('vampiro/upar_virtude/', views.upar_virtude, name='upar_virtude'),
    path('vampiro/subir_nivel/<int:pk>/', views.ficha_update, name='subir_nivel'),
    path('vampiro/upar_habilidade/', views.upar_habilidade, name='upar_habilidade'),
    path('vampiro/aumenta_vida/<int:pk>', views.aumenta_vida, name='aumenta_vida'),
    path('vampiro/diminui_vida/<int:pk>', views.diminui_vida, name='diminui_vida'),
    path('vampiro/aumenta_sangue/<int:pk>', views.aumenta_sangue, name='aumenta_sangue'),
    path('vampiro/diminui_sangue/<int:pk>', views.diminui_sangue, name='diminui_sangue'),
    path('vampiro/aumenta_p_vontade/<int:pk>', views.aumenta_p_vontade, name='aumenta_p_vontade'),
    path('vampiro/diminui_p_vontade/<int:pk>', views.diminui_p_vontade, name='diminui_p_vontade'),
]
