from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inquiries.models import Inquiry
from menu.models import MenuItem
from brands.models import Brand


@login_required
def admin_dashboard(request):

    total_inquiries = Inquiry.objects.count()

    total_menu = MenuItem.objects.count()

    total_brands = Brand.objects.count()

    new_inquiries = Inquiry.objects.filter(
        status='New'
    ).count()

    recent_inquiries = Inquiry.objects.order_by(
        '-created'
    )[:5]

    context={

        'total_inquiries':total_inquiries,
        'total_menu':total_menu,
        'total_brands':total_brands,
        'new_inquiries':new_inquiries,
        'recent_inquiries':recent_inquiries

    }

    return render(
        request,
        'dashboard/index.html',
        context
    )


@login_required
def inquiries_management(request):

    inquiries=Inquiry.objects.all().order_by(
        '-created'
    )

    search=request.GET.get(
        'search'
    )

    if search:

        inquiries=inquiries.filter(
            full_name__icontains=search
        )

    context={

        'inquiries':inquiries
    }

    return render(

        request,
        'dashboard/inquiries.html',
        context
    )