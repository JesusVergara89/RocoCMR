from django.urls import path
from .views import StatsView, OrderOverView, PieChartOrdersVsStock, SellerByMoneyRecovery, OrdersProgress, PieChartViews, PieChartPaidVsStock, PieChartDeliveredVsStock

urlpatterns = [
    path("", StatsView.as_view(), name="stats"),
    path('order-stats/', OrderOverView.as_view(), name='order_stats'),
    path('pie-charts/', PieChartViews.as_view(), name='pie_charts'),
    path('order-vs-stock/', PieChartOrdersVsStock.as_view(), name='order_vs_stock'),
    path('paid-vs-stock/', PieChartPaidVsStock.as_view(), name='paid_vs_stock'),
    path('delivered-vs-stock/', PieChartDeliveredVsStock.as_view(), name='delivered_vs_stock'),
    path('order-money-recovery/', SellerByMoneyRecovery.as_view(), name='seller_by_money_recovery'),
    path('order-progress/', OrdersProgress.as_view(), name='order_progress'),
]
