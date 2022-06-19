from cgitb import html
from urllib import request
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Film, Gatunek, Ocena
from VOD.models import *

from VOD.forms import VodForm   
# Create your views here.


def gatunek(request):
    gatunek_list = Gatunek.objects.all()
    template = loader.get_template('VOD/gatunek.html')
    context = {
        'gatunek_list': gatunek_list
    }
    return render(request, 'VOD/gatunek.html', context)

def film(request):
    film_list = Film.objects.all()
    template = loader.get_template('VOD/film.html')
    context = {
        'film_list': film_list
    }
    return render(request, 'VOD/film.html', context)

def ocena(request):
    ocena_list = Ocena.objects.all()
    template = loader.get_template('VOD/ocena.html')
    context = {
        'ocena_list': ocena_list
    }
    return render(request, 'VOD/ocena.html', context)

def VodFormView(request):
    form = VodForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'Vod/Form.html', context)