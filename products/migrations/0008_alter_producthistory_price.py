# Generated by Django 5.1.1 on 2024-10-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_producthistory_updated_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthistory',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
