# Generated by Django 5.1.1 on 2024-10-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]