from django import forms
from .models import Product
from django.utils.timezone import now 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'quantity', 'available', 'url_image']
        labels = {
            'name': "Product name",
            'price': "Product price",
            'description': "Product description",
            'quantity': "Product quantity",
            'available': "Product availability",
            'url_image': "Product image URL",
        }

    created = forms.DateTimeField(label="Created at", disabled=True, initial=now)
    updated = forms.DateTimeField(label="Last updated", disabled=True, initial=now)

    def save(self, commit=True):
        product = super().save(commit=False)
        product.updated = now()  # Actualiza el campo "updated" con la fecha y hora actuales
        if commit:
            product.save()
        return product
