# Generated by Django 3.0.5 on 2020-04-18 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='templatequestion',
            name='default_value',
        ),
    ]
