from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Base(models.Model):
    creacion = models.DateField(auto_now=True)
    actualizacion = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    
class TipoDocumento(Base):
    nombre = models.CharField(max_length=50)
    
class Cargo(Base):
    nombre = models.CharField(max_length=50)
    
class Dependencia(Base):
    nombre = models.CharField(max_length=50)
    
class Rol(Base):
    nombre = models.CharField(max_length=50)
    
class Implementos(Base):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    referencia_serie = models.CharField(max_length=50)
    
    
class Espacio(Base):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    aforo_del_espacio = models.CharField(max_length=100)
    id_implementos = models.ForeignKey(Implementos,on_delete=models.CASCADE)
    
    
class Persona(AbstractBaseUser):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id_tipo_documento = models.OneToOneField(TipoDocumento,on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    id_dependencia = models.ForeignKey(Dependencia,on_delete=models.CASCADE)
    id_rol = models.OneToOneField(Rol,on_delete=models.CASCADE,)


class Reservas(Base):
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    id_espacio = models.ForeignKey(Espacio,on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

