from django.urls import path
from .views import ClientView, ClientCreateView

urlpatterns = [
    path("", ClientView.as_view(), name="clients"),
    path("add/", ClientCreateView.as_view(), name="add_clients"),
]