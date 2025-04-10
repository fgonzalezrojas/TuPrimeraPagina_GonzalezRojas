from django.forms import ModelForm
from vinoteca.models import VinotecaProducto

class VinotecaProductoForm(ModelForm):
    
    class Meta:
        model = VinotecaProducto
        fields = ["bebida" ,
                  "color" ,
                  "variedad" ,
                  "marca" ,
                  "fabricante" ,
                  "formato" ,
                  "tamaño_ml" ,
                  "EAN" ,
                  "precio",]
        
