# Generated by Django 2.0.2 on 2019-07-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_auto_20190701_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='EgresadoConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('document', models.CharField(max_length=30, unique=True, verbose_name='Documento')),
                ('programa', models.TextField(blank=True, null=True, verbose_name='Programa')),
            ],
        ),
    ]
