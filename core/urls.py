from django.urls import path
from .views import home, contact_view, offers_view, offer_detail, event_detail, event_services, search_view


urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),
    path(
    'contact/',
    contact_view,
    name='contact'
    ),
    path(
        'offers/',
        offers_view,
        name='offers'
    ),
    path(
        'offers/<int:id>/',
        offer_detail,
        name='offer_detail'
    ),
    path(
        'events/',
        event_services,
        name='events'
    ),

    path(
        'events/<int:id>/',
        event_detail,
        name='event_detail'
    ),
    path('search/', search_view, name='search'),
]