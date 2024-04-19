from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name = "landing_page"),
    path('home/', views.landing_page, name = "landing_page"),
    path('outgoings/', views.outgoings, name = "outgoings"),
    path('list/', views.list, name = "list"),
    path('sign_up/', views.sign_up, name = "sign_up"),
    path('persons/', views.persons, name = "persons"),
    path('ausgleich/', views.ausgleich, name = "ausgleich"),
]
