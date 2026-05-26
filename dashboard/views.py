from brands.forms import BrandForm
from core.forms import EventForm
from gallery.forms import GalleryForm
from core.forms import OfferForm
from core.forms import TestimonialForm
from core.forms import FAQForm
from core.models import ContactInfo
from core.forms import ContactInfoForm
from core.models import Statistic
from core.forms import StatisticForm
from core.models import CTASection
from core.forms import CTAForm
from menu.forms import MenuItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

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
# INQUIRIES MANAGEMENT
# ==========================

@login_required
def inquiries_management(request):
    inquiries=Inquiry.objects.all().order_by(
        '-created'
    )

    search=request.GET.get(
        'search'
    )

    if search:

        inquiries=inquiries.filter(

            full_name__icontains=search

        )

    context={

        'inquiries':inquiries

    }
    return render(

        request,
        'dashboard/inquiries/list.html',
        context
    )


@login_required
def update_inquiry_status(request,id):

    inquiry=get_object_or_404(
        Inquiry,
        id=id
    )

    if request.method=="POST":

        status=request.POST.get(
            'status'
        )

        inquiry.status=status

        inquiry.save()

    return redirect(
        'inquiries_management'
    )




@login_required
def delete_inquiry(request,id):

    inquiry=get_object_or_404(
        Inquiry,
        id=id
    )

    inquiry.delete()

    return redirect(
        'inquiries_management'
    )



@login_required
def brands_management(request):

    brands=Brand.objects.all()

    search=request.GET.get(
        'search'
    )

    if search:

        brands=brands.filter(

            name__icontains=search

        )

    return render(

        request,
        'dashboard/brands/list.html',
        {

            'brands':brands

        }

    )




@login_required
def add_brand(request):

    form=BrandForm()

    if request.method=="POST":

        form=BrandForm(

            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'brands_management'
            )


    return render(

        request,
        'dashboard/brands/form.html',
        {

            'form':form,
            'title':'Add Brand'

        }

    )




@login_required
def edit_brand(request,id):

    brand=get_object_or_404(

        Brand,
        id=id
    )

    form=BrandForm(
        instance=brand
    )

    if request.method=="POST":

        form=BrandForm(

            request.POST,
            request.FILES,
            instance=brand
        )

        if form.is_valid():

            form.save()

            return redirect(
                'brands_management'
            )


    return render(

        request,
        'dashboard/brands/form.html',
        {

            'form':form,
            'title':'Edit Brand'

        }

    )




@login_required
def delete_brand(request,id):

    brand=get_object_or_404(

        Brand,
        id=id
    )

    brand.delete()

    return redirect(
        'brands_management'
    )


# ==========================
# EVENTS
# ==========================
@login_required
def events_management(request):

    events=EventService.objects.all()

    search=request.GET.get(
        'search'
    )

    if search:

        events=events.filter(

            title__icontains=search

        )


    context={

        'events':events

    }

    return render(

        request,
        'dashboard/events/list.html',
        context
    )



