from http.client import ImproperConnectionState
from django.urls import URLPattern, path

from . import  views

app_name = 'alkohol'
urlpatterns = [
    path('', views.index, name='index'),
]