from django.urls import path
from . import views

urlpatterns = [
    path('ficha/<int:pk>/', views.ficha, name='ficha'),
]