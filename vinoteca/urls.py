from django.urls import path

from vinoteca.views import (
    vino ,
    whisky ,
    champagne ,
    administracion ,
    proveedores ,
    productos ,
    clientes ,
    alta_productos, 
    lista_productos,
)

app_name = "vinoteca"

urlpatterns = [
        path("vino", lista_productos , name = "vino"),
        path("whisky", whisky , name = "whisky"),
        path("champagne", champagne , name = "champagne"),
        path("administracion", administracion , name = "administracion"),
        path("proveedores", proveedores , name = "proveedores"),
        path("productos", productos , name = "productos"),
        path("clientes", clientes , name = "clientes"),
        path("alta_productos", alta_productos , name = "alta_productos"),
]
