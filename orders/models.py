from django.db import models
from clients.models import Client
from products.models import Product
from stock.models import Stock
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils import timezone

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500, null=True, blank=True)
    sales_associate = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )
    quantity = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    in_warehouse = models.BooleanField(default=True)
    delivered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    delivery_date = models.DateField(null=True, blank=True)
    pay_date = models.DateField(null=True, blank=True)
    canceled = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.client} purchased {self.quantity} of {self.product}'
    
    def subtotal_price(self):
        if isinstance(self.product.price, Decimal):
            return self.quantity * self.product.price
        else:
            raise ValueError("El precio del producto debe ser un Decimal.")
        
    def get_taxes(self):
        if isinstance(self.product.price, Decimal):
            return self.subtotal_price() * Decimal('0.05')
        else:
            raise ValueError("El precio del producto debe ser un Decimal.")
    
    def get_hipo_consumption(self):
        if isinstance(self.product.price, Decimal):
            return self.subtotal_price() * Decimal('0.08')
        else:
            raise ValueError("El precio del producto debe ser un Decimal.")
    
    def get_total_price(self):
        return self.subtotal_price() + self.get_taxes()

    def save(self, *args, **kwargs):
        if self.canceled:
            self.quantity = 0

        if self.delivered and not self.delivery_date and not self.in_warehouse:
            self.delivery_date = timezone.now().date()
            
        elif not self.delivered:
            self.delivery_date = None

        if self.paid and not self.pay_date:
            self.pay_date = timezone.now().date()
        elif not self.paid:
            self.pay_date = None

        super().save(*args, **kwargs)
    

