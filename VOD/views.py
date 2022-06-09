from django.shortcuts import HttpResponse
from .models import film, gatunek, ocena
# Create your views here.


def gatunek(request):
    return HttpResponse("gatunek")

def film(request):
    return HttpResponse("film")

def ocena(request):
    return HttpResponse("ocena")    
    