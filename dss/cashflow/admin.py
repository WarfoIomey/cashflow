from django.contrib import admin

from .models import Category, Record, Type, Status, Subcategory


admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Record)
admin.site.register(Subcategory)
