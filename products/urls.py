from django.urls import path
from .views import DeleteProductView, ProductsView, ProductFormView, UpdateProductView

urlpatterns = [
    path("", ProductsView.as_view(), name="products"),
    path("add/", ProductFormView.as_view(), name="add_product"),
    path("update/<int:pk>/", UpdateProductView.as_view(), name="update_product"),
    path("delete/<int:pk>/", DeleteProductView.as_view(), name="delete_product"),
]
