from django.contrib import admin

# Register your models here.

from vinoteca.models import (
    VinotecaProducto,
    VinotecaProveedor,
    VinotecaCliente,
    )

admin.site.register(VinotecaProducto)

admin.site.register(VinotecaProveedor)

admin.site.register(VinotecaCliente)
