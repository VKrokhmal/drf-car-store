from django.contrib import admin

from .models import *

#
# class CarInstanseInline(admin.TabularInline):
#     model = CarInstance
#
#
# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     inlines = [CarInstanseInline]


# Register your models here.
admin.site.register(Car)  # already registered above
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CarInstance)
