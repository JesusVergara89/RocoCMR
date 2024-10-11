from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from products.models import Product
from django.contrib.auth.models import User

class StatsView(LoginRequiredMixin,TemplateView):
    template_name = "sales_stats/stats.html"

class OrderOverView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "sales_stats/order_stats.html"
    context_object_name = "orders"

    def get_queryset(self):
        queryset = Order.objects.all()

        sales_associate_id = self.request.GET.get('sales_associate')
        product_id = self.request.GET.get('product')
        paid = self.request.GET.get('paid')
        in_warehouse = self.request.GET.get('in_warehouse')
        delivered = self.request.GET.get('delivered')
        canceled = self.request.GET.get('canceled')

        if sales_associate_id:
            queryset = queryset.filter(sales_associate_id=sales_associate_id)

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        if paid is not None and paid != '':
            queryset = queryset.filter(paid=paid)

        if in_warehouse is not None and in_warehouse != '':
            queryset = queryset.filter(in_warehouse=in_warehouse)

        if delivered is not None and delivered != '':
            queryset = queryset.filter(delivered=delivered)

        if canceled is not None and canceled != '':
            queryset = queryset.filter(canceled=canceled)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_associates'] = User.objects.all()
        context['products'] = Product.objects.all()
        return context
    
class PieChartOverViewProduct(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'sales_stats/piechart.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        stock_data = {}

        for product in context['products']:
            orders_for_product = orders.filter(product=product)
            ordered_quantity = orders_for_product.aggregate(Sum('quantity'))['quantity__sum'] or 0
            delivered_quantity = orders_for_product.filter(delivered=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
            paid_quantity = orders_for_product.filter(paid=True).aggregate(Sum('quantity'))['quantity__sum'] or 0
            in_warehouse_quantity = orders_for_product.filter(in_warehouse=True).aggregate(Sum('quantity'))['quantity__sum'] or 0

            total_stock = product.quantity

            ordered_percentage = (ordered_quantity / total_stock * 100) if total_stock > 0 else 0
            delivered_percentage = (delivered_quantity / total_stock * 100) if total_stock > 0 else 0
            paid_percentage = (paid_quantity / total_stock * 100) if total_stock > 0 else 0
            in_warehouse_percentage = (in_warehouse_quantity / total_stock * 100) if total_stock > 0 else 0
            new_stock_percentage = 100 - ordered_percentage - delivered_percentage - paid_percentage - in_warehouse_percentage

            stock_data[product.name] = {
                'stock': total_stock,
                'ordered': ordered_quantity,
                'delivered': delivered_quantity,
                'paid': paid_quantity,
                'in_warehouse': in_warehouse_quantity,
                'ordered_percentage': ordered_percentage,
                'delivered_percentage': delivered_percentage,
                'paid_percentage': paid_percentage,
                'in_warehouse_percentage': in_warehouse_percentage,
                'new_stock_percentage': new_stock_percentage
            }

        context['stock_data'] = stock_data

        return context
    
class SellerByMoneyRecovery(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'sales_stats/seller_by_money_recovery.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = Order.objects.all()
        sales_associate_id = self.request.GET.get('sales_associate')
        product_id = self.request.GET.get('product')
        paid = self.request.GET.get('paid')
        delivered = self.request.GET.get('delivered')
        canceled = self.request.GET.get('canceled')

        if sales_associate_id:
            queryset = queryset.filter(sales_associate_id=sales_associate_id)

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        if paid is not None and paid != '':
            queryset = queryset.filter(paid=paid)

        if delivered is not None and delivered != '':
            queryset = queryset.filter(delivered=delivered)

        if canceled is not None and canceled != '':
            queryset = queryset.filter(canceled=canceled)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sales_associates'] = User.objects.all()
        context['products'] = Product.objects.all()

        orders = context['orders']
        for order in orders:
            order.total_price = order.get_total_price()

        return context





