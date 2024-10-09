from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("id", "name", "description","quantity", "price", "available", "created", "updated")
    search_fields = ("name", "description")
    list_display_links = ('id', 'name')


admin.site.register(Product, ProductAdmin)