from time import timezone
from django.db import models

# Create your models here.


class Equipo(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Jugador(models.Model):
    name = models.CharField(max_length=50)
    goals = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
