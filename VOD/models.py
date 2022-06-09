from django.db import models

# Create your models here.
class ocena(models.Model):
    nazwa = models.CharField(max_length=200, null=True)
    def __str__(self) -> str:
        return self.nazwa

class gatunek(models.Model):
    nazwa = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nazwa

class film(models.Model):
    ocena = models.ForeignKey(ocena, on_delete = models.CASCADE)
    nazwa = models.CharField(max_length=200)
    gatunek = models.ManyToManyField("gatunek")
   
    def __str__(self) -> str:
        return self.nazwa