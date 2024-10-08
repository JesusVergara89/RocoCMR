from django.views import generic
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

class ProductsView(generic.ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

class DeleteProductView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('products')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)

class ProductFormView(LoginRequiredMixin, generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy("products")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
