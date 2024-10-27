from django import forms
from .models import Stock, City
from django.utils.timezone import now 

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'city', 'quantity']
        labels = {
            'product': "Product name",
            'city': "City name",
            'quantity': "Product quantity",
        }

    created = forms.DateTimeField(label="Created at", disabled=True, initial=now)
    updated = forms.DateTimeField(label="Last updated", disabled=True, initial=now)

    def save(self, commit=True):
        stock = super().save(commit=False)
        stock.updated = now() 
        if commit:
            stock.save()
        return stock
    

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city_name', 'state_name', 'country']
        labels = {
            'city_name': "City name",
            'state_name': "State name",
            'country': "Country name",
        }

    created = forms.DateTimeField(label="Created at", disabled=True, initial=now)
    updated = forms.DateTimeField(label="Last updated", disabled=True, initial=now)

    def save(self, commit=True):
        city = super().save(commit=False)
        city.updated = now() 
        if commit:
            city.save()
        return city