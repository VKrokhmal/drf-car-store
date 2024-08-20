from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    class Meta:
        verbose_name = "Category"

    class MPTTMeta:
        order_insertion_by = ["name"]

    class CarTypes(models.TextChoices):
        Coupe = "Coupe"
        Cabriolet = "Cabriolet"
        Sedan = "Sedan"
        SUV = "SUV"

    name = models.CharField(max_length=20, choices=CarTypes.choices)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    class Meta:
        verbose_name = "Brand"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    class Meta:
        verbose_name = "Car"

    make = models.ForeignKey("Brand", on_delete=models.PROTECT)
    model = models.CharField(max_length=150)
    year = models.PositiveIntegerField(default="1970")
    odometer = models.PositiveIntegerField(null=True, default="0")
    price = models.PositiveIntegerField(null=True, default="0")
    description = models.CharField(max_length=150, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Car: {self.model}"
