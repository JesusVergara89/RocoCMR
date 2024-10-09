from django import forms
from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('client', 'product', 'comments', 'sales_associate', 'quantity', 'in_warehouse', 'delivered', 'paid')
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'in_warehouse': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'delivered': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'client': 'Client',
            'product': 'Product',
            'quantity': 'Quantity',
            'in_warehouse': 'In Warehouse',
            'delivered': 'Delivered',
            'paid': 'Paid',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super(OrderForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['sales_associate'].initial = user  
