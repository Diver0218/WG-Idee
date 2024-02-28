from typing import Any
from django.db import models
from .calculations import get_sum
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    zugew_user = models.OneToOneField(User, on_delete=models.CASCADE)
    wert = 0   #models.FloatField(default=0.00)
    debts = models.FloatField(default=0.00)

    def __str__(self) -> str:
        return self.zugew_user.first_name + " " + self.zugew_user.last_name
    
    def calculate_value(self, Ausgabe_list):
        self.wert = 0
        for a in Ausgabe_list:
            if self == a.Person:
                self.wert += a.Preis

    def calculate_debts(self, Ausgaben_list, Person_list):
        self.calculate_value(Ausgaben_list)
        sum = get_sum(Ausgaben_list)
        Person_count = Person_list.count()
        average = sum / Person_count
        self.debts = average - self.wert
        


    
class Ausgabe(models.Model):
    Beschreibung = models.CharField(max_length=50)
    Preis = models.FloatField(default=0.00)
    #Person = models.CharField(max_length=50)
    Person = models.ForeignKey(Person, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.Beschreibung
    