from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuario_responsable = models.ForeignKey(User, on_delete=models.CASCADE)
   