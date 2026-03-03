from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Aprendiz, Prestamo
from .forms import EquipoForm, AprendizForm, PrestamoForm

# LISTAR: Esta es la vista que ve tanto el Aprendiz como el Admin
def lista_equipos(request):
    equipos = Equipo.objects.all()
    # También traemos los préstamos para que el Admin los vea
    prestamos = Prestamo.objects.all()
    return render(request, 'inventario/lista_equipos.html', {
        'equipos': equipos,
        'prestamos': prestamos
    })

# CREAR: Registros
def registrar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'inventario/registrar_equipo.html', {'form': form})

def registrar_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = AprendizForm()
    return render(request, 'inventario/registrar_aprendiz.html', {'form': form})

def registrar_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            # Lógica: Al prestarlo, el equipo ya no está disponible
            prestamo.equipo.estado = 'Prestado'
            prestamo.equipo.save()
            prestamo.save()
            return redirect('lista_equipos')
    else:
        form = PrestamoForm()
    return render(request, 'inventario/registrar_prestamo.html', {'form': form})

# ELIMINAR (Punto 7 del CRUD)
def eliminar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    equipo.delete()
    return redirect('lista_equipos')