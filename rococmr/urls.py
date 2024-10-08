from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('clients/', include('clients.urls')),
    path('admin/', admin.site.urls),
]
