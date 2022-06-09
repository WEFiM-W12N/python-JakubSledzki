from django.urls import URLPattern, path
from  .import  views
from django.contrib import admin

app_name = 'VOD'
urlpatterns = [
    path('gatunek/', views.gatunek, name = "gatunek"),
    path('film/',views.film, name = "film"),
    path('ocena/',views.ocena, name = "ocena"),
]