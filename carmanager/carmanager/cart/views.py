from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CartSerializer,
    CartItemSerializer,
    OrderItemSerializer,
    OrderSerializer,
)
from .models import CartItem, Cart, OrderItem, Order


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
