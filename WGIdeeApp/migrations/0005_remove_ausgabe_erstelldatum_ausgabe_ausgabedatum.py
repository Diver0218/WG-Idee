# Generated by Django 5.0.2 on 2024-03-05 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WGIdeeApp', '0004_ausgabe_erstelldatum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ausgabe',
            name='Erstelldatum',
        ),
        migrations.AddField(
            model_name='ausgabe',
            name='Ausgabedatum',
            field=models.DateField(default=datetime.datetime(2024, 3, 5, 10, 1, 51, 931136, tzinfo=datetime.timezone.utc)),
        ),
    ]
