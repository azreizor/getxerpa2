from django.urls import path
from . import views

urlpatterns = [
    path('equipos', views.equipos),
    path('equipos/<query>', views.equipos),
    path('formulario_equipo', views.formulario_equipo),
    path('ingreso_equipo', views.ingreso_equipo),
    path('editar_equipo/<id>', views.editar_equipo),
    path('editar_equipoBD', views.editar_equipoBD),
    path('eliminar_equipo/<id>', views.eliminar_equipo),
    
    path('jugadores', views.jugadores),
    path('formulario_jugador', views.formulario_jugador),
    path('ingreso_jugador', views.ingreso_jugador),
    path('editar_jugador/<id>', views.editar_jugador),
    path('editar_jugadorBD', views.editar_jugadorBD),
    path('eliminar_jugador/<id>', views.eliminar_jugador),
]