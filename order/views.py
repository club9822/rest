from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from order.models.Cart import Cart
from order.models.Order import Order
from order.models.Discount import Discount

from order.serializers import CartSerializer, OrderSerializer, DiscountSerializer, CartDetailSerializer


# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(customuser=self.request.customuser)

    def get_serializer_class(self):
        """:return approporatte serializer class """
        if self.action == 'retrieve':
            return CartDetailSerializer
        return self.serializer_class


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

# class
