from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

class RegisterView(LoginRequiredMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)
    
class VendorsView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/vendors.html"
    context_object_name = "vendors"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.select_related('profile').all()

