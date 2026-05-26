from django import forms
from .models import EventService
from .models import OfferPackage
from .models import FAQ
from .models import Testimonial
from .models import ContactInfo
from .models import Statistic
from .models import CTASection

class EventForm(forms.ModelForm):
    class Meta:
        model = EventService
        fields = '__all__'
        widgets={
            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4
                }
            ),
            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )
        }

class OfferForm(forms.ModelForm):
    class Meta:
        model=OfferPackage
        fields='__all__'
        widgets={
            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'subtitle':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'price':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )
        }

class FAQForm(forms.ModelForm):

    class Meta:

        model=FAQ

        fields='__all__'

        widgets={

            'question':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'answer':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':5
                }
            ),

            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )

        }

class TestimonialForm(forms.ModelForm):

    class Meta:

        model=Testimonial

        fields='__all__'

        widgets={

            'customer_name':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'review':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':5
                }
            ),

            'rating':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'min':1,
                    'max':5
                }
            ),

            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )

        }


class ContactInfoForm(forms.ModelForm):

    class Meta:

        model=ContactInfo

        fields='__all__'

        widgets={

            'email':forms.EmailInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'phone':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'address':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3
                }
            ),

            'business_hours':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'facebook':forms.URLInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'instagram':forms.URLInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'youtube':forms.URLInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'google_map':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':3
                }
            ),

            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )

        }

class StatisticForm(forms.ModelForm):
    class Meta:
        model=Statistic
        fields='__all__'
        widgets={
            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'value':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )
        }

class CTAForm(forms.ModelForm):

    class Meta:

        model=CTASection

        fields='__all__'

        widgets={

            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'description':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4
                }
            ),

            'button_text':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )

        }