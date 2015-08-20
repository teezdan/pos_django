from django.contrib import admin
from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'items']


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']

    class Meta:
        ordering = ['category__name', 'price',]
