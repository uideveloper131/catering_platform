from django.contrib import admin
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display=(

        'title',
        'category',
        'active',
        'created'

    )

    list_filter=(

        'category',
        'active'

    )

    search_fields=(

        'title',
        'category'

    )

    ordering=(

        '-created',
    )