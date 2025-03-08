from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

from .models import Status, Type, Category, Subcategory
from .forms import StatusForm, TypeForm, CategoryForm, SubcategoryForm


class OnlyAuthorMixin(LoginRequiredMixin, UserPassesTestMixin):

    def handle_no_permission(self):
        return redirect('cashflow:index')

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user


class TemplateEditMixin():
    template_name = 'cashflow/create_guide.html'


class StatusEditMixin(TemplateEditMixin):
    model = Status
    form_class = StatusForm


class TypeEditMixin(TemplateEditMixin):
    model = Type
    form_class = TypeForm


class CategoryEditMixin(TemplateEditMixin):
    model = Category
    form_class = CategoryForm


class SubcategoryEditMixin(TemplateEditMixin):
    model = Subcategory
    form_class = SubcategoryForm
