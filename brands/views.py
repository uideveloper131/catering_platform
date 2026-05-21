from django.shortcuts import render,get_object_or_404
from .models import Brand
from menu.models import MenuItem


def brands(request):

    brands=Brand.objects.filter(
        active=True
    )

    context={

        'brands':brands
    }

    return render(
        request,
        'brands/brands.html',
        context
    )


def brand_detail(request,id):

    brand=get_object_or_404(
        Brand,
        id=id
    )

    menu_items=MenuItem.objects.filter(
        brand=brand
    )

    context={

        'brand':brand,
        'menu_items':menu_items
    }

    return render(
        request,
        'brands/brand_detail.html',
        context
    )