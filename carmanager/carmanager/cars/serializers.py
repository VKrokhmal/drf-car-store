from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id"]


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        # fields = ["brand"]
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # brand = BrandSerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())

    class Meta:
        model = Car
        fields = "__all__"


class CarInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = "__all__"

    car = CarSerializer()
