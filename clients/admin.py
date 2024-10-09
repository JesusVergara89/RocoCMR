from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('id','name', 'last_name', 'email', 'phone', 'address', 'is_active', 'sales_associate')
    search_fields = ('name', 'last_name', 'email', 'phone', 'address')
    list_display_links = ('id', 'name')

admin.site.register(Client, ClientAdmin)
