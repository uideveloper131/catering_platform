from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):

    class Meta:

        model = Brand

        fields='__all__'

        widgets={

            'name':forms.TextInput(
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