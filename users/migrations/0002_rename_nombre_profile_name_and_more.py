# Generated by Django 5.1.1 on 2024-10-09 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='telefono',
            new_name='phone',
        ),
    ]