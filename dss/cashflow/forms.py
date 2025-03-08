from django import forms
from django.contrib.auth import get_user_model

from .models import Category, Record, Type, Subcategory, Status

User = get_user_model()


class RecordFilterForm(forms.Form):
    """Форма для фильтрации записей."""

    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Дата с"
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Дата по"
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        empty_label="Все статусы"
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        empty_label="Все типы"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="Все категории"
    )
    subcategory = forms.ModelChoiceField(
        queryset=Subcategory.objects.all(),
        required=False,
        empty_label="Все подкатегории"
    )


class RecordForm(forms.ModelForm):
    """Форма для записей."""

    created_at = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            },
            format='%Y-%m-%d',
        ),
        required=False,
    )
    status = forms.ModelChoiceField(
        required=False,
        queryset=Status.objects.all(),
        empty_label='Выберите статус',
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        empty_label='Выберите тип',
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        empty_label='Сначала выберите тип',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_category'
        })
    )
    subcategory = forms.ModelChoiceField(
        queryset=Subcategory.objects.none(),
        empty_label='Сначала выберите тип',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_subcategory'
        })
    )
    amount = forms.IntegerField(
        required=True,
        min_value=0
    )
    comment = forms.Textarea()

    def __init__(self, *args, **kwargs):
        """Метод для корректной динамической подгрузки формы."""
        super().__init__(*args, **kwargs)
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(
                    type_id=type_id
                )
            except (ValueError, TypeError):
                pass
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields[
                    'subcategory'
                ].queryset = Subcategory.objects.filter(
                    category_id=category_id
                )
            except (ValueError, TypeError):
                pass

    class Meta:
        model = Record
        fields = (
            'status',
            'type',
            'category',
            'subcategory',
            'amount',
            'comment',
            'created_at',
        )


class StatusForm(forms.ModelForm):
    """Форма для статусов."""

    class Meta:
        model = Status
        fields = ('title', 'description')


class TypeForm(forms.ModelForm):
    """Форма для типов."""

    class Meta:
        model = Type
        fields = ('title', 'description')


class CategoryForm(forms.ModelForm):
    """Форма для категорий."""

    class Meta:
        model = Category
        fields = ('title', 'description', 'slug')


class SubcategoryForm(forms.ModelForm):
    """Форма для подкатегорий."""

    class Meta:
        model = Subcategory
        fields = ('title', 'description', 'slug')
