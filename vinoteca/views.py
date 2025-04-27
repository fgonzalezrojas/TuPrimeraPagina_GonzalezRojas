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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
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
    mensaje = None
    if request.method == "GET":
        contexto = {"formulario": VinotecaProductoBusquedaForm(), "mensaje": mensaje}
        return render(request, "vinoteca/09 busqueda_productos.html", context=contexto)
    else:
        formulario = VinotecaProductoBusquedaForm(request.POST)

        if formulario.is_valid():
            etiqueta = formulario.cleaned_data["etiqueta"]
            resultado_busqueda = VinotecaProducto.objects.filter(etiqueta__icontains=etiqueta)

            if not resultado_busqueda:
                mensaje = "No contamos con la etiqueta '{}' en nuestra selección de bebidas.".format(etiqueta)
                contexto = {"formulario": formulario, "mensaje": mensaje}
                return render(request, "vinoteca/09 busqueda_productos.html", context=contexto)
            else:
                contexto = {
                    "skus": resultado_busqueda,
                }
                return render(request, "vinoteca/10 maestro_productos.html", context=contexto)
        else:
            contexto = {"formulario": formulario}
            return render(request, "vinoteca/09 busqueda_productos.html", context=contexto)
    
from django.shortcuts import redirect

@login_required
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

@login_required
def alta_clientes(request):
    if request.method == "POST":
        formulario = VinotecaClienteForm(request.POST)
        if formulario.is_valid():
            BD_Modelo = VinotecaCliente(
                nombre = formulario.cleaned_data["nombre"],
                apellido = formulario.cleaned_data["apellido"],
                fecha_de_nacimiento = formulario.cleaned_data["fecha_de_nacimiento"],
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

# CRUD | BCV

def home(request):
    return render(request, "vinoteca/17 inicio.html")

from django.views.generic import (
    CreateView ,
    UpdateView , 
    DeleteView ,
    DetailView ,
    ListView ,
)

from django.urls import reverse_lazy

# PRODUCTO
class VinotecaProductoListView(ListView):
    model = VinotecaProducto
    template_name = "vinoteca/cbv/01 productos_lista.html"
    context_object_name = "materiales"

class VinotecaProductoCreateView(LoginRequiredMixin, CreateView):
    model = VinotecaProducto
    fields = [
        "bebida" ,
        "color" ,
        "variedad" ,
        "marca" ,
        "etiqueta",
        "fabricante" ,
        "formato" ,
        "tamaño_ml" ,
        "EAN" ,
        "precio" ,
        ]
    template_name = "vinoteca/cbv/02 productos_alta.html"
    success_url = "lista_productos"

class VinotecaProductoDetailView(LoginRequiredMixin, DetailView):
    model = VinotecaProducto
    template_name = "vinoteca/cbv/03 productos_detalle.html"

class VinotecaProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = VinotecaProducto
    fields = [
        "bebida" ,
        "color" ,
        "variedad" ,
        "marca" ,
        "etiqueta",
        "fabricante" ,
        "formato" ,
        "tamaño_ml" ,
        "EAN" ,
        "precio" ,
        ]
    template_name = "vinoteca/cbv/04 productos_editar.html"
    success_url = reverse_lazy("vinoteca:cbv/lista_productos")

    def get_success_url(self):
        return self.success_url
   
class VinotecaProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = VinotecaProducto
    template_name = "vinoteca/cbv/05 productos_borrar.html"
    success_url = reverse_lazy("vinoteca:cbv/lista_productos")

    def get_success_url(self):
        return self.success_url

# PROVEEDOR
class VinotecaProveedorListView(LoginRequiredMixin, ListView):
    model = VinotecaProveedor
    template_name = "vinoteca/cbv/06 proveedores_lista.html"
    context_object_name = "proveedores"

class VinotecaProveedorCreateView(LoginRequiredMixin, CreateView):
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
        "mail" ,
        ]
    template_name = "vinoteca/cbv/07 proveedores_alta.html"
    success_url = "lista_proveedores"

class VinotecaProveedorDetailView(LoginRequiredMixin, DetailView):
    model = VinotecaProveedor
    template_name = "vinoteca/cbv/08 proveedores_detalle.html"

class VinotecaProveedorUpdateView(LoginRequiredMixin, UpdateView):
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
        "mail" ,
        ]
    template_name = "vinoteca/cbv/09 proveedores_editar.html"
    success_url = reverse_lazy("vinoteca:cbv/lista_proveedores")

    def get_success_url(self):
        return self.success_url
class VinotecaProveedorDeleteView(LoginRequiredMixin, DeleteView):
    model = VinotecaProveedor
    template_name = "vinoteca/cbv/10 proveedores_borrar.html"
    success_url = reverse_lazy("vinoteca:cbv/lista_proveedores")

    def get_success_url(self):
        return self.success_url

# CLIENTE
class VinotecaClienteListView(LoginRequiredMixin, ListView):
    model = VinotecaCliente
    template_name = "vinoteca/cbv/11 clientes_lista.html"
    context_object_name = "clientes"

class VinotecaClienteCreateView(LoginRequiredMixin, CreateView):
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
        "telefono" ,
        ]
    template_name = "vinoteca/cbv/12 clientes_alta.html"
    success_url = "lista_clientes"

class VinotecaClienteDetailView(LoginRequiredMixin, DetailView):
    model = VinotecaCliente
    template_name = "vinoteca/cbv/13 clientes_detalle.html"

class VinotecaClienteUpdateView(LoginRequiredMixin, UpdateView):
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
        "telefono" ,
        ]
    template_name = "vinoteca/cbv/14 clientes_editar.html"
    success_url = reverse_lazy("vinoteca:cbv/lista_clientes")

    def get_success_url(self):
        return self.success_url
class VinotecaClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = VinotecaCliente
    template_name = "vinoteca/cbv/15 clientes_borrar.html"
    success_url = reverse_lazy("vinoteca:cbv/lista_clientes")

    def get_success_url(self):
        return self.success_url

def about(request):
    return render(request , "vinoteca/18 about.html")

