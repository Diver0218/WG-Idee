# Generated by Django 5.0.2 on 2024-02-12 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WGIdeeApp', '0004_alter_ausgabe_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='wert',
        ),
    ]