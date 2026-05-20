from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'active',
    )

    list_filter = (
        'active',
    )

    search_fields = (
        'name',
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'brand',
        'category',
        'price',
        'available',
    )

    list_filter = (
        'brand',
        'category',
        'available',
    )

    search_fields = (
        'name',
    )