from django.db import models
from django.db.models.deletion import SET_DEFAULT

# Create your models here.

#modelo para servicio
class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True, verbose_name='Id de servicio')
    nombreServicio = models.CharField(max_length=50, verbose_name='nombre del servicio')

    def __str__(self):
        return self.nombreServicio        
    

#modelo para proveedor

class Proveedor(models.Model):
    rut = models.CharField(max_length=40, primary_key=True, verbose_name='rut')
    razon_social = models.CharField(max_length=50,verbose_name='razon_social')
    descripcion = models.CharField(max_length=200, null=True, blank=True, verbose_name='descripcion')
    Servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.razon_social        