from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('clients/', include('clients.urls')),
    path('orders/', include('orders.urls')),
    path('stats/', include('sales_stats.urls')),
    path('stock/', include('stock.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
