# Generated by Django 2.0.2 on 2019-07-18 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0019_auto_20190718_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_user', to='Usuarios.Profile', verbose_name='Seguidor'),
        ),
    ]
