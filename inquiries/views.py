from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import date

from .forms import InquiryForm


def inquiry(request):

    form=InquiryForm()

    if request.method=="POST":

        form=InquiryForm(

            request.POST
        )

        if form.is_valid():

            inquiry=form.save()


            try:

                # Customer Email

                send_mail(

                    subject='Catering Inquiry Received',

                    message=f'''

Hello {inquiry.full_name},

Thank you for contacting our Catering Platform.

We have successfully received your inquiry.

Event Type:
{inquiry.event_type}

Guests:
{inquiry.guests}

Event Date:
{inquiry.event_date}

Our team will contact you within 24–48 hours.

Thank you.

Catering Platform Team

''',

                    from_email=settings.EMAIL_HOST_USER,

                    recipient_list=[

                        inquiry.email
                    ],

                    fail_silently=False

                )


                # Admin Email

                send_mail(

                    subject='New Catering Inquiry Received',

                    message=f'''

New Catering Inquiry

Customer Name:
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

Venue:
{inquiry.venue}

''',

                    from_email=settings.EMAIL_HOST_USER,

                    recipient_list=[

                        settings.EMAIL_HOST_USER
                    ],

                    fail_silently=False

                )


            except Exception:

                messages.warning(

                    request,

                    'Inquiry saved successfully but email notification could not be sent.'

                )


            messages.success(

                request,

                'Inquiry submitted successfully , We will respond within 24–48 hours.'

            )


            return redirect(

                'inquiry'
            )


        else:

            messages.error(

                request,

                'Please correct the errors below.'

            )


    context={

        'form':form

    }

    return render(

        request,
        'inquiries/inquiry.html',
        context
    )