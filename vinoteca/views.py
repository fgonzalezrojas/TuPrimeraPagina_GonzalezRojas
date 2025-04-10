from django.shortcuts import render

# Create your views here.

def vino(request):
    return render(request, "vinoteca/01 vino.html")

def whisky(request):
    return render(request, "vinoteca/02 whisky.html")

def champagne(request):
    return render(request, "vinoteca/03 champagne.html")

def administracion(request):
    return render(request, "vinoteca/04 administracion.html")

def proveedores(request):
    return render(request, "vinoteca/05 proveedores.html")

def productos(request):
    return render(request, "vinoteca/06 productos.html")

def clientes(request):
    return render(request, "vinoteca/07 clientes.html")

from vinoteca.forms import VinotecaProductoForm
from vinoteca.models import VinotecaProducto
from django.shortcuts import redirect

def alta_productos(request):
    if request.method == "POST":
        formulario = VinotecaProductoForm(request.POST)
        if formulario.is_valid():
            BD_Modelo = VinotecaProducto(
                bebida = formulario.cleaned_data["bebida"],
                color = formulario.cleaned_data["color"],
                variedad = formulario.cleaned_data["variedad"],
                marca = formulario.cleaned_data["marca"],
                fabricante = formulario.cleaned_data["fabricante"],
                formato = formulario.cleaned_data["formato"],
                tamaño_ml = formulario.cleaned_data["tamaño_ml"],
                EAN = formulario.cleaned_data["EAN"],
                precio = formulario.cleaned_data["precio"],
            )
            BD_Modelo.save()
            return redirect("vinoteca:alta_productos")
    else:
        formulario = VinotecaProductoForm()
        contexto = {"formulario" : VinotecaProductoForm()}
    return render(request, "vinoteca/08 alta_productos.html", context= contexto)
