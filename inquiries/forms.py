from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):

    class Meta:

        model = Inquiry

        exclude = [

            'created',
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
                    'placeholder':'Indian, Italian, Indian-Italian Fusion, Chef Choice'
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

            'hear_about': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Google, Instagram, Referral'
                }
            )

        }