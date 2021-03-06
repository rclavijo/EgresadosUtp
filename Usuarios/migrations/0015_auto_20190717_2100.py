# Generated by Django 2.0.2 on 2019-07-18 02:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0014_auto_20190717_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='datebirth',
        ),
        migrations.AddField(
            model_name='egresado',
            name='country',
            field=models.TextField(blank=True, null=True, verbose_name='Pais'),
        ),
        migrations.AddField(
            model_name='egresado',
            name='datebirth',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha De Nacimiento'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(7)], verbose_name='Ciudad'),
        ),
    ]
