# Generated by Django 3.2.16 on 2025-03-07 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0007_auto_20250306_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='category',
            field=models.ForeignKey(help_text='Категория записи', null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.ForeignKey(help_text='статус записи', null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.statusmoney', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.ForeignKey(help_text='Тип записи', null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.typemoney', verbose_name='Тип'),
        ),
    ]
