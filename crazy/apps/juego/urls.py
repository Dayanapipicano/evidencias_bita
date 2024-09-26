from django.urls import path
from . import views

app_name='aplicaciones'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Jugar/', views.boton1, name='Jugar'),
    path('Controles/', views.boton2, name='Controles'),
    path('Créditos/', views.boton3, name='Créditos'),
    path('Salir/', views.boton4, name='Salir'),
]


