from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, VendorsView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path('vendors/', VendorsView.as_view(), name='vendors')
]
