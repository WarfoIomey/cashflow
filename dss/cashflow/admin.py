from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Type


admin.site.register(Category)
admin.site.register(Type)
