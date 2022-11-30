from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
def bienvenido(request):
    return HttpResponse("Buenas tardes")


"""


def bienvenido(request):
    mensajes = {"mensaje1": "valor del mensaje1", "mensaje2": "valor del mensaje2"}
    return render(request, "bienvenido.html", mensajes)


def listar_datos(request):
    listado_alumnos = [
        {"nombre": "Nombre1", "apellidos": "Apellido1", "dni": "1111A"},
        {"nombre": "Nombre2", "apellidos": "Apellido2", "dni": "2222B"},
        {"nombre": "Nombre3", "apellidos": "Apellido3", "dni": "3333C"}
    ]
    contexto = {"listado_alumnos": listado_alumnos}
    return render(request, "gestion/alumno.html", contexto)


def despedida(request):
    return render(request, "despedida.html")
