from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def boton1(request):
    return render(request, 'Jugar.html')

def boton2(request):
    return render(request, 'Controles.html')

def boton3(request):
    return render(request, 'Créditos.html')

def boton4(request):
    return render(request, 'Salir.html')
