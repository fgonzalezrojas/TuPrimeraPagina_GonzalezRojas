from django.urls import path

from vinoteca.views import vinoteca

urlpatterns = [
        path("vinoteca", vinoteca),
]