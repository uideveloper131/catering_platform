from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display=(

        'name',
        'active'

    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display=(

        'name',
        'brand',
        'category',
        'available'
    )

    list_filter=(

        'brand',
        'category',
        'available'
    )

    search_fields=(

        'name',
    )