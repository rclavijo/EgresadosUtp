# Generated by Django 2.0.2 on 2019-07-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_auto_20190703_1407'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='interests',
            field=models.ManyToManyField(blank=True, to='Usuarios.Interests'),
        ),
    ]