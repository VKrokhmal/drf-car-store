from rest_framework import routers

from carmanager.cars.views import (
    CarViewSet,
    BrandViewSet,
    CategoryViewSet,
    AllCarsViewSet,
    CarInstanceViewSet,
)

router = routers.SimpleRouter()
router.register(r"", AllCarsViewSet, basename="all_cars")
router.register(r"cars", CarViewSet)
router.register(r"brands", BrandViewSet)
router.register(r"categories", CategoryViewSet)
router.register("car-instance", CarInstanceViewSet)
print(router.urls)
