from django.db import models

# Create your models here.

class VinotecaProducto(models.Model):
    bebida = models.CharField(max_length=50) #Vino
    color = models.CharField(max_length=50)  #Tinto
    variedad = models.CharField(max_length=50) #Malbec
    marca = models.CharField(max_length=50) #Terrazas de Los Andes
    fabricante = models.CharField(max_length=13) #Moet Hennessy
    formato = models.CharField(max_length=50) #Botella
    tamaño_ml = models.CharField(max_length=50) #750
    EAN =models.IntegerField() #7790975001487
    precio = models.IntegerField() #13790

    def __str__(self):
        return f"{self.marca} {self.variedad} {self.tamaño_ml}"
    
