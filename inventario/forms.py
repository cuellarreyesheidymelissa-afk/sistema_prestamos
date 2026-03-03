from django import forms
from .models import Aprendiz, Equipo, Prestamo

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['documento', 'nombre', 'programa']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'tipo', 'estado']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['aprendiz', 'equipo']

