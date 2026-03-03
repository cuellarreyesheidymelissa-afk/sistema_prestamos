from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipos, name='lista_equipos'), # Página principal
    path('registrar-equipo/', views.registrar_equipo, name='registrar_equipo'),
    path('registrar-aprendiz/', views.registrar_aprendiz, name='registrar_aprendiz'),
    path('registrar-prestamo/', views.registrar_prestamo, name='registrar_prestamo'),
    path('eliminar-equipo/<int:pk>/', views.eliminar_equipo, name='eliminar_equipo'),
]