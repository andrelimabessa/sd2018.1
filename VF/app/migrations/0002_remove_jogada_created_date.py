# Generated by Django 2.0.6 on 2018-06-25 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogada',
            name='created_date',
        ),
    ]