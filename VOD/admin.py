from django.contrib import admin
from .models import gatunek, film ,ocena

# Register your models here.
admin.site.register(gatunek),
admin.site.register(film),
admin.site.register(ocena),