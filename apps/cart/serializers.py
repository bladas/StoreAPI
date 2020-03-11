from django.db.models import Max, Min
from rest_framework import serializers

from .models import CartItem


class CartObjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'
