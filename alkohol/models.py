from django.db import models

# Create your models here.
class alkohol(models.Model):
    nazwa = models.CharField(max_length=40)
    moc = models.IntegerField
class moc(models.Model):
    nazwa = models.CharField(max_length=40)
    alkohol = models.ForeignKey(
        'alkohol',
        on_delete=models.CASCADE,
    )
    smak = models.ManyToManyField("emoty")
class smak(models.Model):
    nazwa = models.CharField(max_length=40)