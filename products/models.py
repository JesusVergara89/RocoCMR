from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    def __str__(self):
        return f'History of {self.product.name} at {self.created}'


@receiver(post_save, sender=Product)
def create_product_history(sender, instance, created, **kwargs):
    ProductHistory.objects.create(
        product=instance,
        name=instance.name,
        price=instance.price,
        quantity=instance.quantity,
        available=instance.available
    )
