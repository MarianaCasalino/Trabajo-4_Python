from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas_viajeros/lista_tareas.html', {'tareas': tareas})
