from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format

from .models import Car, Brand, Category, CarItem
from .serializers import (
    CarSerializer,
    BrandSerializer,
    CategorySerializer,
    CarInstanceSerializer,
)


class AllCarsViewSet(ViewSet):
    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # # permission_classes = (IsAuthenticatedOrReadOnly,)
    #
    # @action(
    #     methods=["get"],
    #     detail=False,
    #     url_path=r"category/(?P<category>\w+)/all",
    #     url_name="all",
    # )
    # def list_cars_by_category(self, request, category=None):
    #     serializer = CarSerializer(
    #         self.queryset.filter(category__name=category), many=True
    #     )
    #     q = self.queryset.filter(category__name=category)
    #     sqlformatter = format(str(q.query), reindent=True)
    #     print(highlight(sqlformatter, SqlLexer(), TerminalFormatter()))
    #     print(connection.queries)
    #     return Response(serializer.data)


class CarInstanceViewSet(ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CarInstanceSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
