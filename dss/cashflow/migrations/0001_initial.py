# Generated by Django 3.2.16 on 2025-03-06 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название категории, максимальная длинна строки 256', max_length=256, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='StatusMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название статуса, максимальная длинна строки 256', max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Статус денежных средств',
                'verbose_name_plural': 'Статус денежных средств',
            },
        ),
        migrations.CreateModel(
            name='TypeMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Тип денежных средств, максимальная длинна строки 256', max_length=256, verbose_name='Тип')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Тип денежных средств',
                'verbose_name_plural': 'Типы денежных средств',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название подкатегории, максимальная длинна строки 256', max_length=256, verbose_name='Название подкатегории')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
                ('category', models.ForeignKey(help_text='Категория денежных средств', on_delete=django.db.models.deletion.CASCADE, to='cashflow.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Время создания записи', verbose_name='Добавлено')),
                ('comment', models.TextField(help_text='Текст комментария', verbose_name='Комментарий')),
                ('amount', models.PositiveIntegerField(default=0, help_text='Сумма, по умолчанию 0', verbose_name='Сумма')),
                ('category', models.ForeignKey(help_text='Категория записи', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashflow.category', verbose_name='Категория')),
                ('status', models.ForeignKey(help_text='статус записи', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashflow.statusmoney', verbose_name='Статус')),
                ('type', models.ForeignKey(help_text='Тип записи', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cashflow.typemoney', verbose_name='Тип')),
            ],
        ),
    ]
