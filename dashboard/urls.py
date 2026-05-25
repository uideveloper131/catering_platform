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


    # ==========================
    # BRANDS
    # ==========================

    path(
        'brands/',
        brands_management,
        name='brands_management'
    ),


    # ==========================
    # EVENTS
    # ==========================

    path(
        'events/',
        events_management,
        name='events_management'
    ),


    # ==========================
    # GALLERY
    # ==========================

    path(
        'gallery/',
        gallery_management,
        name='gallery_management'
    ),


    # ==========================
    # OFFERS
    # ==========================

    path(
        'offers/',
        offers_management,
        name='offers_management'
    ),


    # ==========================
    # MESSAGES
    # ==========================

    path(
        'messages/',
        messages_management,
        name='messages_management'
    ),

]