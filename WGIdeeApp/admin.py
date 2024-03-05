from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

admin.site.register(Ausgabe)
admin.site.register(Person)

class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = "Personen"

class UserAdmin(BaseUserAdmin):
    inlines = [PersonInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)