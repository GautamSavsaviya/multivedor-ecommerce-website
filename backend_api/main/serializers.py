from rest_framework import serializers
from . import models


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']
        depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id','user', 'address']
        depth = 1


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        # fields = '__all__'
        fields = ['id', 'vendor', 'category', 'title', 'detail', 'price']
        depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'vendor', 'category', 'title', 'detail', 'price']
        depth = 1