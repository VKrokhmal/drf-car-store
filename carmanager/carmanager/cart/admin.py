from django.contrib import admin
from .models import CartItem, Cart, OrderItem, Order

# Register your models here.
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
