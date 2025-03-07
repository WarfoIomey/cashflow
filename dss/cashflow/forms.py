from django import forms
from django.contrib.auth import get_user_model

from .models import Record, TypeMoney, Category, SubCategory, StatusMoney

User = get_user_model()


class RecordForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=StatusMoney.objects.all(),
        empty_label='Выберите статус',
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    type = forms.ModelChoiceField(
        queryset=TypeMoney.objects.all(),
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
        queryset=SubCategory.objects.none(),
        empty_label='Сначала выберите тип',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_subcategory'
        })
    )

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
        model = StatusMoney
        fields = ('title', 'description')


class TypeForm(forms.ModelForm):

    class Meta:
        model = TypeMoney
        fields = ('title', 'description')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('title', 'description', 'slug')


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = ('title', 'description', 'slug')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
