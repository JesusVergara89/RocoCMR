from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Order

def send_order_invoice(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'My Shop - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent order.'

    fixed_emails = ['jesusmanuelv1989@gmail.com', 'jesusvergara890109@gmail.com']

    client_email = order.client.email

    recipients = [client_email] + fixed_emails

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipients)

    html = render_to_string('orders/pdf.html', {'order': order})

    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)
    out.seek(0) 
    email.attach(f'order_{order.id}.pdf', out.read(), 'application/pdf')

    try:
        email.send()
    except Exception as e:
        print(f"Error sending email: {e}")




