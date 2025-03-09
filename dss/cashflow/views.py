from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from django.urls import reverse, reverse_lazy


from .models import Category, Type, Record, Subcategory, Status
from .mixins import (
    CategoryEditMixin,
    OnlyAuthorMixin,
    RecordEditMixin,
    TypeEditMixin,
    StatusEditMixin,
    SubcategoryEditMixin
)
from .forms import RecordForm, RecordFilterForm, TypeForm, StatusForm
from .utils import get_types, get_categorys, get_subcategorys, get_status


RECORD_PER_PAGE: int = 3

User = get_user_model()


class RecordListView(LoginRequiredMixin, ListView):
    """Получение всех записей, с возможностью их отфильтровать."""

    model = Record
    template_name: str = 'cashflow/index.html'
    paginate_by: int = RECORD_PER_PAGE

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        form = RecordFilterForm(self.request.GET)

        if form.is_valid():
            if (form.cleaned_data["start_date"] and
                    form.cleaned_data["end_date"]):
                queryset = queryset.filter(
                    created_at__range=(
                        form.cleaned_data["start_date"],
                        form.cleaned_data["end_date"]
                    )
                )
            if form.cleaned_data["start_date"]:
                queryset = queryset.filter(
                    created_at__gte=form.cleaned_data["start_date"]
                )
            if form.cleaned_data["end_date"]:
                queryset = queryset.filter(
                    created_at__lte=form.cleaned_data["end_date"]
                )
            if form.cleaned_data["status"]:
                queryset = queryset.filter(status=form.cleaned_data["status"])
            if form.cleaned_data["type"]:
                queryset = queryset.filter(type=form.cleaned_data["type"])
            if form.cleaned_data["category"]:
                queryset = queryset.filter(
                    category=form.cleaned_data["category"]
                )
            if form.cleaned_data["subcategory"]:
                queryset = queryset.filter(
                    subcategory=form.cleaned_data["subcategory"]
                )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RecordFilterForm(self.request.GET)
        return context


class RecordCreateView(LoginRequiredMixin, RecordEditMixin, CreateView):
    """Создание записи."""

    template_name: str = 'cashflow/create.html'
    success_url = reverse_lazy('cashflow:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecordCreateView, self).form_valid(form)


class RecordDetailView(LoginRequiredMixin, RecordEditMixin, DetailView):
    """Обзор одной записи."""

    pk_url_kwarg: str = 'record_id'
    template_name: str = 'cashflow/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record = get_object_or_404(
            Record,
            id=self.kwargs['record_id'],
            user=self.request.user
        )
        context['record'] = record
        if record.status is not None:
            context['status_title'] = record.status.title
        else:
            context['status_title'] = None
        context['type_title'] = record.type.title
        context['category_title'] = record.category.title
        context['subcategory_title'] = record.subcategory.title
        return context


class RecordUpdateView(OnlyAuthorMixin, RecordEditMixin, UpdateView):
    """Редактирование записи."""

    template_name: str = 'cashflow/create.html'
    pk_url_kwarg: str = 'record_id'

    def get_success_url(self):
        return reverse(
            'cashflow:record_detail',
            kwargs={'record_id': self.kwargs['record_id']}
        )


class RecordDeleteView(OnlyAuthorMixin, RecordEditMixin, DeleteView):
    """Удаление записи."""

    pk_url_kwarg: str = 'record_id'
    template_name: str = 'cashflow/create.html'
    success_url = reverse_lazy('cashflow:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record = get_object_or_404(Record, pk=self.kwargs['record_id'])
        context['form'] = RecordForm(instance=record)
        return context


class StatusListView(LoginRequiredMixin, ListView):
    """Получение всех статусов."""

    model = Status
    template_name: str = 'cashflow/list.html'
    paginate_by: int = RECORD_PER_PAGE

    def get_queryset(self):
        return get_status(self.request.user)


class StatusDetailView(LoginRequiredMixin, DetailView):
    """Обзор одного статуса."""
    model = Status
    template_name: str = 'cashflow/detail.html'
    pk_url_kwarg: str = 'status_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = get_object_or_404(
            Status,
            id=self.kwargs['status_id'],
            user=self.request.user,
        )
        return context


class StatusCreateView(LoginRequiredMixin, StatusEditMixin, CreateView):
    """Создание статуса."""

    def get_success_url(self):
        return reverse('cashflow:status')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StatusUpdateView(OnlyAuthorMixin, StatusEditMixin, UpdateView):
    """Изменение статуса."""

    pk_url_kwarg: str = 'status_id'

    def get_success_url(self):
        return reverse(
            'cashflow:status_detail',
            kwargs={'status_id': self.kwargs['status_id']}
        )


