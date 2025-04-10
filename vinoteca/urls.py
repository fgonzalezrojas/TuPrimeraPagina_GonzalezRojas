from django.urls import path

from vinoteca.views import vino , whisky , champagne

app_name = "vinoteca"

urlpatterns = [
        path("vino", vino , name = "vino"),
        path("whisky", whisky , name = "whisky"),
        path("champagne", champagne , name = "champagne"),
]
