from rest_framework import routers
from .views import OrderViewSet, OrderItemViewSet, CartViewSet, CartItemViewSet

router = routers.SimpleRouter()
router.register("order-item", OrderItemViewSet)
router.register("order", OrderViewSet)
router.register("cart-item", CartItemViewSet)
router.register("cart", CartViewSet)
