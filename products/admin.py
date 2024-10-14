from django.contrib import admin
from .models import Product, ProductHistory

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("id", "name", "description","quantity", "price", "available", "created", "updated")
    search_fields = ("name", "description")
    list_display_links = ('id', 'name')

class ProductHistoryAdmin(admin.ModelAdmin):
    model = ProductHistory
    list_display = ("id", "product", "created", "updated", "name", "price", "quantity", "available")
    search_fields = ("product", "name")
    list_display_links = ('id', 'product')  


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductHistory, ProductHistoryAdmin)