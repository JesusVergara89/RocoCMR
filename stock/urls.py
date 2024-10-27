from django.urls import path
from .views import StockFormView

urlpatterns = [
    path("", StockFormView.as_view(), name="add_city"),
]
