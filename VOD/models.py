from django.db import models

# Create your models here.
class Ocena(models.Model):
    nazwa = models.CharField(max_length=200, null=True)
    def __str__(self) -> str:
        return self.nazwa

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.nazwa

class Film(models.Model):
    Nazwa = models.CharField(max_length=200)
    Ocena = models.ForeignKey(Ocena, on_delete = models.CASCADE)   
    Gatunek = models.ManyToManyField("gatunek")
   
    def __str__(self) -> str:
        return self.Nazwa