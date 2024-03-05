from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from . import forms
from WGIdeeApp.models import *
from WGIdeeApp.calculations import *
from django.contrib.auth import login, logout, authenticate, get_user, get_user_model
from django.contrib.auth import models as authModels
from django.contrib.auth.decorators import login_required

import WGIdeeApp

# Create your views here.
@login_required(login_url="/WGIdee/login/")
def landingPage(request):
    recent_Ausgabe = Ausgabe.objects.all().order_by('-Ausgabedatum')[:10]
    Ausgaben_list = Ausgabe.objects.all()
    Person_list = Person.objects.all().order_by('-debts')[:5]
    calculate_value_all(Person_list, Ausgaben_list)
    calculate_debts_all(Person_list, Ausgaben_list)
    template = loader.get_template("WGIdeeApp/landingPage.html")
    context = {
        'recent_Ausgabe': recent_Ausgabe,
        'Person_list': Person_list,
    }
    return HttpResponse(template.render(request=request, context=context))


@login_required(login_url="/WGIdee/login/")
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


@login_required(login_url="/WGIdee/login/")
def list(request):
    Ausgaben_list = Ausgabe.objects.all()
    Person_list = Person.objects.all()
    if (Ausgaben_list.exists() and Person_list.exists()):
        comp_list = compensation(Ausgaben_list, Person_list)
        calculate_value_all(Person_list, Ausgaben_list)
        calculate_debts_all(Person_list, Ausgaben_list)
        Summe = get_sum(Ausgaben_list)
    else:
        Summe = 0
        comp_list = []

    template = loader.get_template("WGIdeeApp/list.html")
    context = {
        'Ausgaben_list': Ausgaben_list,
        'Summe': Summe,
        'Person_list': Person_list,
        'comp_list': comp_list,
    }
    return HttpResponse(template.render(context, request))



def sign_up(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            person = Person(zugew_user=user)
            person.save()
            login(request, user)
            return redirect('landingPage')
    else:
        form = forms.RegisterForm()

    template = loader.get_template("registration/sign_up.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def persons(request):
    Ausgaben_list = Ausgabe.objects.all()
    Person_list = Person.objects.all()
    calculate_value_all(Person_list, Ausgaben_list)
    calculate_debts_all(Person_list, Ausgaben_list)

    template = loader.get_template("WGIdeeApp/persons.html")
    context = {
        'Person_list' : Person_list,
    }
    return HttpResponse(template.render(context, request))

def ausgleich(request):
    Ausgaben_list = Ausgabe.objects.all()
    Person_list = Person.objects.all()
    if (Ausgaben_list.exists() and Person_list.exists()):
        comp_list = compensation(Ausgaben_list, Person_list)
        calculate_value_all(Person_list, Ausgaben_list)
        calculate_debts_all(Person_list, Ausgaben_list)
    else:
        comp_list = []

    template = loader.get_template("WGIdeeApp/ausgleich.html")
    context = {
        'comp_list': comp_list,
    }
    return HttpResponse(template.render(context, request))