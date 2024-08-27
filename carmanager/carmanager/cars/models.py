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

    name = models.CharField(max_length=20, choices=CarTypes.choices, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    class Meta:
        verbose_name = "Brand"

    brand_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    class Meta:
        verbose_name = "Car"

    brand = models.ForeignKey("Brand", on_delete=models.PROTECT)
    model = models.CharField(max_length=150)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.model


class CarInstance(models.Model):
    class Meta:
        verbose_name = "CarInstance"

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    odometer = models.PositiveIntegerField(null=True, default="0")
    year = models.PositiveIntegerField(default="1970")
    description = models.CharField(max_length=150, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
