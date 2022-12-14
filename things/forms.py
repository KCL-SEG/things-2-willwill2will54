"""Forms of the project."""
from django import forms
from .models import *

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.widgets.Textarea(),
            'quantity': forms.widgets.NumberInput()
        }
