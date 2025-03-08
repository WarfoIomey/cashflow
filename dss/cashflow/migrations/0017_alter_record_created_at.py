# Generated by Django 3.2.16 on 2025-03-08 11:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0016_alter_record_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, help_text='Время создания записи', verbose_name='Дата и время создания'),
        ),
    ]
