# Generated by Django 5.0.6 on 2024-06-25 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_customeraddress_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_addresses', to='main.customer'),
        ),
    ]
