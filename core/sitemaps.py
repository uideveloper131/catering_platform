# core/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from brands.models import Brand
from core.models import (
    EventService,
    OfferPackage
)


class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = "weekly"

    def items(self):

        return [ 'home', 'contact', 'events', 'offers', 'gallery', 'inquiry', ]

    def location(self, item):

        return reverse(item)


class BrandSitemap(Sitemap):

    priority = 0.8
    changefreq = "monthly"

    def items(self):

        return Brand.objects.filter(
            active=True
        )


class EventSitemap(Sitemap):

    priority = 0.8
    changefreq = "monthly"

    def items(self):

        return EventService.objects.filter(
            active=True
        )


class OfferSitemap(Sitemap):

    priority = 0.8
    changefreq = "monthly"

    def items(self):

        return OfferPackage.objects.filter(
            active=True
        )