from django.db import models

# Create your models here.
class Persona(models.Model):
    apellido_materno = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    ubigeo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno