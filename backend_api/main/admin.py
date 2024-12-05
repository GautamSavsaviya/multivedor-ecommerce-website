from django.contrib import admin
from . import models

# Register your models here.

# Vendor
admin.site.register(models.Vendor)


# Customer
admin.site.register(models.Customer)
admin.site.register(models.CustomerAddress)


# Product 
admin.site.register(models.ProductCategory)
admin.site.register(models.Product)
admin.site.register(models.ProductRetingReview)


# Order
admin.site.register(models.Order)
admin.site.register(models.OrderItems)