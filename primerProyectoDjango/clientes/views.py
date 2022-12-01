from clientes.models import Clientes
from django.shortcuts import render


# Create your views here.
def insertar_clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellidos = request.POST.get('apellido', '')
        dni = request.POST.get('dni', '')
        email = request.POST.get('email', '')
        cliente = Clientes(1, nombre, apellidos, dni, email)
        cliente.save()
    return render(request, "Clientes.html")
