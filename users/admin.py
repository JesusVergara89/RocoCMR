from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('id','user', 'name', 'email', 'phone', 'address')
    search_fields = ('id','user', 'name', 'email', 'phone', 'address')
    list_display_links = ('id', 'name')

admin.site.register(Profile, ProfileAdmin)





