from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.lista_equipos, name='lista_equipos'),
]