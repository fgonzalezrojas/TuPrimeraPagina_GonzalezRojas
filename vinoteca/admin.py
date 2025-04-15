from django.contrib import admin

# Register your models here.

from vinoteca.models import (
    VinotecaProducto,
    VinotecaProveedor,
    )

admin.site.register(VinotecaProducto)

admin.site.register(VinotecaProveedor)
