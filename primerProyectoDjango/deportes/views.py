from django.shortcuts import render


# Create your views here.

def inicio(request):
    inicio_param = {"Titulo": "Deportes", "Descripcion": "Apicacion deportes"}
    return render(request, "inicio.html", inicio_param)


def listar_equipos(request):
    brasil = {"Equipo": "Brasil", "Continente": "America", "Numero_Mundiales": 5}
    alemania = {"Equipo": "Alemania", "Continente": "Europa", "Numero_Mundiales": 4}
    espania = {"Equipo": "España", "Continente": "Europa", "Numero_Mundiales": 1}

    contexto = {"listado_equipos": [brasil, alemania, espania]}
    return render(request, "gestion/equipos.html", contexto)
