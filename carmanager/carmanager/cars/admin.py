from django.contrib import admin

from .models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "brand", "category")
    list_display_links = ("id", "model", "brand", "category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
    list_display_links = ("id", "category_name")


admin.site.register(Brand)
# admin.site.register(CarItem)


@admin.register(CarItem)
class CarItemAdmin(admin.ModelAdmin):
    list_display = ("uuid",)
