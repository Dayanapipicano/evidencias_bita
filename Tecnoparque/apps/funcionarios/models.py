from django.db import models


class Estrategia_detalle(models.Model):
    estd_formacion = models.CharField(max_length=100)
    estd_meta = models.CharField(max_length=100)
    

class Estrategia(models.Model):
    est_nombre = models.CharField(max_length=100)
    est_modalidad = models.CharField(max_length=100)
    est_total_meta = models.CharField(max_length=100)
    estrategia_detalle = models.ForeignKey(Estrategia_detalle, on_delete=models.CASCADE)


class Metas_formacion(models.Model):
    metd_modalidad =  models.CharField(max_length=100)
    metf_formacion = models.CharField(max_length=100)
    metf_meta = models.CharField(max_length=100)
    

class Metas_poblacion_vulnerable(models.Model):
    metpv_poblacion = models.CharField(max_length=100)
    metpv_tipo_poblacion = models.CharField(max_length=100)
    
    
    

class Meta(models.Model):
    met_centro_formacion = models.CharField(max_length=150)
    met_codigo = models.CharField(max_length=150)
    met_fecha_inicio = models.DateField()
    met_fecha_fin = models.DateField()
    met_año = models.CharField(max_length=4)
    met_total_otras_poblaciones = models.CharField(max_length=100)
    met_total_victimas = models.CharField(max_length=100)
    met_total_hechos_victimizantes = models.CharField(max_length=100)
    met_total_desplazados_violencia = models.CharField(max_length=100)
    met_total_titulada = models.CharField(max_length=100)
    met_total_complementaria = models.CharField(max_length=100)
    met_total_poblacion_vulnerable = models.CharField(max_length=100)
    estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    metas_formacion = models.ForeignKey(Metas_formacion, on_delete=models.CASCADE)
    metas_poblacion_vulnerable = models.ForeignKey(Metas_poblacion_vulnerable, on_delete=models.CASCADE)
    
    
    
class   Rol(models.Model):
    rol_nombre = models.CharField(max_length=100)
    rol_descripcion = models.CharField(max_length=200)


class Persona(models.Model):
    per_documento = models.AutoField(primary_key=True)
    per_tipo_documento = models.CharField(max_length=100)
    per_correo = models.EmailField(unique=True)
    per_nombres = models.CharField(max_length=60)
    per_apellidos = models.CharField(max_length=60)
    per_telefono = models.CharField(max_length=10)
    rol = models.ManyToManyField(Rol)
    
    
