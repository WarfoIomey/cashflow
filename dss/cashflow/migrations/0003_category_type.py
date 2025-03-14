# Generated by Django 3.2.16 on 2025-03-06 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0002_record_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(default=1, help_text='Тип денежных средств', on_delete=django.db.models.deletion.CASCADE, to='cashflow.typemoney', verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
