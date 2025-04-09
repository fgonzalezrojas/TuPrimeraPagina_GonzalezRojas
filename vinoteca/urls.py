from django.urls import path

from vinoteca.views import vinos

urlpatterns = [
        path("vinos", vinos),
]
