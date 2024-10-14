from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=200)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url_image = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    
class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True) 
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'History of {self.product.name} at {self.created}'


