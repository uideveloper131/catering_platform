from django.shortcuts import render

from brands.models import Brand
from menu.models import MenuItem
from gallery.models import Gallery
from .models import FAQ, Service,Testimonial, ContactInfo ,CTASection,Statistic, OfferPackage, EventService


def home(request):

    brands = Brand.objects.filter(
        active=True
    )
    menu_items = MenuItem.objects.filter(
        available=True
    )[:6]
    services = Service.objects.filter(
        active=True
    )
    testimonials = Testimonial.objects.filter(
        active=True
    )
    cta = CTASection.objects.filter(
        active=True
    ).first()
    gallery_items = Gallery.objects.filter(
        active=True
    ).order_by(
        '-created'
    )[:6]
    contact = ContactInfo.objects.filter(
        active=True
    ).first()
    statistics = Statistic.objects.filter(
        active=True
    )

    context = {

        'brands': brands,
        'menu_items': menu_items,
        'services': services,
        'testimonials': testimonials,
        'cta': cta,
        'gallery_items': gallery_items,
        'contact': contact,
        'statistics': statistics

    }

    return render(
        request,
        'home/index.html',
        context
    )


def contact_view(request):

    contact=ContactInfo.objects.filter(
        active=True
    ).first()

    context={

        'contact':contact

    }
    return render(

        request,
        'contact/contact.html',
        context
    )


def faq_view(request):
    faqs = FAQ.objects.filter(
        active=True
    )
    context = {

        'faqs': faqs

    }
    return render(
        request,
        'components/faq.html',
        context
    )


def offers_view(request):

    offers = OfferPackage.objects.filter(
        active=True
    )

    context={

        'offers':offers

    }

    return render(

        request,
        'gallery/offers.html',
        context
    )


def offer_detail(request,id):

    offer = OfferPackage.objects.get(
        id=id
    )

    context={

        'offer':offer

    }

    return render(

        request,
        'gallery/offer_detail.html',
        context
    )


def event_services(request):

    events = EventService.objects.filter(
        active=True
    )

    context={

        'events':events

    }

    return render(

        request,
        'events/events.html',
        context
    )


def event_detail(request,id):

    event = EventService.objects.get(
        id=id
    )

    context={

        'event':event

    }

    return render(

        request,
        'events/event_detail.html',
        context
    )