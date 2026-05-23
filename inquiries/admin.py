from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display=(

        'full_name',
        'event_type',
        'event_date',
        'guests',
        'budget',
        'status',
        'created'

    )

    list_filter=(

        'status',
        'event_type',
        'created',
        'service_style',
        'indoor_outdoor'

    )

    search_fields=(

        'full_name',
        'email',
        'phone',
        'company',
        'venue'

    )

    list_editable=(

        'status',
    )

    ordering=(

        '-created',
    )

    readonly_fields=(

        'created',
        'updated'

    )

    date_hierarchy='created'

    list_per_page=20


    fieldsets=(

        (

            'Contact Information',
            {

                'fields':(

                    'full_name',
                    'email',
                    'phone',
                    'company'

                )
            }

        ),

        (

            'Event Information',
            {

                'fields':(

                    'event_type',
                    'event_date',
                    'flexible_date',
                    'event_time',
                    'guests',
                    'venue',
                    'indoor_outdoor'

                )
            }

        ),

        (

            'Food Preferences',
            {

                'fields':(

                    'cuisine',
                    'service_style',
                    'dietary_requirements',
                    'services_needed'

                )
            }

        ),

        (

            'Budget & Notes',
            {

                'fields':(

                    'budget',
                    'event_details',
                    'hear_about'

                )
            }

        ),

        (

            'Inquiry Status',
            {

                'fields':(

                    'status',
                    'created',
                    'updated'

                )
            }

        )

    )