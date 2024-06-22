from . import serializers
from rest_framework import generics
from . import models

# Create your views here.


class VendorList(generics.ListAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
