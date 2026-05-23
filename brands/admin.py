from django.contrib import admin
from .models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display=(

        'name',
        'active',
        'created'

    )

    list_filter=(

        'active',
    )

    search_fields=(

        'name',
    )