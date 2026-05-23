from .models import ContactInfo


def global_contact(request):

    contact = ContactInfo.objects.filter(
        active=True
    ).first()

    return {

        'contact': contact

    }