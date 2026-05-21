from django.urls import path
from .views import *

urlpatterns=[

    path(
        '',
        admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'inquiries/',
        inquiries_management,
        name='inquiries_management'
    ),

]