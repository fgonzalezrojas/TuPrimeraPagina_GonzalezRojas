from django.db import models

# Create your models here.

# PRODUCTO
class VinotecaProducto(models.Model):

    bebida_opciones = [
        ("Vino", "Vino"),
        ("Whisky" , "Whisky"),
        ("Champagne" , "Champagne"),
    ]

    bebida = models.CharField(max_length=50 , choices=bebida_opciones) #Vino
    color = models.CharField(max_length=50)  #Tinto
    variedad = models.CharField(max_length=50) #Malbec
    marca = models.CharField(max_length=50) #Terrazas de Los Andes
    etiqueta = models.CharField(max_length=50) #Reserva
    fabricante = models.CharField(max_length=13) #Moet Hennessy
    formato = models.CharField(max_length=50) #Botella
    tamaño_ml = models.CharField(max_length=50) #750
    EAN =models.IntegerField() #7790975001487
    precio = models.IntegerField() #13790

    def __str__(self):
        return f"{self.marca} {self.variedad} {self.tamaño_ml}"

# PROVEEDOR
class VinotecaProveedor(models.Model):
    
    iva_opciones = [
        ("RI", "Responsable Inscripto"),
        ("MT" , "Monotributista"),
        ("CF" , "Consumidor fina"),
    ]
    
    razon_social = models.CharField(max_length=200)
    cuit = models.IntegerField()
    provincia = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    codigo_postal = models.IntegerField()
    calle = models.CharField(max_length=100)
    altura =  models.CharField(max_length=50)
    iva = models.CharField(max_length=100 , choices=iva_opciones)
    telefono = models.IntegerField()
    mail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.razon_social} {self.cuit} {self.provincia}"

# CLIENTE    
class VinotecaCliente(models.Model):
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    mail = models.CharField(max_length=200)
    provincia = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    codigo_postal = models.IntegerField()
    calle = models.CharField(max_length=100)
    altura =  models.CharField(max_length=50)
    piso =  models.CharField(max_length=50)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.apellido} {self.nombre} {self.DNI}"
    
