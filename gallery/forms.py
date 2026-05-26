from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):

    class Meta:

        model=Gallery

        fields='__all__'

        widgets={

            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'category':forms.TextInput(
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