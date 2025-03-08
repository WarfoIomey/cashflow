from django.shortcuts import get_object_or_404

from .models import Category, Type, Subcategory, Status


def get_types(user):
    """Получение записей."""
    return Type.objects.select_related('user').filter(user=user)


def get_status(user):
    """Получение статусов."""
    return Status.objects.select_related('user').filter(user=user)


def get_categorys(pk, user):
    """Получение категорий."""
    return Category.objects.select_related('type', 'user').filter(
        type=pk,
        user=user
    )


def get_subcategorys(slug, user):
    """Получение подкатегорий."""
    category = get_object_or_404(Category, slug=slug)
    return Subcategory.objects.select_related('category', 'user').filter(
        category=category.pk,
        user=user
    )
