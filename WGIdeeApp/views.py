from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from . import forms
from WGIdeeApp.models import *
from WGIdeeApp.calculations import *

import WGIdeeApp

# Create your views here.
def landingPage(request):
    template = loader.get_template("WGIdeeApp/landingPage.html")
    return HttpResponse(template.render(request=request))

def outgoings(request):
    if request.method == 'POST':
        form = forms.AusgabenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landingPage')
    else:
        form = forms.AusgabenForm()

    template = loader.get_template("WGIdeeApp/outgoings.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def list(request):
    Ausgaben_list = Ausgabe.objects.all()
    Person_list = Person.objects.all()
    calculate_value_all(Person_list, Ausgaben_list)
    calculate_debts_all(Person_list, Ausgaben_list)
    comp_list = compensation(Ausgaben_list, Person_list)
    Summe = get_sum(Ausgaben_list)
    template = loader.get_template("WGIdeeApp/list.html")
    context = {
        'Ausgaben_list': Ausgaben_list,
        'Summe': Summe,
        'Person_list': Person_list,
        'comp_list': comp_list,
    }
    return HttpResponse(template.render(context, request))