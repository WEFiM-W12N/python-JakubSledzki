from dataclasses import field, fields
from django import forms
from .models import *

class VodForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('Ocena','Nazwa')