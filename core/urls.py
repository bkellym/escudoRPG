from django.urls import path
from . import views

urlpatterns = [
    path('ficha/<int:pk>/', views.ficha, name='ficha'),
    path('aumenta_vida/<int:pk>', views.aumenta_vida, name='aumenta_vida'),
    path('diminui_vida/<int:pk>', views.diminui_vida, name='diminui_vida'),
    path('aumenta_sangue/<int:pk>', views.aumenta_sangue, name='aumenta_sangue'),
    path('diminui_sangue/<int:pk>', views.diminui_sangue, name='diminui_sangue'),
    path('aumenta_p_vontade/<int:pk>', views.aumenta_p_vontade, name='aumenta_p_vontade'),
    path('diminui_p_vontade/<int:pk>', views.diminui_p_vontade, name='diminui_p_vontade'),
]