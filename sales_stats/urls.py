from django.urls import path
from .views import StatsView, OrderssAssociateByQuantityProduct

urlpatterns = [
    path("", StatsView.as_view(), name="stats"),
    path("sales-associate-by-quantity-product/", OrderssAssociateByQuantityProduct.as_view(), name="sales_associate_by_quantity_product"),
]
