# Generated by Django 5.0.6 on 2024-06-24 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_category_product_vender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='vender',
            new_name='vendor',
        ),
    ]
