from brands.models import Brand
from menu.models import MenuItem
from gallery.models import Gallery
from .models import FAQ, Service,Testimonial, ContactInfo ,CTASection,Statistic, OfferPackage, EventService
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from .models import OfferPackage
from .models import ContactInfo
from .models import ContactMessage

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

    events = EventService.objects.filter(
        active=True
    )[:4]

    faqs = FAQ.objects.filter(
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
        'statistics': statistics,
        'events': events,
        'faqs': faqs

    }

    return render(

        request,
        'home/index.html',
        context
    )



def contact_view(request):

    contact = ContactInfo.objects.filter(
        active=True
    ).first()


    if request.method=="POST":

        full_name=request.POST.get(
            'full_name'
        )

        email=request.POST.get(
            'email'
        )

        subject=request.POST.get(
            'subject'
        )

        message=request.POST.get(
            'message'
        )


        ContactMessage.objects.create(

            full_name=full_name,
            email=email,
            subject=subject,
            message=message

        )


        send_mail(

            subject=f'New Contact Message: {subject}',

            message=f'''

New Contact Message

Name:
{full_name}

Email:
{email}

Message:

{message}

''',

            from_email=settings.EMAIL_HOST_USER,

            recipient_list=[
                settings.EMAIL_HOST_USER
            ],

            fail_silently=True
        )


        messages.success(

            request,

            'Message sent successfully.'
        )

        return redirect(
            'contact'
        )


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
    ).order_by(
        '-created'
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

    offer=get_object_or_404(

        OfferPackage,
        id=id,
        active=True
    )

    features=offer.features.all()


    context={

        'offer':offer,
        'features':features

    }

    return render(

        request,
        'gallery/offer_detail.html',
        context
    )



def event_services(request):

    events = EventService.objects.filter(
        active=True
    ).order_by(
        '-created'
    )

    context = {

        'events': events

    }

    return render(

        request,
        'events/events.html',
        context
    )


def event_detail(request,id):

    event = get_object_or_404(

        EventService,

        id=id,
        active=True
    )

    related_menus = event.event_menus.all()

    related_packages = event.event_packages.all()


    context = {

        'event': event,
        'related_menus': related_menus,
        'related_packages': related_packages

    }

    return render(

        request,
        'events/event_detail.html',
        context
    )