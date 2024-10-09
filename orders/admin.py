from django.contrib import admin
from django.urls import reverse
from .models import Order
from django.utils.safestring import mark_safe

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id', 'client', 'product', 'quantity', 'created_at', 'in_warehouse', 'delivered', 'paid', 'order_pdf', 'delivery_date','pay_date')
    search_fields = ('client', 'product', 'quantity')

    def order_pdf(self, obj):
        url = reverse('pdf', args=[obj.id])
        return mark_safe(f'<a href="{url}">PDF</a>')
    
    order_pdf.short_description = 'Invoice'

admin.site.register(Order, OrderAdmin)


