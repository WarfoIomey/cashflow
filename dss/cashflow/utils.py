from django.shortcuts import get_object_or_404

from .models import Type, Category, Subcategory, Status


def get_types(user):
    """Получение постов"""
    return Type.objects.select_related('user').filter(user=user)


def get_status(user):
    return Status.objects.select_related('user').filter(user=user)


def get_categorys(pk, user):
    return Category.objects.select_related('type','user').filter(
        type=pk,
        user=user
    )


def get_subcategorys(slug, user):
    category = get_object_or_404(Category, slug=slug)
    return Subcategory.objects.select_related('category', 'user').filter(
        category=category.pk,
        user=user
    )
