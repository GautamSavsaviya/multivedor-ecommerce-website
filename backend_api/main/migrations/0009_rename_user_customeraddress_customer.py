# Generated by Django 5.0.6 on 2024-06-25 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_customeraddress_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeraddress',
            old_name='user',
            new_name='customer',
        ),
    ]
