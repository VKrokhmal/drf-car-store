from rest_framework import routers

from carmanager.cars.views import CarViewSet, BrandViewSet

router = routers.SimpleRouter()
router.register(r"cars", CarViewSet)
router.register(r"brands", BrandViewSet)
print(router.urls)
