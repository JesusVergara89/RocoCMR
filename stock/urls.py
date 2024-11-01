from django.urls import path
from .views import CityStockView, CityView, CityFormView

urlpatterns = [
    path("", CityStockView.as_view(), name="city_stock"),
    path('cities/', CityView.as_view(), name="cities"),
    path('add_city/', CityFormView.as_view(), name="add_city"),
]
