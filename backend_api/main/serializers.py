from rest_framework import serializers
from . import models


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']
        # depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']
        # depth = 1


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        # fields = '__all__'
        fields = ['id', 'vendor', 'category', 'title', 'detail', 'price']
        # depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = ['id', 'vendor', 'category', 'title', 'detail', 'price', 'product_ratings']
        # depth = 1



class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'mobile']
        # depth = 1


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id','user', 'mobile']
        # depth = 1


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id', 'customer','order_time']
        depth = 1

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['id', 'order','product']
        depth = 1


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id', 'customer', 'address']
        depth = 1


class ProductRetingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRetingReview
        fields = ['id', 'customer', 'product', 'ratings', 'review', 'add_time']
        depth = 1


