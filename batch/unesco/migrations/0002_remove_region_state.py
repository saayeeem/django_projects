# Generated by Django 3.2.3 on 2021-06-01 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='state',
        ),
    ]