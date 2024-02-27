from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models as authModels

class AusgabenForm(forms.ModelForm):
    class Meta:
        model = models.Ausgabe
        fields = ['Beschreibung','Preis','Person']
        
class RegisterForm(UserCreationForm):
    vorname = forms.CharField(required=True)
    nachname = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = authModels.User
        fields = ["username", "vorname", "nachname", "email", "password1", "password2"]
