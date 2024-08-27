from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BrandSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="brand_name")

    class Meta:
        model = Brand
        fields = ["name"]


class CarSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = CategorySerializer()
    make_field = BrandSerializer(source="make", read_only=True)

    class Meta:
        model = Car
        fields = "__all__"

    def create(self, validated_data):
        cat_add = validated_data.pop("category")
        print(cat_add)
        print(cat_add)

        return super().create(validated_data)


class CarInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInstance
        fields = "__all__"

    car = CarSerializer()
