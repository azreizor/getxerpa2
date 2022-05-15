from django.shortcuts import render, redirect
from .models import Equipo, Jugador
from django.contrib import messages
from django.db.models import Sum
# Create your views here.

def equipos(request):
    equipos = Equipo.objects.all()
    goles = []
    for equipo in equipos:
        goles = Jugador.objects.filter(equipo = equipo).aggregate(Sum('goals'))
        equipo.goles = goles["goals__sum"]
    return render(request, "equipos.html", {"equipos": equipos})

def formulario_equipo(request):
    return render(request, "formulario_equipo.html")

def ingreso_equipo(request):
    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    equipo = Equipo.objects.create(name = nombre, city = ciudad)
    return redirect("/equipos")

def editar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request, "editar_equipo.html", {"equipo": equipo})

def editar_equipoBD(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    equipo = Equipo.objects.get(id=id)
    equipo.name = nombre
    equipo.city = ciudad
    equipo.save()
    messages.success(request, "JUGADOR ACTUALIZADO CORRECTAMENTE")
    return redirect("/equipos")

def eliminar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    jugadores = Jugador.objects.filter(equipo=equipo)
    if len(jugadores)>0:
        print("existen conflictos")
        messages.error(request, "ERROR AL ELIMINAR, existen jugadores asociados a este equipo")
    else:
        messages.success(request, "EQUIPO ELIMINADO CORRECTAMENTE")
        equipo.delete()
    return redirect("/equipos")


#--------------------------------------------------------------------------------------

def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, "jugadores.html", {"jugadores": jugadores})

def formulario_jugador(request):
    equipos = Equipo.objects.all()
    return render(request, "formulario_jugador.html", {"equipos": equipos})

def ingreso_jugador(request):
    nombre = request.POST["nombre"]
    goles = request.POST["goles"]
    equipoid = request.POST["equipo"]
    equipo = Equipo.objects.get(id=equipoid)
    jugador = Jugador.objects.create(name = nombre, goals = goles, equipo = equipo)
    return redirect("/jugadores")

def editar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    equipos = Equipo.objects.all()
    return render(request, "editar_jugador.html", {"jugador": jugador, "equipos": equipos})

def editar_jugadorBD(request):
    jugadorid = request.POST["id"]
    nombre = request.POST["nombre"]
    goles = request.POST["goles"]
    equipoid = request.POST["equipo"]
    equipo = Equipo.objects.get(id=equipoid)
    jugador = Jugador.objects.get(id=jugadorid)
    jugador.name = nombre
    jugador.goals = goles
    jugador.equipo = equipo
    jugador.save()
    messages.success(request, "JUGADOR ACTUALIZADO CORRECTAMENTE")
    return redirect("/jugadores")

def eliminar_jugador(request, id):
    jugador = Jugador.objects.get(id=id)
    jugador.delete()
    messages.success(request, "JUGADOR ELIMINADO CORRECTAMENTE")
    return redirect("/jugadores")