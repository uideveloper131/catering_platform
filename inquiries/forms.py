from django import forms
from .models import Inquiry

from datetime import date
import re


class InquiryForm(forms.ModelForm):

    class Meta:

        model = Inquiry

        exclude = [

            'created',
            'updated',
            'status'

        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'company': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'event_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'event_date': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),

            'flexible_date': forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            ),

            'event_time': forms.TimeInput(
                attrs={
                    'class':'form-control',
                    'type':'time'
                }
            ),

            'guests': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),

            'venue': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'indoor_outdoor': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),

            'cuisine': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Indian, Italian, Indian-Italian Fusion'
                }
            ),

            'service_style': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),

            'dietary_requirements': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3
                }
            ),

            'services_needed': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3
                }
            ),

            'budget': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Budget range'
                }
            ),

            'event_details': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4
                }
            ),

            'hear_about': forms.Select(
                attrs={
                    'class':'form-select'
                }
            )

        }


    # Full Name Validation

    def clean_full_name(self):

        full_name=self.cleaned_data.get(
            'full_name'
        )

        if len(full_name)<3:

            raise forms.ValidationError(

                'Name should contain minimum 3 characters'

            )

        return full_name


    # Phone Validation

    def clean_phone(self):

        phone=self.cleaned_data.get(
            'phone'
        )

        if not re.match(

            r'^\+?[0-9]{10,15}$',

            phone

        ):

            raise forms.ValidationError(

                'Enter a valid phone number'

            )

        return phone


    # Event Date Validation

    def clean_event_date(self):

        event_date=self.cleaned_data.get(
            'event_date'
        )

        if event_date < date.today():

            raise forms.ValidationError(

                'Event date cannot be in the past'

            )

        return event_date


    # Budget Validation

    def clean_budget(self):

        budget=self.cleaned_data.get(
            'budget'
        )

        if len(budget)<2:

            raise forms.ValidationError(

                'Enter a valid budget'

            )

        return budget


    # Cuisine Validation

    def clean_cuisine(self):

        cuisine=self.cleaned_data.get(
            'cuisine'
        )

        if len(cuisine)<3:

            raise forms.ValidationError(

                'Cuisine preference is too short'

            )

        return cuisine