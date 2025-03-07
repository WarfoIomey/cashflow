from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy

from .models import Record, TypeMoney, Category, SubCategory, StatusMoney
from .forms import (
    RecordForm,
    TypeForm,
    CategoryForm,
    SubcategoryForm,
    StatusForm,
)
from .utils import get_types, get_categorys, get_subcategorys, get_status


RECORD_PER_PAGE = 10

User = get_user_model()


class RecordListView(LoginRequiredMixin, ListView):
    """Получение всех записей"""

    model = Record
    template_name = 'cashflow/index.html'
    paginate_by = RECORD_PER_PAGE


class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    template_name = 'cashflow/create.html'
    form_class = RecordForm


class StatusListView(LoginRequiredMixin, ListView):
    model = StatusMoney
    template_name = 'cashflow/list.html'
    paginate_by = RECORD_PER_PAGE

    def get_queryset(self):
        return get_status()


class StatusDetailView(LoginRequiredMixin, DetailView):
    model = StatusMoney
    template_name = 'cashflow/detail.html'
    pk_url_kwarg = 'status_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = get_object_or_404(
            StatusMoney,
            id=self.kwargs['status_id']
        )
        return context


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = StatusMoney
    template_name = 'cashflow/create_guide.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('cashflow:status')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = StatusMoney
    template_name = 'cashflow/create_guide.html'
    pk_url_kwarg = 'status_id'
    form_class = StatusForm

    def get_success_url(self):
        return reverse(
            'cashflow:status_detail',
            kwargs={'status_id': self.kwargs['status_id']}
        )


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = StatusMoney
    template_name = 'cashflow/create_guide.html'
    pk_url_kwarg = 'status_id'
    form_class = StatusForm
    success_url = reverse_lazy('cashflow:status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = get_object_or_404(StatusMoney, pk=self.kwargs['status_id'])
        context['form'] = StatusForm(instance=status)
        return context


class TypeListView(LoginRequiredMixin, ListView):
    model = TypeMoney
    template_name = 'cashflow/list.html'
    paginate_by = RECORD_PER_PAGE

    def get_queryset(self):
        return get_types()


class TypeCreateView(LoginRequiredMixin, CreateView):
    model = TypeMoney
    template_name = 'cashflow/create_guide.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('cashflow:type')


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TypeMoney
    template_name = 'cashflow/create_guide.html'
    pk_url_kwarg = 'type_id'
    form_class = TypeForm

    def get_success_url(self):
        return reverse(
            'cashflow:type_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
            }
        )


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TypeMoney
    template_name = 'cashflow/create_guide.html'
    pk_url_kwarg = 'type_id'
    form_class = TypeForm
    success_url = reverse_lazy('cashflow:type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = get_object_or_404(TypeMoney, pk=self.kwargs['type_id'])
        context['form'] = TypeForm(instance=type)
        return context


class TypeDetailCategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'cashflow/detail.html'
    paginate_by = RECORD_PER_PAGE
    pk_url_kwarg = 'type_id'

    def get_queryset(self):
        return get_categorys(self.kwargs['type_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = get_object_or_404(
            TypeMoney,
            id=self.kwargs['type_id']
        )
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    type_card = None
    model = Category
    template_name = 'cashflow/create_guide.html'
    form_class = CategoryForm

    def dispatch(self, request, *args, **kwargs):
        self.type_card = get_object_or_404(TypeMoney, pk=kwargs['type_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.type = self.type_card
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'cashflow:type_detail',
            kwargs={'type_id': self.type_card.id}
        )


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'cashflow/create_guide.html'
    slug_url_kwarg = 'category_slug'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse(
            'cashflow:category_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
                'category_slug': self.kwargs['category_slug'],
            }
        )


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'cashflow/create_guide.html'
    slug_url_kwarg = 'category_slug'
    form_class = CategoryForm
    # success_url = reverse_lazy('cashflow:type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )
        context['form'] = TypeForm(instance=category)
        return context

    def get_success_url(self):
        return reverse(
            'cashflow:type_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
            }
        )


class CategoryDetailSubcategoryListView(ListView):
    model = SubCategory
    paginate_by = RECORD_PER_PAGE
    slug_url_kwarg = 'category_slug'
    template_name = 'cashflow/detail.html'

    def get_queryset(self):
        return get_subcategorys(self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )
        context['type_id'] = self.kwargs['type_id']
        return context


class SubcategoryDetailListView(DetailView):
    model = SubCategory
    slug_url_kwarg = 'sub_slug'
    template_name = 'cashflow/detail.html'

    def get_queryset(self):
        return get_subcategorys(self.kwargs['category_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_id'] = self.kwargs['type_id']
        context['category_slug'] = self.kwargs['category_slug']
        return context


class SubcategoryCreateView(LoginRequiredMixin, CreateView):
    category_card = None
    model = SubCategory
    template_name = 'cashflow/create_guide.html'
    form_class = SubcategoryForm

    def dispatch(self, request, *args, **kwargs):
        self.category_card = get_object_or_404(
            Category,
            slug=kwargs['category_slug']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.category = self.category_card
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'cashflow:category_detail',
            kwargs={
                'type_id': self.category_card.type.id,
                'category_slug': self.category_card.slug
            }
        )


class SubcategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = SubCategory
    template_name = 'cashflow/create_guide.html'
    slug_url_kwarg = 'sub_slug'
    form_class = SubcategoryForm

    def get_success_url(self):
        return reverse(
            'cashflow:subcategory_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
                'category_slug': self.kwargs['category_slug'],
                'sub_slug': self.kwargs['sub_slug']
            }
        )


class SubcategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = SubCategory
    template_name = 'cashflow/create_guide.html'
    slug_url_kwarg = 'sub_slug'
    form_class = SubcategoryForm 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = get_object_or_404(
            SubCategory,
            slug=self.kwargs['sub_slug']
        )
        context['form'] = StatusForm(instance=subcategory)
        return context

    def get_success_url(self):
        return reverse(
            'cashflow:category_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
                'category_slug': self.kwargs['category_slug']
            }
        )


class ProfileDetailView(ListView):
    """Обзор профиля"""

    model = Record
    paginate_by = RECORD_PER_PAGE
    template_name = 'cashflow/profile.html'
    user = None

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Record.objects.select_related(
            'user', 'category'
        ).filter(user=self.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.user
        return context


def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'title')
    return JsonResponse(list(categories), safe=False)


def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(
        category_id=category_id
    ).values('id', 'title')
    return JsonResponse(list(subcategories), safe=False)


def page_not_found(request, exception):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)


def failure_server(request):
    return render(request, 'pages/500.html', status=500)
