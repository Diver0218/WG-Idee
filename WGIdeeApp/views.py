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

@login_required(login_url="/WGIdee/login/")
def landing_page(request):
    recent_ausgabe = Ausgabe.objects.all().order_by('-ausgabedatum')[:10]
    ausgaben_list = Ausgabe.objects.all()
    person_list = Person.objects.all().order_by('-debts')[:5]
    calculate_value_all(person_list, ausgaben_list)
    calculate_debts_all(person_list, ausgaben_list)
    template = loader.get_template("WGIdeeApp/landing_page.html")
    context = {
        'recent_ausgabe': recent_ausgabe,
        'person_list': person_list,
    }
    return HttpResponse(template.render(request=request, context=context))


@login_required(login_url="/WGIdee/login/")
def outgoings(request):
    if request.method == 'POST':
        form = forms.AusgabenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = forms.AusgabenForm()

    template = loader.get_template("WGIdeeApp/outgoings.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/WGIdee/login/")
def list(request):
    ausgaben_list = Ausgabe.objects.all()
    person_list = Person.objects.all()
    if (ausgaben_list.exists() and person_list.exists()):
        comp_list = compensation(ausgaben_list, person_list)
        calculate_value_all(person_list, ausgaben_list)
        calculate_debts_all(person_list, ausgaben_list)
        summe = get_sum(ausgaben_list)
    else:
        summe = 0
        comp_list = []

    template = loader.get_template("WGIdeeApp/list.html")
    context = {
        'ausgaben_list': ausgaben_list,
        'summe': summe,
        'person_list': person_list,
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
            return redirect('landing_page')
    else:
        form = forms.RegisterForm()

    template = loader.get_template("registration/sign_up.html")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/WGIdee/login/")
def persons(request):
    ausgaben_list = Ausgabe.objects.all()
    person_list = Person.objects.all()
    calculate_value_all(person_list, ausgaben_list)
    calculate_debts_all(person_list, ausgaben_list)

    template = loader.get_template("WGIdeeApp/persons.html")
    context = {
        'person_list' : person_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/WGIdee/login/")
def ausgleich(request):
    ausgaben_list = Ausgabe.objects.all()
    person_list = Person.objects.all()
    if (ausgaben_list.exists() and person_list.exists()):
        comp_list = compensation(ausgaben_list, person_list)
        calculate_value_all(person_list, ausgaben_list)
        calculate_debts_all(person_list, ausgaben_list)
    else:
        comp_list = []

    template = loader.get_template("WGIdeeApp/ausgleich.html")
    context = {
        'comp_list': comp_list,
    }
    return HttpResponse(template.render(context, request))