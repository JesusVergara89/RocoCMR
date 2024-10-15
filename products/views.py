import requests
from django.views import generic
from .models import Product, ProductHistory
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

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
    
class UpdateProductView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form_response = super().form_valid(form)

        ip_address = self.request.META.get('REMOTE_ADDR')
        country = None
        city = None

        if ip_address:
            try:
                location_response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
                if location_response['status'] == 'success':
                    country = location_response.get('country')
                    city = location_response.get('city')
            except Exception as e:
                print(f'Error fetching location: {e}')

        ProductHistory.objects.create(
            product=self.object,
            name=self.object.name,
            price=self.object.price,
            quantity=self.object.quantity,
            available=self.object.available,
            ip_address=ip_address,
            country=country,
            city=city
        )

        return form_response

class ProductFormView(LoginRequiredMixin, generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy("products")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        product = form.save()

        ip_address = self.request.META.get('REMOTE_ADDR')
        country = None
        city = None

        if ip_address:
            try:
                response = requests.get(f'http://ip-api.com/json/{ip_address}').json()
                print(response, 'this is the response')
                if response['status'] == 'success':
                    country = response.get('country')
                    city = response.get('city')
            except Exception as e:
                print(f'Error fetching location: {e}')

        ProductHistory.objects.create(
            product=product,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
            available=product.available,
            ip_address=ip_address,
            country=country,
            city=city
        )

        return super().form_valid(form)
