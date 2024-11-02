from django.db import models
from products.models import Product
from django.core.exceptions import ValidationError

class City(models.Model):
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name 

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.quantity > self.product.quantity:
            raise ValidationError(f'Not enough stock available for {self.product.name}. Available: {self.product.quantity}')
        
        self.product.quantity -= self.quantity
        self.product.save()  # Guarda los cambios en el producto

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} in {self.city.city_name} - {self.quantity} units'
