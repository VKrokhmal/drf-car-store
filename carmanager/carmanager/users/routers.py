from rest_framework import routers

from .views import ProfileViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"users", UserViewSet)

print(router.urls)
