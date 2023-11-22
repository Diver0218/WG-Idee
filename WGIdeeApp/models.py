from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    wert = models.FloatField(default=0.00)

class Student(Person):
    matrikelnr = models.IntegerField()
    
class Ausgabe(models.Model):
    description = models.CharField(max_length=50)
    value = models.FloatField(default=0.00)
    person = models.CharField(max_length=30)

    