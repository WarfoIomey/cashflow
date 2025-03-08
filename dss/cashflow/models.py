from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class Record(models.Model):
    """Модель записи пользователя."""

    created_at = models.DateField(
        default=timezone.now,
        help_text='Время создания записи',
        verbose_name='Дата и время создания',
        editable=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор записи',
        help_text='Автор записи',
        related_name='records',
    )
    status = models.ForeignKey(
        'Status',
        on_delete=models.SET_NULL,
        verbose_name='Статус',
        help_text='статус записи',
        null=True,
        blank=True,
    )
    type = models.ForeignKey(
        'Type',
        on_delete=models.CASCADE,
        verbose_name='Тип',
        help_text='Тип записи',
        null=True,
        blank=False,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Категория записи',
        null=True,
        blank=False
    )
    subcategory = models.ForeignKey(
        'Subcategory',
        on_delete=models.CASCADE,
        verbose_name='Подкатегория',
        help_text='Подкатегория записи',
        null=True,
        blank=False

    )
    comment = models.TextField(
        blank=False,
        help_text='Текст комментария',
        verbose_name='Комментарий'
    )
    amount = models.PositiveIntegerField(
        default=0,
        help_text='Сумма, по умолчанию 0',
        verbose_name='Сумма',
        blank=False,
    )


class Status(models.Model):
    """Модель статуса денежных средств."""

    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название статуса, максимальная длинна строки 256'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор статуса',
        help_text='Автор статуса',
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Статус денежных средств'
        verbose_name_plural = 'Статус денежных средств'

    def __str__(self):
        return self.title


class Type(models.Model):
    """Тип денежных средств."""

    title = models.CharField(
        max_length=256,
        verbose_name='Тип',
        help_text='Тип денежных средств, максимальная длинна строки 256'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор Типа',
        help_text='Автор Типа',
        related_name='type',
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Тип денежных средств'
        verbose_name_plural = 'Типы денежных средств'

    def __str__(self):
        return self.title


class Category(models.Model):
    """Модель категорий."""

    title = models.CharField(
        max_length=256,
        verbose_name='Название категории',
        help_text='Название категории, максимальная длинна строки 256'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор категории',
        help_text='Автор категории',
        related_name='category',
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name='Тип',
        help_text='Тип денежных средств',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL;'
                   ' разрешены символы латиницы, цифры, дефис'
                   ' и подчёркивание.')
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    """Модель подкатегорий."""

    title = models.CharField(
        max_length=256,
        verbose_name='Название подкатегории',
        help_text='Название подкатегории, максимальная длинна строки 256'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор подкатегории',
        help_text='Автор подкатегории',
        related_name='subcategory',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        help_text='Категория денежных средств',
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL;'
                   ' разрешены символы латиницы, цифры, дефис'
                   ' и подчёркивание.')
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title
