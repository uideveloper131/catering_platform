from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model=MenuItem
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
            'brand':forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),
            'active':forms.CheckboxInput(
                attrs={
                    'class':'form-check-input'
                }
            )

        }