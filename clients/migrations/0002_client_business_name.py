# Generated by Django 5.1.1 on 2024-10-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='business_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]