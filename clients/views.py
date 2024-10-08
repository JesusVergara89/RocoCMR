from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Client
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ClientForm


class ClientView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/clients.html"
    context_object_name = "clients"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(sales_associate=self.request.user, is_active=True)


class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = "clients/add_client.html"
    form_class = ClientForm
    success_url = reverse_lazy("clients")

    def form_valid(self, form):
        form.instance.sales_associate = self.request.user
        return super().form_valid(form)
