from tkinter import Widget
from django.db import models
from django.forms import CharField, DateField

# Create your models here.
class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_cumpleaños= models.DateField()

class Estudios(models.Model):
    id = models.IntegerField(primary_key=True)
    carrera = models.CharField(max_length=40)
    name_establecimiento = models.CharField(max_length=40)

