from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display = (

        'full_name',
        'email',
        'phone',
        'event_type',
        'event_date',
        'guests',
        'budget',
        'status',
        'created'

    )

    list_filter = (

        'status',
        'event_type',
        'created'

    )

    search_fields = (

        'full_name',
        'email',
        'phone'

    )

    list_editable = (

        'status',
    )

    ordering = (

        '-created',
    )