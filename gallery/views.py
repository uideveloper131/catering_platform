from django.shortcuts import render
from .models import Gallery


def gallery_view(request):

    images = Gallery.objects.filter(
        active=True
    )

    context={

        'images':images

    }

    return render(

        request,
        'gallery/gallery.html',
        context
    )