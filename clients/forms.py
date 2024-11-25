from django import forms
from django.forms import ModelForm
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = (
            "name",
            "last_name",
            "business_name",
            "email",
            "phone",
            "address",
            "is_active",
            "city",
            "state",
            "tax_identification_number",
            "tax_regime",
            "social_name",
        )
        widgets = {"is_active": forms.CheckboxInput}
