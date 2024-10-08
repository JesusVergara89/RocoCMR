from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('name', 'last_name', 'email', 'phone', 'address', 'is_active', 'sales_associate')
    search_fields = ('name', 'last_name', 'email', 'phone', 'address')

admin.site.register(Client, ClientAdmin)
