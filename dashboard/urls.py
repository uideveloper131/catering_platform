from django.urls import path
from .views import *

urlpatterns=[


    # ==========================
    # DASHBOARD
    # ==========================

    path(
        '',
        admin_dashboard,
        name='admin_dashboard'
    ),


    # ==========================
    # INQUIRIES
    # ==========================

    path(
        'inquiries/',
        inquiries_management,
        name='inquiries_management'
    ),

    path(
        'inquiries/update/<int:id>/',
        update_inquiry_status,
        name='update_inquiry_status'
    ),

    path(
        'inquiries/delete/<int:id>/',
        delete_inquiry,
        name='delete_inquiry'
    ),


    # ==========================
    # BRANDS
    # ==========================

    path(
        'brands/',
        brands_management,
        name='brands_management'
    ),

    path(
        'brands/add/',
        add_brand,
        name='add_brand'
    ),

    path(
        'brands/edit/<int:id>/',
        edit_brand,
        name='edit_brand'
    ),

    path(
        'brands/delete/<int:id>/',
        delete_brand,
        name='delete_brand'
    ),


    # ==========================
    # EVENTS
    # ==========================

    path(
        'events/',
        events_management,
        name='events_management'
    ),

    path(
        'events/add/',
        add_event,
        name='add_event'
    ),

    path(
        'events/edit/<int:id>/',
        edit_event,
        name='edit_event'
    ),

    path(
        'events/delete/<int:id>/',
        delete_event,
        name='delete_event'
    ),


    # ==========================
    # GALLERY
    # ==========================

    path(
        'gallery/',
        gallery_management,
        name='gallery_management'
    ),

    path(
        'gallery/add/',
        add_gallery,
        name='add_gallery'
    ),

    path(
        'gallery/edit/<int:id>/',
        edit_gallery,
        name='edit_gallery'
    ),

    path(
        'gallery/delete/<int:id>/',
        delete_gallery,
        name='delete_gallery'
    ),


    # ==========================
    # OFFERS
    # ==========================

    path(
        'offers/',
        offers_management,
        name='offers_management'
    ),

    path(
        'offers/add/',
        add_offer,
        name='add_offer'
    ),

    path(
        'offers/edit/<int:id>/',
        edit_offer,
        name='edit_offer'
    ),

    path(
        'offers/delete/<int:id>/',
        delete_offer,
        name='delete_offer'
    ),


    path(
    'faq/',
    faq_management,
    name='faq_management'
    ),

    path(
    'faq/add/',
    add_faq,
    name='add_faq'
    ),

    path(
    'faq/edit/<int:id>/',
    edit_faq,
    name='edit_faq'
    ),

    path(
    'faq/delete/<int:id>/',
    delete_faq,
    name='delete_faq'
    ),
    path(
    'testimonials/',
    testimonials_management,
    name='testimonials_management'
    ),

    path(
    'testimonials/add/',
    add_testimonial,
    name='add_testimonial'
    ),

    path(
    'testimonials/edit/<int:id>/',
    edit_testimonial,
    name='edit_testimonial'
    ),

    path(
    'testimonials/delete/<int:id>/',
    delete_testimonial,
    name='delete_testimonial'
    ),

    # ==========================
    # MESSAGES
    # ==========================

    path(
        'messages/',
        messages_management,
        name='messages_management'
    ),

    path(
        'messages/<int:id>/',
        message_detail,
        name='message_detail'
    ),

    path(
        'messages/delete/<int:id>/',
        delete_message,
        name='delete_message'
    ),

    path(
    'contact/',
    contact_management,
    name='contact_management'
    ),

    path(
    'contact/add/',
    add_contact,
    name='add_contact'
    ),

    path(
    'contact/edit/<int:id>/',
    edit_contact,
    name='edit_contact'
    ),

    path(
    'contact/delete/<int:id>/',
    delete_contact,
    name='delete_contact'
    ),

    path(
    'statistics/',
    statistics_management,
    name='statistics_management'
    ),

    path(
    'statistics/add/',
    add_statistic,
    name='add_statistic'
    ),

    path(
    'statistics/edit/<int:id>/',
    edit_statistic,
    name='edit_statistic'
    ),

    path(
    'statistics/delete/<int:id>/',
    delete_statistic,
    name='delete_statistic'
    ),

    path(
    'cta/',
    cta_management,
    name='cta_management'
    ),

    path(
    'cta/add/',
    add_cta,
    name='add_cta'
    ),

    path(
    'cta/edit/<int:id>/',
    edit_cta,
    name='edit_cta'
    ),

    path(
    'cta/delete/<int:id>/',
    delete_cta,
    name='delete_cta'
    ),

    path(
    'menu/',
    menu_management,
    name='menu_management'
    ),

    path(
    'menu/add/',
    add_menu,
    name='add_menu'
    ),

    path(
    'menu/edit/<int:id>/',
    edit_menu,
    name='edit_menu'
    ),

    path(
    'menu/delete/<int:id>/',
    delete_menu,
    name='delete_menu'
    ),

]