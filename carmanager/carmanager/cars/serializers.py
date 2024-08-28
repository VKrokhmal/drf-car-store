from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]


class BrandSerializer(serializers.ModelSerializer):
    brand = serializers.CharField()

    class Meta:
        model = Brand
        fields = ["brand"]


class CarSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category = CategorySerializer()

    make_field = BrandSerializer(source="make", read_only=True)
    # category = SlugRelatedField(slug_field="category_name", read_only=True)
    # brand = SlugRelatedField(slug_field="brand", read_only=True)

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
