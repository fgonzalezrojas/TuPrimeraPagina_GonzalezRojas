from django.shortcuts import render

# Create your views here.

def vino(request):
    return render(request, "vinoteca/vino.html")

def whisky(request):
    return render(request, "vinoteca/whisky.html")

def champagne(request):
    return render(request, "vinoteca/champagne.html")

