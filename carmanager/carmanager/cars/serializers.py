from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_field = CategorySerializer(source="category", read_only=True)
    make_field = BrandSerializer(source="make", read_only=True)

    class Meta:
        model = Car
        fields = "__all__"
