from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):

    STATE_CHOICES = [
        ('autoretenedor', 'Autoretenedor'),
        ('regimen_simplificado', 'Régimen Simplificado'),
    ] 

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    social_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    tax_identification_number = models.CharField(
        max_length=150,
        null=True,
        unique=True,
        blank=True
        )
    tax_regime = models.CharField(
        max_length=150, 
        choices=STATE_CHOICES, 
        null=True, 
        blank=True
    )
    sales_associate = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"
