from django.urls import path

from vinoteca.views import (
    vino ,
    whisky ,
    champagne ,
    administracion ,
    proveedores ,
    productos ,
    clientes ,
    alta_productos , 
    lista_vino ,
    lista_whisky ,
    lista_champagne ,
    busqueda_productos ,
    alta_proveedores ,
    alta_clientes ,
    )

app_name = "vinoteca"

urlpatterns = [
        path("vino", lista_vino , name = "vino"),
        path("whisky", lista_whisky , name = "whisky"),
        path("champagne", lista_champagne , name = "champagne"),
        path("administracion", administracion , name = "administracion"),
        path("proveedores", proveedores , name = "proveedores"),
        path("productos", productos , name = "productos"),
        path("clientes", clientes , name = "clientes"),
        path("alta_productos", alta_productos , name = "alta_productos"),
        path("busqueda_productos", busqueda_productos , name = "busqueda_productos"),
        path("alta_proveedores", alta_proveedores , name = "alta_proveedores"),
        path("alta_clientes", alta_clientes , name = "alta_clientes"),
        ]

