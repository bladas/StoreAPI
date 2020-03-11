from django.db.models import Max, Min
from rest_framework import serializers

from apps.product.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(ProductListSerializer):
    class Meta:
        model = Product
        fields = '__all__'