@login_required
def add_event(request):

    form=EventForm()

    if request.method=="POST":

        form=EventForm(

            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(

                'events_management'
            )


    context={

        'form':form,
        'title':'Add Event'

    }

    return render(

        request,
        'dashboard/events/form.html',
        context
    )




@login_required
def edit_event(request,id):

    event=get_object_or_404(

        EventService,
        id=id
    )

    form=EventForm(
        instance=event
    )

    if request.method=="POST":

        form=EventForm(

            request.POST,
            request.FILES,
            instance=event
        )

        if form.is_valid():

            form.save()

            return redirect(

                'events_management'
            )


    context={

        'form':form,
        'title':'Edit Event'

    }

    return render(

        request,
        'dashboard/events/form.html',
        context
    )




@login_required
def delete_event(request,id):

    event=get_object_or_404(

        EventService,
        id=id
    )

    event.delete()

    return redirect(

        'events_management'
    )


# ==========================
# GALLERY
# ==========================
@login_required
def gallery_management(request):

    gallery=Gallery.objects.all()

    search=request.GET.get(
        'search'
    )

    if search:

        gallery=gallery.filter(

            title__icontains=search

        )

    context={

        'gallery':gallery

    }

    return render(

        request,
        'dashboard/gallery/list.html',
        context
    )




@login_required
def add_gallery(request):

    form=GalleryForm()

    if request.method=="POST":

        form=GalleryForm(

            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(

                'gallery_management'
            )

    context={

        'form':form,
        'title':'Add Gallery Image'

    }

    return render(

        request,
        'dashboard/gallery/form.html',
        context
    )




@login_required
def edit_gallery(request,id):

    gallery=get_object_or_404(

        Gallery,
        id=id
    )

    form=GalleryForm(
        instance=gallery
    )

    if request.method=="POST":

        form=GalleryForm(

            request.POST,
            request.FILES,
            instance=gallery
        )

        if form.is_valid():

            form.save()

            return redirect(

                'gallery_management'
            )

    context={

        'form':form,
        'title':'Edit Gallery'

    }

    return render(

        request,
        'dashboard/gallery/form.html',
        context
    )




@login_required
def delete_gallery(request,id):

    gallery=get_object_or_404(

        Gallery,
        id=id
    )

    gallery.delete()

    return redirect(

        'gallery_management'
    )

# ==========================
# OFFERS
# ==========================
@login_required
def offers_management(request):
    offers=OfferPackage.objects.all()
    search=request.GET.get(
        'search'
    )
    if search:
        offers=offers.filter(
            title__icontains=search

        )
    return render(
        request,
        'dashboard/offers/list.html',
        {
            'offers':offers
        }
    )

@login_required
def add_offer(request):
    form=OfferForm()
    if request.method=="POST":
        form=OfferForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect(
                'offers_management'
            )
    return render(
        request,
        'dashboard/offers/form.html',
        {

            'form':form,
            'title':'Add Offer'
        }
    )

@login_required
def edit_offer(request,id):
    offer=get_object_or_404(
        OfferPackage,
        id=id
    )
    form=OfferForm(
        instance=offer
    )
    if request.method=="POST":
        form=OfferForm(
            request.POST,
            request.FILES,
            instance=offer
        )

        if form.is_valid():
            form.save()
            return redirect(
                'offers_management'
            )

    return render(
        request,
        'dashboard/offers/form.html',
        {

            'form':form,
            'title':'Edit Offer'

        }

    )

@login_required
def delete_offer(request,id):

    offer=get_object_or_404(
        OfferPackage,
        id=id
    )
    offer.delete()
    return redirect(
        'offers_management'
    )

# =============================
# FAQ MANAGEMENT
# =============================

@login_required
def faq_management(request):

    faqs=FAQ.objects.all()

    search=request.GET.get(
        'search'
    )

    if search:

        faqs=faqs.filter(

            question__icontains=search

        )

    return render(

        request,
        'dashboard/faq/list.html',
        {

            'faqs':faqs

        }

    )




@login_required
def add_faq(request):

    form=FAQForm()

    if request.method=="POST":

        form=FAQForm(

            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(

                'faq_management'
            )

    return render(

        request,
        'dashboard/faq/form.html',
        {

            'form':form,
            'title':'Add FAQ'

        }

    )




@login_required
def edit_faq(request,id):

    faq=get_object_or_404(

        FAQ,
        id=id
    )

    form=FAQForm(
        instance=faq
    )

    if request.method=="POST":

        form=FAQForm(

            request.POST,
            instance=faq
        )

        if form.is_valid():

            form.save()

            return redirect(

                'faq_management'
            )

    return render(

        request,
        'dashboard/faq/form.html',
        {

            'form':form,
            'title':'Edit FAQ'

        }

    )




@login_required
def delete_faq(request,id):

    faq=get_object_or_404(

        FAQ,
        id=id
    )

    faq.delete()

    return redirect(
        'faq_management'
    )

# ==========================
# TESTIMONIAL MANAGEMENT
# ==========================

@login_required
def testimonials_management(request):

    testimonials=Testimonial.objects.all()

    search=request.GET.get(
        'search'
    )

    if search:

        testimonials=testimonials.filter(

            customer_name__icontains=search

        )

    return render(

        request,
        'dashboard/testimonials/list.html',
        {

            'testimonials':testimonials

        }

    )


@login_required
def add_testimonial(request):
    form=TestimonialForm()
    if request.method=="POST":
        form=TestimonialForm(

            request.POST,
            request.FILES
        )
        if form.is_valid():

            form.save()

            return redirect(

                'testimonials_management'
            )

    return render(

        request,
        'dashboard/testimonials/form.html',
        {

            'form':form,
            'title':'Add Testimonial'

        }

    )


@login_required
def edit_testimonial(request,id):

    testimonial=get_object_or_404(

        Testimonial,
        id=id
    )

    form=TestimonialForm(
        instance=testimonial
    )

    if request.method=="POST":

        form=TestimonialForm(

            request.POST,
            request.FILES,
            instance=testimonial
        )

        if form.is_valid():

            form.save()

            return redirect(

                'testimonials_management'
            )

    return render(

        request,
        'dashboard/testimonials/form.html',
        {

            'form':form,
            'title':'Edit Testimonial'

        }

    )


@login_required
def delete_testimonial(request,id):

    testimonial=get_object_or_404(

        Testimonial,
        id=id
    )

    testimonial.delete()

    return redirect(

        'testimonials_management'
    )

# ==========================
# CONTACT MESSAGES
# ==========================

@login_required
def messages_management(request):

    messages = ContactMessage.objects.all().order_by(
        '-created'
    )

    search=request.GET.get(
        'search'
    )

    if search:

        messages=messages.filter(

            full_name__icontains=search

        )

    context={

        'messages':messages

    }

    return render(

        request,
        'dashboard/messages/list.html',
        context
    )



@login_required
def message_detail(request,id):

    message=get_object_or_404(

        ContactMessage,
        id=id
    )

    return render(

        request,
        'dashboard/messages/detail.html',

        {

            'message':message

        }

    )



@login_required
def delete_message(request,id):

    message=get_object_or_404(

        ContactMessage,
        id=id
    )

    message.delete()

    return redirect(

        'messages_management'
    )

# ==========================
# CONTACT INFO MANAGEMENT
# ==========================

@login_required
def contact_management(request):

    contacts=ContactInfo.objects.all()

    return render(

        request,
        'dashboard/contact/list.html',

        {

            'contacts':contacts

        }

    )




@login_required
def add_contact(request):

    form=ContactInfoForm()

    if request.method=="POST":

        form=ContactInfoForm(

            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'contact_management'
            )

    return render(

        request,
        'dashboard/contact/form.html',

        {

            'form':form,
            'title':'Add Contact Information'

        }

    )




@login_required
def edit_contact(request,id):

    contact=get_object_or_404(

        ContactInfo,
        id=id
    )

    form=ContactInfoForm(
        instance=contact
    )

    if request.method=="POST":

        form=ContactInfoForm(

            request.POST,
            instance=contact
        )

        if form.is_valid():

            form.save()

            return redirect(
                'contact_management'
            )

    return render(

        request,
        'dashboard/contact/form.html',

        {

            'form':form,
            'title':'Edit Contact Information'

        }

    )




@login_required
def delete_contact(request,id):

    contact=get_object_or_404(

        ContactInfo,
        id=id
    )

    contact.delete()

    return redirect(
        'contact_management'
    )


# ==========================
# STATISTICS MANAGEMENT
# ==========================

@login_required
def statistics_management(request):

    statistics=Statistic.objects.all()

    return render(

        request,
        'dashboard/statistics/list.html',

        {

            'statistics':statistics

        }

    )




@login_required
def add_statistic(request):

    form=StatisticForm()

    if request.method=="POST":

        form=StatisticForm(

            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'statistics_management'
            )

    return render(

        request,
        'dashboard/statistics/form.html',

        {

            'form':form,
            'title':'Add Statistic'

        }

    )




@login_required
def edit_statistic(request,id):

    statistic=get_object_or_404(

        Statistic,
        id=id
    )

    form=StatisticForm(
        instance=statistic
    )

    if request.method=="POST":

        form=StatisticForm(

            request.POST,
            instance=statistic
        )

        if form.is_valid():

            form.save()

            return redirect(
                'statistics_management'
            )

    return render(

        request,
        'dashboard/statistics/form.html',

        {

            'form':form,
            'title':'Edit Statistic'

        }

    )


@login_required
def delete_statistic(request,id):

    statistic=get_object_or_404(

        Statistic,
        id=id
    )

    statistic.delete()

    return redirect(
        'statistics_management'
    )

# ==========================
# CTA MANAGEMENT
# ==========================

@login_required
def cta_management(request):
    ctas=CTASection.objects.all()
    return render(
        request,
        'dashboard/cta/list.html',
        {
            'ctas':ctas

        }
    )

@login_required
def add_cta(request):
    form=CTAForm()
    if request.method=="POST":
        form=CTAForm(
            request.POST
        )
        if form.is_valid():
            form.save()
            return redirect(
                'cta_management'
            )

    return render(
        request,
        'dashboard/cta/form.html',
        {
            'form':form,
            'title':'Add CTA'
        }

    )

@login_required
def edit_cta(request,id):
    cta=get_object_or_404(
        CTASection,
        id=id
    )
    form=CTAForm(
        instance=cta
    )
    if request.method=="POST":
        form=CTAForm(
            request.POST,
            instance=cta
        )

        if form.is_valid():
            form.save()
            return redirect(
                'cta_management'
            )

    return render(
        request,
        'dashboard/cta/form.html',
        {
            'form':form,
            'title':'Edit CTA'

        }

    )

@login_required
def delete_cta(request,id):
    cta=get_object_or_404(
        CTASection,
        id=id
    )
    cta.delete()
    return redirect(
        'cta_management'
    )

# ==========================
# MENU MANAGEMENT
# ==========================

@login_required
def menu_management(request):
    menus=MenuItem.objects.all()
    search=request.GET.get(
        'search'
    )
    if search:
        menus=menus.filter(
            name__icontains=search

        )

    return render(
        request,
        'dashboard/menu/list.html',
        {
            'menus':menus

        }

    )

@login_required
def add_menu(request):
    form=MenuItemForm()
    if request.method=="POST":
        form=MenuItemForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect(
                'menu_management'
            )

    return render(
        request,
        'dashboard/menu/form.html',
        {
            'form':form,
            'title':'Add Menu Item'

        }

    )

@login_required
def edit_menu(request,id):
    menu=get_object_or_404(
        MenuItem,
        id=id
    )
    form=MenuItemForm(
        instance=menu
    )

    if request.method=="POST":
        form=MenuItemForm(
            request.POST,
            request.FILES,
            instance=menu
        )

        if form.is_valid():
            form.save()
            return redirect(
                'menu_management'
            )

    return render(
        request,
        'dashboard/menu/form.html',
        {

            'form':form,
            'title':'Edit Menu Item'

        }
    )


@login_required
def delete_menu(request,id):
    menu=get_object_or_404(
        MenuItem,
        id=id
    )

    menu.delete()
    return redirect(
        'menu_management'
    )