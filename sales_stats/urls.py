from django.urls import path
from .views import StatsView, OrderOverView, PieChartOverViewProduct

urlpatterns = [
    path("", StatsView.as_view(), name="stats"),
    path('order-stats/', OrderOverView.as_view(), name='order_stats'),
    path('order-pie-chart/', PieChartOverViewProduct.as_view(), name='order_pie_chart'),
]
