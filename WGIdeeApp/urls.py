from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name = "landingPage"),
    path('home/', views.landingPage, name = "landingPage"),
    path('outgoings/', views.outgoings, name = "outgoings"),
    path('list/', views.list, name = "list"),
    path('sign_up/', views.sign_up, name = "sign_up")
]
