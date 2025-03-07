from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import TypeMoney, Category, SubCategory, StatusMoney


def get_types():
    """Получение постов"""
    return TypeMoney.objects.all()


def get_status():
    return StatusMoney.objects.all()


def get_categorys(pk):
    return Category.objects.select_related('type').filter(type=pk)


def get_subcategorys(slug):
    category = get_object_or_404(Category, slug=slug)
    return SubCategory.objects.select_related('category').filter(
        category=category.pk
    )