from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manages import UsuarioManage

class Usuario(AbstractBaseUser):
    
    nombre =  models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    
    is_staff =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'correo'
    
    objects = UsuarioManage()