# Generated by Django 2.0.2 on 2019-07-05 22:32

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
