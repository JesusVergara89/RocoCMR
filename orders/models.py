from django.db import models
from clients.models import Client
from products.models import Product
from django.contrib.auth.models import User

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500, null=True, blank=True)
    sales_associate = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )
    quantity = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    in_warehouse = models.BooleanField(default=True)
    delivered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.client} purchased {self.quantity} of {self.product}'
    
    def total_price(self):
        return self.quantity * self.product.price 
    

