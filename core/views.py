from django.shortcuts import render
from brands.models import Brand
from menu.models import MenuItem


def home(request):

    brands = Brand.objects.filter(
        active=True
    )

    menu_items = MenuItem.objects.filter(
        available=True
    )[:6]

    context = {
        'brands': brands,
        'menu_items': menu_items
    }

    return render(
        request,
        'home/index.html',
        context
    )