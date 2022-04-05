from django.shortcuts import render
from django.http import HttpResponse
from datos_familiares.models import *

# Create your views here.
def index (request):
    h1 = 'Primer MVT'
    subtitulo = 'Crear una web que permite ver los datos de algunos de tus familiares, guardados en un BD.'
    dict_datos = {'h1': h1, 'subtitulo': subtitulo}
    return render(request, 'datos_familiares/index.html', dict_datos)

def familiares(self):
    familiar_1 = Familiar(id= 1, nombre= "Lorena", apellido= "Calapeña",fecha_cumpleaños= "1988-06-26")
    familiar_1.save()

    plantilla = f"ID: {familiar_1.id} | Nombre:  {familiar_1.nombre} | Apellido:  {familiar_1.apellido} | Cumpleaños:  {familiar_1.fecha_cumpleaños}"
    
    return HttpResponse(plantilla)