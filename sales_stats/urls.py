from django.urls import path
from .views import StatsView, OrderOverView,  SellerByMoneyRecovery, OrdersProgress, PieChartViews, PieChartSctockVs

urlpatterns = [
    path("", StatsView.as_view(), name="stats"),
    path('order-stats/', OrderOverView.as_view(), name='order_stats'),
    path('pie-charts/', PieChartViews.as_view(), name='pie_charts'),
    path('order-vs-stock/', PieChartSctockVs.as_view(), name='order_vs_stock'),
    path('paid-vs-stock/', PieChartSctockVs.as_view(template_name="sales_stats/paid_vs_stock.html"), name='paid_vs_stock'),
    path('delivered-vs-stock/', PieChartSctockVs.as_view(template_name="sales_stats/delivered_vs_stock.html"), name='delivered_vs_stock'),
    path('order-money-recovery/', SellerByMoneyRecovery.as_view(), name='seller_by_money_recovery'),
    path('order-progress/', OrdersProgress.as_view(), name='order_progress'),
]
