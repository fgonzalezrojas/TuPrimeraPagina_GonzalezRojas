from django.shortcuts import render

# Create your views here.

def vino(request):
    return render(request, "vinoteca/01 vino.html")

def whisky(request):
    return render(request, "vinoteca/02 whisky.html")

def champagne(request):
    return render(request, "vinoteca/03 champagne.html")

