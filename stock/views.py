from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import CityForm, StockForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import City, Stock


class CityStockView(LoginRequiredMixin,TemplateView):
    template_name = "stock/city_stock.html"

class CityView(LoginRequiredMixin, ListView):
    model = City
    template_name = "stock/cities.html"
    context_object_name = "cities"    

class CityFormView(LoginRequiredMixin, generic.FormView):
    template_name = "stock/add_city.html"
    form_class = CityForm
    success_url = reverse_lazy("cities")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class StockFormView(LoginRequiredMixin, generic.FormView):
    template_name = "stock/add_stock.html"
    form_class = StockForm
    success_url = reverse_lazy("cities")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

