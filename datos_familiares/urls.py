from django.urls import path
from datos_familiares.views import *

urlpatterns = [
    path('', index, name='inicio'),
    path('familiares/', familiares),

]

