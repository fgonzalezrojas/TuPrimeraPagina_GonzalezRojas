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

from vinoteca.forms import ( 
    VinotecaProductoForm , 
    VinotecaProductoBusquedaForm ,
    VinotecaProveedorForm ,
    VinotecaClienteForm,
)

from vinoteca.models import (
    VinotecaProducto,
    VinotecaProveedor,
    VinotecaCliente,
)

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
                etiqueta = formulario.cleaned_data["etiqueta"],
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

def lista_vino(request):
    modelos = VinotecaProducto.objects.filter(bebida__icontains="vino")
    contexto = {
        "materiales": modelos
    }
    return render(request, "vinoteca/01 vino.html", context= contexto)

def lista_whisky(request):
    modelos = VinotecaProducto.objects.filter(bebida__icontains="whisky")
    contexto = {
        "materiales": modelos
    }
    return render(request, "vinoteca/02 whisky.html", context= contexto)

def lista_champagne(request):
    modelos = VinotecaProducto.objects.filter(bebida__icontains="champagne")
    contexto = {
        "materiales": modelos
    }
    return render(request, "vinoteca/03 champagne.html", context= contexto)

def busqueda_productos(request):
    if request.method == "GET":
        contexto = {"formulario" : VinotecaProductoBusquedaForm()}
        return render(request, "vinoteca/09 busqueda_productos.html", context= contexto)
    else:
        formulario = VinotecaProductoBusquedaForm(request.POST)

        if formulario.is_valid():
            etiqueta = formulario.cleaned_data["etiqueta"]
            resultado_busqueda = VinotecaProducto.objects.filter(etiqueta__icontains=etiqueta)
            
            contexto = {
                "skus" : resultado_busqueda,
                }
            return render(request, "vinoteca/10 maestro_productos.html", context= contexto)
        
        contexto = {"formulario" : VinotecaProductoBusquedaForm()}
        return render(request, "vinoteca/09 busqueda_productos.html", context=contexto)
    
from django.shortcuts import redirect

def alta_proveedores(request):
    if request.method == "POST":
        formulario = VinotecaProveedorForm(request.POST)
        if formulario.is_valid():
            BD_Modelo = VinotecaProveedor(
                razon_social = formulario.cleaned_data["razon_social"],
                cuit = formulario.cleaned_data["cuit"],
                provincia = formulario.cleaned_data["provincia"],
                localidad = formulario.cleaned_data["localidad"],
                codigo_postal = formulario.cleaned_data["codigo_postal"],
                calle = formulario.cleaned_data["calle"],
                altura = formulario.cleaned_data["altura"],
                iva = formulario.cleaned_data["iva"],
                telefono = formulario.cleaned_data["telefono"],
                mail = formulario.cleaned_data["mail"],
            )
            BD_Modelo.save()
            return redirect("vinoteca:alta_proveedores")
    else:
        formulario = VinotecaProveedorForm()
        contexto = {"formulario" : VinotecaProveedorForm()}
    return render(request, "vinoteca/11 alta_proveedores.html", context= contexto)

def alta_clientes(request):
    if request.method == "POST":
        formulario = VinotecaClienteForm(request.POST)
        if formulario.is_valid():
            BD_Modelo = VinotecaCliente(
                nombre = formulario.cleaned_data["nombre"],
                apellido = formulario.cleaned_data["apellido"],
                DNI = formulario.cleaned_data["DNI"],
                mail = formulario.cleaned_data["mail"],
                provincia = formulario.cleaned_data["provincia"],
                localidad = formulario.cleaned_data["localidad"],
                codigo_postal = formulario.cleaned_data["codigo_postal"],
                calle = formulario.cleaned_data["calle"],
                altura = formulario.cleaned_data["altura"],
                piso = formulario.cleaned_data["piso"],
                telefono = formulario.cleaned_data["telefono"],
            )
            BD_Modelo.save()
            return redirect("vinoteca:alta_clientes")
    else:
        formulario = VinotecaClienteForm()
        contexto = {"formulario" : VinotecaClienteForm()}
    return render(request, "vinoteca/14 alta_clientes.html", context= contexto)

