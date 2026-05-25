from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from inquiries.models import Inquiry
from menu.models import MenuItem
from brands.models import Brand
from core.models import (
    EventService,
    Testimonial,
    ContactMessage,
    FAQ,
    OfferPackage
)
from gallery.models import Gallery


# ==========================
# DASHBOARD HOME
# ==========================

@login_required
def admin_dashboard(request):

    total_inquiries = Inquiry.objects.count()

    total_menu = MenuItem.objects.count()

    total_brands = Brand.objects.count()

    total_events = EventService.objects.count()

    total_gallery = Gallery.objects.count()

    total_testimonials = Testimonial.objects.count()

    total_faqs = FAQ.objects.count()

    total_offers = OfferPackage.objects.count()

    total_messages = ContactMessage.objects.count()

    new_inquiries = Inquiry.objects.filter(
        status='New'
    ).count()


    recent_inquiries = Inquiry.objects.order_by(
        '-created'
    )[:5]


    recent_messages = ContactMessage.objects.order_by(
        '-created'
    )[:5]


    context={

        'total_inquiries':total_inquiries,

        'total_menu':total_menu,

        'total_brands':total_brands,

        'total_events':total_events,

        'total_gallery':total_gallery,

        'total_testimonials':total_testimonials,

        'total_faqs':total_faqs,

        'total_offers':total_offers,

        'total_messages':total_messages,

        'new_inquiries':new_inquiries,

        'recent_inquiries':recent_inquiries,

        'recent_messages':recent_messages

    }

    return render(

        request,
        'dashboard/index.html',
        context
    )



# ==========================
# INQUIRIES
# ==========================

@login_required
def inquiries_management(request):

    inquiries = Inquiry.objects.all().order_by(
        '-created'
    )

    search=request.GET.get(
        'search'
    )

    status=request.GET.get(
        'status'
    )


    if search:

        inquiries=inquiries.filter(

            full_name__icontains=search

        )


    if status:

        inquiries=inquiries.filter(

            status=status

        )


    context={

        'inquiries':inquiries

    }

    return render(

        request,
        'dashboard/inquiries.html',
        context
    )



# ==========================
# BRANDS
# ==========================

@login_required
def brands_management(request):

    brands=Brand.objects.all()

    context={

        'brands':brands

    }

    return render(

        request,
        'dashboard/brands.html',
        context
    )



# ==========================
# EVENTS
# ==========================

@login_required
def events_management(request):

    events=EventService.objects.all()

    context={

        'events':events

    }

    return render(

        request,
        'dashboard/events.html',
        context
    )



# ==========================
# GALLERY
# ==========================

@login_required
def gallery_management(request):

    gallery=Gallery.objects.all()

    context={

        'gallery':gallery

    }

    return render(

        request,
        'dashboard/gallery.html',
        context
    )



# ==========================
# OFFERS
# ==========================

@login_required
def offers_management(request):

    offers=OfferPackage.objects.all()

    context={

        'offers':offers

    }

    return render(

        request,
        'dashboard/offers.html',
        context
    )



# ==========================
# CONTACT MESSAGES
# ==========================

@login_required
def messages_management(request):

    messages=ContactMessage.objects.all().order_by(
        '-created'
    )

    context={

        'messages':messages

    }

    return render(

        request,
        'dashboard/messages.html',
        context
    )