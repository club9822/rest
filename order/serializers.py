from rest_framework import serializers
from order.models.Cart import Cart
from order.models.Order import Order
from order.models.Discount import Discount
from customuser.models import CustomUser


class CartSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(many=False, queryset=CustomUser.objects.all())

    class Meta:
        model = Cart
        # fields = ('id', 'status', 'user_id',)
        read_only_fields = ('id',)
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class CartDetailSerializer(CartSerializer):
    """ extra data fo each cart """
    orders = OrderSerializer(many=True, read_only=True)
