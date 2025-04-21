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
    # CRUD | CBV
    home ,
    # PRODUCTO
    VinotecaProductoListView ,
    VinotecaProductoCreateView ,
    VinotecaProductoDetailView ,
    VinotecaProductoUpdateView ,
    VinotecaProductoDeleteView ,
    # PROVEEDOR
    VinotecaProveedorListView ,
    VinotecaProveedorCreateView ,
    VinotecaProveedorDetailView ,
    VinotecaProveedorUpdateView ,
    VinotecaProveedorDeleteView ,
    # PROVEEDOR
    VinotecaClienteListView ,
    VinotecaClienteCreateView ,
    VinotecaClienteDetailView ,
    VinotecaClienteUpdateView ,
    VinotecaClienteDeleteView ,
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
        # CRUD | CBV
        path("home", home , name = "home"),
        # PRODCUTO
        path("cbv/lista_productos", VinotecaProductoListView.as_view(), name = "cbv/lista_productos"),
        path("cbv/alta_productos", VinotecaProductoCreateView.as_view(), name = "cbv/alta_productos"),
        path("cbv/detalle_productos/<int:pk>", VinotecaProductoDetailView.as_view(), name ="cbv/detalle_productos"),
        path("cbv/editar_productos/<int:pk>", VinotecaProductoUpdateView.as_view(), name ="cbv/editar_productos"),
        path("cbv/eliminar_productos/<int:pk>", VinotecaProductoDeleteView.as_view(), name ="cbv/eliminar_productos"),
        # PROVEEDOR
        path("cbv/lista_proveedores", VinotecaProveedorListView.as_view(), name = "cbv/lista_proveedores"),
        path("cbv/alta_proveedores", VinotecaProveedorCreateView.as_view(), name = "cbv/alta_proveedores"),
        path("cbv/detalle_proveedores/<int:pk>", VinotecaProveedorDetailView.as_view(), name ="cbv/detalle_proveedores"),
        path("cbv/editar_proveedores/<int:pk>", VinotecaProveedorUpdateView.as_view(), name ="cbv/editar_proveedores"),
        path("cbv/eliminar_proveedores/<int:pk>", VinotecaProveedorDeleteView.as_view(), name ="cbv/eliminar_proveedores"),
        # CLIENTE
        path("cbv/lista_clientes", VinotecaClienteListView.as_view(), name = "cbv/lista_clientes"),
        path("cbv/alta_clientes", VinotecaClienteCreateView.as_view(), name = "cbv/alta_clientes"),
        path("cbv/detalle_clientes/<int:pk>", VinotecaClienteDetailView.as_view(), name ="cbv/detalle_clientes"),
        path("cbv/editar_clientes/<int:pk>", VinotecaClienteUpdateView.as_view(), name ="cbv/editar_clientes"),
        path("cbv/eliminar_clientes/<int:pk>", VinotecaClienteDeleteView.as_view(), name ="cbv/eliminar_clientes"),
        ]

