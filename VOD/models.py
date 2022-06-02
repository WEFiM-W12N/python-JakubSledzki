from django.db import models

# Create your models here.
class film(models.Model):
    nazwa = models.CharField(max_length=40)
    gatunek = models.IntegerField
class gatunek(models.Model):
    nazwa = models.CharField(max_length=40)
    film = models.ForeignKey(
        'film',
        on_delete=models.CASCADE,
    )
    ocena = models.ManyToManyField("emoty")
class ocena(models.Model):
    nazwa = models.CharField(max_length=40)