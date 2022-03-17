from rest_framework import serializers
from .models import Product
from .models import Order
from .models import OrderDetail


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id_PK', 'name', 'price', 'stock')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id_PK', 'date_time')

class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('order', 'quantity', 'product')