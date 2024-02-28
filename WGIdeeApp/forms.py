from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import models as authModels

class AusgabenForm(forms.ModelForm):
    class Meta:
        model = models.Ausgabe
        fields = ['Beschreibung','Preis','Person']
        
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = authModels.User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
