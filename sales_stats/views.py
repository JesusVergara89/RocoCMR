from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from products.models import Product
from stock.models import Stock
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class StatsView(LoginRequiredMixin,TemplateView):
    template_name = "sales_stats/stats.html"

class PieChartViews(LoginRequiredMixin, TemplateView):
    template_name  = "sales_stats/piechart_templates.html"

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

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')        

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

        if start_date:
            queryset = queryset.filter(created_at__gte=start_date)

        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)
            
        queryset = queryset.order_by('-created_at')            

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_associates'] = User.objects.all()
        context['products'] = Stock.objects.all()
        return context
    
class PieChartStockVs(LoginRequiredMixin, ListView):
    model = Stock
    context_object_name = 'products'

    def get_queryset(self):
        return Stock.objects.filter(available=True)

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

            ordered_percentage = (ordered_quantity / (total_stock + ordered_quantity ) * 100) if total_stock > 0 else 0
            delivered_percentage = (delivered_quantity / (total_stock + delivered_quantity) * 100) if total_stock > 0 else 0
            paid_percentage = (paid_quantity / (total_stock + paid_quantity) * 100) if total_stock > 0 else 0
            in_warehouse_percentage = (in_warehouse_quantity / (total_stock + in_warehouse_quantity) * 100) if total_stock > 0 else 0
            new_stock_orders = 100 - ordered_percentage
            new_stock_paid = 100 - paid_percentage
            new_stock_in_warehouse = 100 - in_warehouse_percentage
            new_stock_delivered = 100 - delivered_percentage

            stock_data[product.name] = {
                'stock': total_stock,
                'ordered': ordered_quantity,
                'delivered': delivered_quantity,
                'paid': paid_quantity,
                'in_warehouse': in_warehouse_quantity,
                'ordered_percentage': ordered_percentage,
                'delivered_percentage': delivered_percentage,
                'paid_percentage': paid_percentage,
                'new_stock_orders': new_stock_orders,
                'new_stock_paid': new_stock_paid,
                'new_stock_in_warehouse': new_stock_in_warehouse,
                'new_stock_delivered': new_stock_delivered
            }

        context['stock_data'] = stock_data

        return context
    
    def get_template_names(self):          
        if hasattr(self, 'template_name') and self.template_name is not None:
            return [self.template_name]
        return ['sales_stats/order_vs_stock.html']

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

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

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

        if start_date:
            queryset = queryset.filter(created_at__gte=start_date)

        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)

        queryset = queryset.order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sales_associates'] = User.objects.all()
        context['products'] = Stock.objects.all()

        orders = context['orders']
        for order in orders:
            order.total_price = order.get_total_price()

        return context

class OrdersProgress(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'sales_stats/orders_progress.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = Order.objects.all()
        sales_associate_id = self.request.GET.get('sales_associate')
        product_id = self.request.GET.get('product')

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if sales_associate_id:
            queryset = queryset.filter(sales_associate_id=sales_associate_id)

        if product_id:
            queryset = queryset.filter(product_id=product_id)

        if start_date:
            queryset = queryset.filter(created_at__gte=start_date)

        if end_date:
            queryset = queryset.filter(created_at__lte=end_date)

        queryset = queryset.order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sales_associates'] = User.objects.all()
        context['products'] = Stock.objects.all()

        for order in context['orders']:
            order.delivery_status_color = 'red'
            order.payment_status_color = 'red'
            order.status = 'Not delivered'
            order.last_delivery_date = order.created_at + timedelta(days=1)

            if order.delivered:
                if order.delivery_date:
                    if order.delivery_date <= order.last_delivery_date:
                        order.delivery_status_color = 'green'
                        order.status = 'Delivery on time'
                    else:
                        order.status = 'Delivery delay'
                    order.last_paid_date = order.delivery_date + timedelta(days=1)

                    if order.paid:
                        if order.pay_date:
                            if order.pay_date <= order.last_paid_date:
                                order.payment_status_color = 'green'
                            else:
                                order.payment_status_color = 'red'
                                order.status = 'Late payment'
                        else:
                            order.status = 'Pending payment'
                    else:
                        if timezone.now().date() <= order.last_paid_date:
                            order.payment_status_color = 'orange'
                            order.status = 'Payment pending (on time)'
                        else:
                            order.payment_status_color = 'red'
                            order.status = 'Payment overdue'
                else:
                    order.status = 'Delivered without date'
                    order.last_paid_date = None
            elif order.canceled:
                    order.delivery_status_color = 'red'
                    order.payment_status_color = 'red'
                    order.status = 'Canceled'
                    order.last_paid_date = None
            else:
                if timezone.now().date() < order.last_delivery_date:
                    order.delivery_status_color = 'orange'
                    order.payment_status_color = 'orange'
                    order.status = 'Delivery on time'
                    order.last_paid_date = None
                elif timezone.now().date() > order.last_delivery_date:
                    order.delivery_status_color = 'red'
                    order.payment_status_color = 'red'
                    order.status = 'Delivery delay' 

        return context