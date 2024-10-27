from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CityForm, StockForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import City, Stock

class StockFormView(LoginRequiredMixin, generic.FormView):
    template_name = "stock/add_city.html"

    form_class = StockForm
    success_url = reverse_lazy("add")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  

