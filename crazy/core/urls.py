
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.juego.urls'), name='aplicaciones'),  # Corregido el uso de include
]