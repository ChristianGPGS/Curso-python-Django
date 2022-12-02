from deportes.models import Jugador
from django.forms import modelform_factory
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

    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]

    # Recibe los datos del boton enviar
    if request.method == 'POST':
        accion = request.POST.get('accion', '')

        if accion == "Filtrar":
            continente_filtro = request.POST['continente']
            titulo = request.POST.get('titulo', 'titulo por defecto')

            lista_selecciones = list(
                filter(lambda seleccion: seleccion["continente"] == continente_filtro, lista_selecciones))
        elif accion == "guardar":
            nombre = request.POST['equipo']
            continente = request.POST['continente']
            num_mundiales = request.POST['num_mundiales']
            nueva_seleccion = {"nombre": nombre, "continente": continente, "num_mundiales": num_mundiales}
            lista_selecciones.append(nueva_seleccion)

    elif request.method == 'GET':
        titulo = request.GET.get('titulo', 'titulo por defecto')

    contexto = {"listado_selecciones": lista_selecciones, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "listado_selecciones_mundial.html", contexto)


def aniadir_seleccion(request):
    return render(request, "aniadir_seleccion.html")


JugadorForm = modelform_factory(Jugador, exclude=[])


def jugadores(request):
    listado_posiciones = ["Portero", "Defensa", "Centrocampistas", "Delanteros"]
    listado_jugadores = []
    accion = request.POST.get('action', '')
    id_jugador_borrar = request.POST.get('id_jugador', '')

    if request.method == "POST":
        # Inicio Metodo para Añadir jugadores
        if accion == "guardar":
            jugador_form = JugadorForm(request.POST)
            jugador_form.save()
        # Final Metodo para Añadir jugadores
    jugador_form = JugadorForm()
    jugadores = Jugador.objects.all()
    for jugador in jugadores:
        id = jugador.id
        nombres = jugador.nombre
        equipo = jugador.equipo
        edad = jugador.edad
        posicion = jugador.posicion
        nacionalidad = jugador.nacionalidad
        jugador_format = {"id": id, "nombre": nombres, "equipo": equipo, "edad": edad, "posicion": posicion,
                          "nacionalidad": nacionalidad}
        listado_jugadores.append(jugador_format)
        if accion == "borrar":
            print(id_jugador_borrar)
    contexto = {"listado_posiciones": listado_posiciones, "listado_jugadores": listado_jugadores,
                "jugador_form": jugador_form}

    return render(request, "Jugadores.html", contexto)


def add_jugador(request):
    mensaje = ''
    if request.method == 'POST':
        try:
            jugador_form = JugadorForm(request.POST)
            jugador_form.save()
        except Exception as e:
            mensaje = f'Error al almacenar el jugador {e}'
        else:
            mensaje = "Jugador almacenado correctamente"

    jugador_form = JugadorForm()

    contexto = {"jugador_form": jugador_form, "mensaje": mensaje}
    return render(request, "add_jugador.html", contexto)
