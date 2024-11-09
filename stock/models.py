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

    name = models.CharField(max_length=100, default="Nombre no disponible")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(max_length=200, default="Sin descripción")
    url_image = models.URLField(max_length=500, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = self.product.name
        self.price = self.product.price
        self.description = self.product.description
        self.url_image = self.product.url_image

        if not self.pk: 
            if self.quantity > self.product.quantity:
                raise ValidationError(f'Not enough stock available for {self.product.name}. Available: {self.product.quantity}')
            self.product.quantity -= self.quantity
            self.product.save() 

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} in {self.city.city_name} - {self.quantity} units'
