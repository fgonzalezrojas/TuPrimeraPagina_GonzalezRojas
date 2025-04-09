from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def vinoteca(request):
    return HttpResponse("Vinoteca ON")