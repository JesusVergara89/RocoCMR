from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from users.models import Profile

class StatsView(LoginRequiredMixin,TemplateView):
    template_name = "sales_stats/stats.html"


class OrderssAssociateByQuantityProduct(LoginRequiredMixin, ListView):
    model = Order
    template_name = "sales_stats/sales_associate_by_quantity_product.html"
    context_object_name = "sales_associates"

    def get_queryset(self):
        sales_data = (
            Order.objects
            .values('sales_associate__username')  
            .annotate(total_quantity=Sum('quantity'))  
            .order_by('-total_quantity')
        )
        for item in sales_data:
            try:
                profile = Profile.objects.get(user__username=item['sales_associate__username'])
                item['sales_associate_name'] = profile.name  
            except Profile.DoesNotExist:
                item['sales_associate_name'] = 'Perfil no encontrado' 

        return sales_data
    

