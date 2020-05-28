from django.urls import path
from . import views

urlpatterns = [
    path('ficha', views.ficha, name='ficha'),
]