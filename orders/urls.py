from django.urls import path
from .views import OrdersView, OrderFormView, OrderUpdateView,DeleteOrderView

urlpatterns = [
    path("", OrdersView.as_view(), name="orders"),
    path('add/', OrderFormView.as_view(), name="add_orders"),
    path('delete/<int:pk>/', DeleteOrderView.as_view(), name="delete_orders"),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name="update_orders"),
]