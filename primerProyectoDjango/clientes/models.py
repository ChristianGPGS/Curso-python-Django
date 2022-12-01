from django.db import models


# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    combustive = models.CharField(max_length=15)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.matricula} {self.marca} {self.color} {self.combustive} {self.cliente}"


