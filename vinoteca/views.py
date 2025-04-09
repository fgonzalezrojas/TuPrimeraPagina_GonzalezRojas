from django.shortcuts import render

# Create your views here.

def vinos(request):
    return render(request, "vinoteca/vinos.html")
