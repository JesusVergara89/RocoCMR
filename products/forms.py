from django import forms
from .models import Product
from django.utils.timezone import now 

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Product name")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Product price")    
    description = forms.CharField(max_length=200, label="Product description")
    quantity = forms.IntegerField(label="Product quantity")
    available = forms.BooleanField(initial=True, label="Product availability", required=False)
    created = forms.DateTimeField(label="Created at", disabled=True, initial=now)
    updated = forms.DateTimeField(label="Last updated", disabled=True, initial=now)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            quantity= self.cleaned_data["quantity"],
            available=self.cleaned_data["available"],
        )
