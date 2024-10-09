from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id','client', 'product', 'quantity', 'created_at', 'in_warehouse', 'delivered', 'paid')
    search_fields = ('client', 'product', 'quantity')

admin.site.register(Order, OrderAdmin)
