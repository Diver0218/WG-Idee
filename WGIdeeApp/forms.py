from django import forms
from . import models

class AusgabenForm(forms.ModelForm):
    class Meta:
        model = models.Ausgabe
        fields = ['description','value','person']
        