from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.contrib.sitemaps.views import sitemap

from core.sitemaps import (
    StaticViewSitemap,
    BrandSitemap,
    EventSitemap,
    OfferSitemap
)


sitemaps = {

    'static': StaticViewSitemap,
    'brands': BrandSitemap,
    'events': EventSitemap,
    'offers': OfferSitemap,

}


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        ),
    ),

    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),

    path(
        '',
        include('core.urls')
    ),

    path(
        'request-quote/',
        include('inquiries.urls')
    ),

    path(
        'dashboard/',
        include('dashboard.urls')
    ),

    path(
        'accounts/',
        include('accounts.urls')
    ),

    path(
        'brands/',
        include('brands.urls')
    ),

    path(
        'gallery/',
        include('gallery.urls')
    ),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)