# Generated by Django 3.2.16 on 2025-03-06 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0003_category_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusmoney',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='typemoney',
            name='slug',
        ),
    ]
