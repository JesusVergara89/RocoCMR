from django import forms
from django.forms import ModelForm
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'last_name','business_name' ,'email', 'phone', 'address', 'is_active')
        widgets = {
            'is_active': forms.CheckboxInput
        }