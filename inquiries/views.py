from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import InquiryForm


def inquiry(request):

    form=InquiryForm()

    if request.method=="POST":

        form=InquiryForm(

            request.POST
        )

        if form.is_valid():

            inquiry=form.save()


            send_mail(

                subject='Catering Inquiry Received',

                message=f'''

Hello {inquiry.full_name},

Thank you for contacting our Catering Platform.

We have received your inquiry successfully.

Event Type: {inquiry.event_type}
Guests: {inquiry.guests}
Date: {inquiry.event_date}

Our team will contact you within 24–48 hours.

Thank you.

Catering Platform Team
''',

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[

                    inquiry.email

                ],

                fail_silently=True
            )


            send_mail(

                subject='New Catering Inquiry',

                message=f'''

New inquiry received:

Name:
{inquiry.full_name}

Email:
{inquiry.email}

Phone:
{inquiry.phone}

Event:
{inquiry.event_type}

Guests:
{inquiry.guests}

Budget:
{inquiry.budget}

''',

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[

                    settings.EMAIL_HOST_USER
                ],

                fail_silently=True

            )


            messages.success(

                request,

                'Inquiry submitted successfully. Please check your email confirmation.'

            )

            return redirect(
                'inquiry'
            )


    context={

        'form':form
    }

    return render(

        request,
        'inquiries/inquiry.html',
        context
    )