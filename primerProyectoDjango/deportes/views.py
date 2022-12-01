from django.shortcuts import render


# Create your views here.
def deportes(request):
    contenido = {"titulo_pagina": "Actualidad deportiva",
                 "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
    return render(request, "deportes.html", contenido)


def listar_selecciones(request):
    continente_filtro = None
    titulo = ""
    nueva_seleccion = {}

    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]

    # Recibe los datos del boton enviar
    if request.method == 'POST':
        continente_filtro = request.POST['continente']
        titulo = request.POST.get('titulo', 'titulo por defecto')
        nombre = request.POST['equipo']
        continente = request.POST['continente']
        num_mundiales = request.POST['num_mundiales']
        nueva_seleccion = {"nombre": nombre, "continente": continente, "num_mundiales": num_mundiales}
        lista_selecciones.append(nueva_seleccion)
    elif request.method == 'GET':
        titulo = request.GET.get('titulo', 'titulo por defecto')

    if continente_filtro is not None:
        lista_selecciones = list(
            filter(lambda seleccion: seleccion["continente"] == continente_filtro, lista_selecciones))

    contexto = {"listado_selecciones": lista_selecciones, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "listado_selecciones_mundial.html", contexto)


def aniadir_seleccion(request):
    return render(request, "aniadir_seleccion.html")
