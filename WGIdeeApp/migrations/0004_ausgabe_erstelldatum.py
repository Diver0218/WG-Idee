# Generated by Django 5.0.2 on 2024-03-05 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WGIdeeApp', '0003_alter_ausgabe_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='ausgabe',
            name='Erstelldatum',
            field=models.DateField(default=datetime.datetime(2024, 3, 5, 9, 56, 25, 713963, tzinfo=datetime.timezone.utc)),
        ),
    ]
