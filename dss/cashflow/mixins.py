from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import redirect

from .models import Category, Record, Type, Status, Subcategory
from .forms import (
    CategoryForm,
    RecordForm,
    TypeForm,
    StatusForm,
    SubcategoryForm,
)


class OnlyAuthorMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Миксин для измениния записей только автором записей"""

    def handle_no_permission(self):
        raise Http404("Страница не найдена")

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user


class RecordEditMixin():
    """Миксин для указания формы и модели записей."""

    model = Record
    form_class = RecordForm


class StatusEditMixin():
    """Миксин для указания формы, модели и html страницы статусов."""

    model = Status
    form_class = StatusForm
    template_name: str = 'cashflow/create_guide.html'


class TypeEditMixin():
    """Миксин для указания формы, модели и html страницы типов."""

    model = Type
    form_class = TypeForm
    template_name: str = 'cashflow/create_guide.html'


class CategoryEditMixin():
    """Миксин для указания формы, модели и html страницы категорий."""

    model = Category
    form_class = CategoryForm
    template_name: str = 'cashflow/create_guide.html'


class SubcategoryEditMixin():
    """Миксин для указания формы, модели и html страницы подкатегорий."""

    model = Subcategory
    form_class = SubcategoryForm
    template_name: str = 'cashflow/create_guide.html'
