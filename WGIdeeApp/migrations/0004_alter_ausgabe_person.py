# Generated by Django 5.0.2 on 2024-02-12 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WGIdeeApp', '0003_alter_ausgabe_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ausgabe',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WGIdeeApp.person'),
        ),
    ]
