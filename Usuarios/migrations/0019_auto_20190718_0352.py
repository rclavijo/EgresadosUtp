# Generated by Django 2.0.2 on 2019-07-18 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0018_auto_20190718_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_user', to=settings.AUTH_USER_MODEL, verbose_name='Seguidor'),
        ),
    ]
