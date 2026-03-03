from django.db import models

class Aprendiz(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    programa = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Prestado', 'Prestado'),
        ('Mantenimiento', 'Mantenimiento'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Disponible')

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Prestamo(models.Model):
    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='Activo')

    def __str__(self):
        return f"Préstamo: {self.equipo.nombre} a {self.aprendiz.nombre}"
