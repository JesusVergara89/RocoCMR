from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm
from products.models import Product
from django.shortcuts import render
from decimal import Decimal

class OrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        else:
            return Order.objects.filter(sales_associate=self.request.user)
        
class OrderFormView(LoginRequiredMixin, CreateView):
    template_name = "orders/add_order.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders")

    def form_valid(self, form):
        form.instance.sales_associate = self.request.user
        product = get_object_or_404(Product, id=form.cleaned_data['product'].id)
        if product.quantity < form.cleaned_data['quantity']:
            form.add_error('quantity', 'No hay suficiente cantidad en stock.')
            return self.form_invalid(form)
        order = form.save(commit=False) 
        order.in_warehouse = True 
        order.delivered = False
        order.paid = False 
        order.save() 
        product.quantity -= order.quantity
        product.save()
        return super().form_valid(form)

    
class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/update_order.html"
    success_url = reverse_lazy("orders")

    def form_valid(self, form):
        product = form.cleaned_data['product']
        order = self.get_object()
        old_quantity = order.quantity
        new_quantity = form.cleaned_data['quantity']
        quantity_difference = new_quantity - old_quantity
        if quantity_difference < 0: 
            product.quantity += abs(quantity_difference)  
        else:  
            if product.quantity < quantity_difference:
                form.add_error('quantity', 'No hay suficiente cantidad en stock después de actualizar.')
                return self.form_invalid(form)
            product.quantity -= quantity_difference  

        product.save()
        return super().form_valid(form)
    
class DeleteOrderView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/delete_order.html"
    success_url = reverse_lazy("orders")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, '403_error.html', status=403)
        return super().dispatch(request, *args, **kwargs)
    
@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    taxes = order.total_price() * Decimal('0.19')
    
    html = render_to_string('orders/pdf.html', {'order': order, 'taxes': taxes})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=order_{order.id}.pdf'

    weasyprint.HTML(string=html).write_pdf(response)
    
    return response

