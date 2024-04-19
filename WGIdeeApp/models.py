import datetime
from email.policy import default
from time import timezone
from typing import Any
from django.db import models
from .calculations import get_sum
from django.contrib.auth.models import User
from django.utils import timezone

class Person(models.Model):
    zugew_user = models.OneToOneField(User, on_delete=models.CASCADE)
    wert = 0
    debts = models.FloatField(default=0.00)

    def __str__(self) -> str:
        return self.zugew_user.first_name + " " + self.zugew_user.last_name
    
    def calculate_value(self, ausgaben_list):
        self.wert = 0
        for a in ausgaben_list:
            if self == a.person:
                self.wert += a.preis

    def calculate_debts(self, ausgaben_list, person_list):
        self.calculate_value(ausgaben_list)
        sum = get_sum(ausgaben_list)
        person_count = person_list.count()
        average = sum / person_count
        self.debts = average - self.wert
        


    
class Ausgabe(models.Model):
    beschreibung = models.CharField(max_length=50)
    preis = models.FloatField(default=0.00)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    ausgabedatum = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.beschreibung
    