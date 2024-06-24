from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Vendor Model
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


# Product Category
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

# Product
class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='product_vendor')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, related_name='product_category')
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=False)
    price = models.FloatField()

    def __str__(self):
        return self.title


# Customer Model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username


# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_customer')
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.user.username} - Order'

# Order Items Model
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')

    def __str__(self):
        return self.product.title
    
    class Meta:
        verbose_name = "Order Items"
        verbose_name_plural = "Order Items"