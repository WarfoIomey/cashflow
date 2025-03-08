from django import forms
from django.contrib.auth import get_user_model

from .models import Record, Type, Category, Subcategory, Status

User = get_user_model()


class RecordFilterForm(forms.Form):
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
        exclude = ('user',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%d-%m-%Y',
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            )
        }


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('title', 'description')


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ('title', 'description')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title', 'description', 'slug')


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = ('title', 'description', 'slug')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
