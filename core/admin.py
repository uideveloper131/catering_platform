from .models import FAQ, Testimonial, ContactInfo, CTASection, Statistic, OfferPackage, PackageFeature, EventService, EventMenu, EventPackage, ContactMessage
from django.contrib import admin
from .models import (
    EventService,
    EventMenu,
    EventPackage
)
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):

    list_display=(

        'question',
        'active',
        'created'

    )

    list_filter=(

        'active',
    )

    search_fields=(

        'question',
    )



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display=(

        'customer_name',
        'rating',
        'active'

    )

    list_filter=(

        'rating',
        'active'

    )

    search_fields=(

        'customer_name',
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):

    list_display=(

        'email',
        'phone',
        'active'

    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display=(

        'full_name',
        'email',
        'subject',
        'created'

    )

    search_fields=(

        'full_name',
        'email'

    )

@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):

    list_display=(

        'title',
        'active'

    )
    list_filter=(

        'active',
    )

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):

    list_display=(

        'title',
        'value',
        'active'

    )

    list_filter=(

        'active',
    )

    search_fields=(

        'title',
    )

class PackageFeatureInline(
    admin.TabularInline
):

    model = PackageFeature
    extra = 1


@admin.register(OfferPackage)
class OfferPackageAdmin(
    admin.ModelAdmin
):

    list_display=(

        'title',
        'price',
        'active'

    )

    list_filter=(

        'active',
    )

    search_fields=(

        'title',
    )

    inlines=[

        PackageFeatureInline
    ]



class EventMenuInline(
    admin.TabularInline
):

    model = EventMenu
    extra = 1



class EventPackageInline(
    admin.TabularInline
):

    model = EventPackage
    extra = 1



@admin.register(EventService)
class EventServiceAdmin(
    admin.ModelAdmin
):

    list_display = (

        'title',
        'active',
        'created'

    )

    list_filter = (

        'active',
    )

    search_fields = (

        'title',
        'description'
    )

    ordering = (

        '-created',
    )

    inlines = [

        EventMenuInline,
        EventPackageInline

    ]



@admin.register(EventMenu)
class EventMenuAdmin(
    admin.ModelAdmin
):

    list_display = (

        'event',
        'menu_item'
    )

    list_filter = (

        'event',
    )

    search_fields = (

        'event__title',
        'menu_item__name'
    )



@admin.register(EventPackage)
class EventPackageAdmin(
    admin.ModelAdmin
):

    list_display = (

        'event',
        'package'
    )

    list_filter = (

        'event',
    )

    search_fields = (

        'event__title',
        'package__title'
    )