class StatusDeleteView(OnlyAuthorMixin, StatusEditMixin, DeleteView):
    """Удаление статуса."""

    pk_url_kwarg: str = 'status_id'
    success_url = reverse_lazy('cashflow:status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = get_object_or_404(Status, pk=self.kwargs['status_id'])
        context['form'] = StatusForm(instance=status)
        return context


class TypeListView(LoginRequiredMixin, ListView):
    """Получение списка типов."""

    model = Type
    template_name: str = 'cashflow/list.html'
    paginate_by: int = RECORD_PER_PAGE

    def get_queryset(self):
        return get_types(self.request.user)


class TypeCreateView(LoginRequiredMixin, TypeEditMixin, CreateView):
    """Создание типов."""

    def get_success_url(self):
        return reverse('cashflow:type')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TypeUpdateView(OnlyAuthorMixin, TypeEditMixin, UpdateView):
    """Редактирование типов."""

    pk_url_kwarg: str = 'type_id'

    def get_success_url(self):
        return reverse(
            'cashflow:type_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
            }
        )


class TypeDeleteView(OnlyAuthorMixin, TypeEditMixin, DeleteView):
    """Удаленение типов."""

    pk_url_kwarg: str = 'type_id'
    success_url = reverse_lazy('cashflow:type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        type = get_object_or_404(Type, pk=self.kwargs['type_id'])
        context['form'] = TypeForm(instance=type)
        return context


class TypeDetailCategoryListView(LoginRequiredMixin, ListView):
    """Получение всех категорий определенного типа."""

    model = Category
    template_name: str = 'cashflow/detail.html'
    paginate_by: int = RECORD_PER_PAGE
    pk_url_kwarg: str = 'type_id'

    def get_queryset(self):
        return get_categorys(self.kwargs['type_id'], self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = get_object_or_404(
            Type,
            id=self.kwargs['type_id']
        )
        return context


class CategoryCreateView(LoginRequiredMixin, CategoryEditMixin, CreateView):
    """Создание категории."""

    type_card = None

    def dispatch(self, request, *args, **kwargs):
        self.type_card = get_object_or_404(Type, pk=kwargs['type_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.type = self.type_card
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'cashflow:type_detail',
            kwargs={'type_id': self.type_card.id}
        )


class CategoryUpdateView(OnlyAuthorMixin, CategoryEditMixin, UpdateView):
    """Редактирование категории."""

    slug_url_kwarg: str = 'category_slug'

    def get_success_url(self):
        return reverse(
            'cashflow:category_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
                'category_slug': self.kwargs['category_slug'],
            }
        )


class CategoryDeleteView(OnlyAuthorMixin, CategoryEditMixin, DeleteView):
    """Удаление категории."""

    slug_url_kwarg: str = 'category_slug'

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
    """Получение всех подкатегорий определенной категории."""

    model = Subcategory
    paginate_by: int = RECORD_PER_PAGE
    slug_url_kwarg: str = 'category_slug'
    template_name: str = 'cashflow/detail.html'

    def get_queryset(self):
        return get_subcategorys(
            self.kwargs['category_slug'],
            self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )
        context['type_id'] = self.kwargs['type_id']
        return context


class SubcategoryDetailView(LoginRequiredMixin, DetailView):
    """Обзор подкатегории."""

    model = Subcategory
    slug_url_kwarg: str = 'sub_slug'
    template_name: str = 'cashflow/detail.html'

    def get_queryset(self):
        return get_subcategorys(
            self.kwargs['category_slug'],
            self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_id'] = self.kwargs['type_id']
        context['category_slug'] = self.kwargs['category_slug']
        return context


class SubcategoryCreateView(
    LoginRequiredMixin,
    SubcategoryEditMixin,
    CreateView
):
    """Создание подкатегории."""

    category_card = None

    def dispatch(self, request, *args, **kwargs):
        self.category_card = get_object_or_404(
            Category,
            slug=kwargs['category_slug']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.category = self.category_card
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'cashflow:category_detail',
            kwargs={
                'type_id': self.category_card.type.id,
                'category_slug': self.category_card.slug
            }
        )


class SubcategoryUpdateView(OnlyAuthorMixin, SubcategoryEditMixin, UpdateView):
    """Редактирование подкатегории."""

    slug_url_kwarg: str = 'sub_slug'

    def get_success_url(self):
        return reverse(
            'cashflow:subcategory_detail',
            kwargs={
                'type_id': self.kwargs['type_id'],
                'category_slug': self.kwargs['category_slug'],
                'sub_slug': self.kwargs['sub_slug']
            }
        )


class SubcategoryDeleteView(OnlyAuthorMixin, SubcategoryEditMixin, DeleteView):
    """Удаление подкатегории."""

    slug_url_kwarg: str = 'sub_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = get_object_or_404(
            Subcategory,
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


def load_categories(request):
    """Динамическая подгрузка категориев для создания записи."""
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(
        type_id=type_id,
        user=request.user
    ).values('id', 'title')
    return JsonResponse(list(categories), safe=False)


def load_subcategories(request):
    """Динамическая подгрузка подкатегории для создания записи."""
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(
        category_id=category_id,
        user=request.user,
    ).values('id', 'title')
    return JsonResponse(list(subcategories), safe=False)


def page_not_found(request, exception):
    """Перенаправление на страницу 404"""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """Перенаправление на страницу 403"""
    return render(request, 'pages/403csrf.html', status=403)


def failure_server(request):
    """Перенаправление на страницу 500"""
    return render(request, 'pages/500.html', status=500)
