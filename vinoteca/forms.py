from django.forms import ModelForm
from vinoteca.models import (
    VinotecaProducto,
    VinotecaProveedor,
    VinotecaCliente,
)

class VinotecaProductoForm(ModelForm):
    
    class Meta:
        model = VinotecaProducto
        fields = ["bebida" ,
                  "color" ,
                  "variedad" ,
                  "marca" ,
                  "etiqueta",
                  "fabricante" ,
                  "formato" ,
                  "tamaño_ml" ,
                  "EAN" ,
                  "precio",]
        
class VinotecaProductoBusquedaForm(ModelForm):
    
    class Meta:
        model = VinotecaProducto
        fields = [
                  "etiqueta",
                 ]

class VinotecaProveedorForm(ModelForm):
    
    class Meta:
        model = VinotecaProveedor
        fields = [
            "razon_social" ,
            "cuit" ,
            "provincia" ,
            "localidad" ,
            "codigo_postal" ,
            "calle" ,
            "altura" ,
            "iva" ,
            "telefono" , 
            "mail" ,]
        
class VinotecaClienteForm(ModelForm):
    
    class Meta:
        model = VinotecaCliente
        fields = [
            "nombre" ,
            "apellido" ,
            "fecha_de_nacimiento" ,
            "DNI" ,
            "mail" ,
            "provincia" ,
            "localidad" ,
            "codigo_postal" ,
            "calle" ,
            "altura" , 
            "piso" ,
            "telefono" ,]

