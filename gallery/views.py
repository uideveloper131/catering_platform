from django.shortcuts import render
from .models import Gallery


def gallery_view(request):

    gallery_items=Gallery.objects.filter(
        active=True
    )

    context={

        'gallery_items':gallery_items

    }

    return render(
        request,
        'gallery/gallery.html',
        context
    )