from django.urls import path
from .views import StatsView, OrderOverView, PieChartOverViewProduct, SellerByMoneyRecovery

urlpatterns = [
    path("", StatsView.as_view(), name="stats"),
    path('order-stats/', OrderOverView.as_view(), name='order_stats'),
    path('order-pie-chart/', PieChartOverViewProduct.as_view(), name='order_pie_chart'),
    path('order-money-recovery/', SellerByMoneyRecovery.as_view(), name='seller_by_money_recovery'),
]
